# Evaluating tool-calling behavior

**Framework**: Evaluations

Analyze your model’s tool calls against expected trajectories, argument values, and call ordering.

#### Overview

Language models can perform actions beyond text generation by calling tools you define for specific tasks, such as searching a database, controlling a smart device, or calling an external API. The model determines when to call each tool and what arguments to pass based on the user’s request and the tools you provide.

A model that picks the wrong tool, passes incorrect arguments, or calls tools out of order can silently break your app. The Evaluations framework lets you define the tool-calling behavior you expect and rate the model’s actual behavior against it. For guidance on defining success criteria and choosing quality dimensions, see [`Designing specific, measurable criteria in an evaluation suite`](designing-evaluation-criteria.md). For an introduction to the Evaluations framework and how evaluations work, see [`Evaluating language model responses`](evaluating-language-model-responses.md). To see tool-call evaluation in a complete app, see [`Book Tracker: Using Evaluations to evaluate an intelligent feature`](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md).

#### Define Your Tools

Define the tools the model can call. Each tool conforms to the [`Tool`](https://developer.apple.com/documentation/foundationmodels/tool) protocol with a name, description, and a [`Generable`](https://developer.apple.com/documentation/foundationmodels/generable) arguments structure that tells the model which parameters to pass.

This example defines a home automation tool that takes a string and a numeric argument:

```swift
import FoundationModels

struct SetLights: Tool {
    let name = "set_lights"
    let description = "Controls lights in a room. Brightness 0 means off, 100 means full."

    // The arguments the model passes to the tool.
    @Generable
    struct Arguments {
        @Guide(description: "Which room, e.g. 'living room', 'bedroom', 'all'")
        var room: String
        @Guide(description: "Brightness from 0 (off) to 100 (full)")
        var brightness: Int
    }

    // The implementation of the call.
    func call(arguments: Arguments) async throws -> String {
        "ok"
    }
}
```

In this example, the `call(arguments:)` method returns a string rather than controlling real hardware. Tool-calling evaluation measures whether the model selects the right tool with the right arguments, not what the tool does when called. Your tools don’t need to perform real actions during evaluation, so simple stubs like this one work well.

The following examples reference additional tools such as `set_thermostat` and `lock_door` that follow the same pattern. For details on building tools with [`Foundation Models`](https://developer.apple.com/documentation/foundationmodels), see [`Expanding generation with tool calling`](https://developer.apple.com/documentation/foundationmodels/expanding-generation-with-tool-calling).

#### Match a Single Tool Call

The simplest evaluation verifies that the model calls a specific tool with exact argument values. A [`TrajectoryExpectation`](trajectoryexpectation.md) describes the tool calls you expect for a given prompt, and each *argument matcher* controls how strictly the evaluator compares a value. This example uses [`ArgumentMatcher.exact(argumentName:value:)`](argumentmatcher/exact(argumentname:value:).md), which requires a precise match; later sections cover matchers for flexible comparisons.

Start by defining samples. Each sample pairs a prompt with the expected tool calls:

```swift
struct LightControlEvaluation: Evaluation {
    let dataset = ArrayLoader(samples: [
            ModelSample(
                prompt: "Turn off the living room lights.",
                expectations: TrajectoryExpectation(
                    expected: "set_lights", arguments: [
                        .exact(argumentName: "room", value: .string("living room")),
                        .exact(argumentName: "brightness", value: .int(0)),
                    ]
                )
            ),
            ModelSample(
                prompt: "Set the bedroom lights to full brightness.",
                expectations: TrajectoryExpectation(
                    expected: "set_lights", arguments: [
                        .exact(argumentName: "room", value: .string("bedroom")),
                        .exact(argumentName: "brightness", value: .int(100)),
                    ]
                )
            ),
        ])
    // Continued below in the next two code snippets...
```

Next, implement [`subject(from:)`](evaluation/subject(from:).md) to call the model with your tools. Capture the transcript from the session so the evaluator can inspect the tool calls.

```swift
    func subject(from sample: ModelSample<String>) async throws -> ModelSubject<String> {
        let session = LanguageModelSession(
            tools: [SetLights(), SetThermostat(), LockDoor()],
            instructions: "You are a smart home assistant. Use tools to fulfill requests."
        )
        let response = try await session.respond(
            to: sample.prompt,
            generating: String.self
        )
        // Capture the structured transcript from the session.
        let transcript = session.transcript.structuredTranscript
        return ModelSubject(value: response.content, transcript: transcript)
    }
    // Continued below in the next code snippet...
```

Finally, add a [`ToolCallEvaluator`](toolcallevaluator.md) to score the model’s tool calls against your expectations, and define how to aggregate the results:

```swift
    // ToolCallEvaluator writes its results to these two metrics.
    let toolsAllPass = Metric("ToolsAllPass")
    let toolsPercentagePass = Metric("ToolsPercentagePass")

    var evaluators: Evaluators {
        ToolCallEvaluator(allPass: toolsAllPass, percentagePass: toolsPercentagePass)
    }

    // Compute the mean of each metric across all samples.
    func aggregateMetrics(using aggregator: inout MetricsAggregator) {
        aggregator.computeMean(of: toolsAllPass)
        aggregator.computeMean(of: toolsPercentagePass)
    }
}
```

#### Handle Ambiguous Intents

When the user says “I’m feeling cold,” both “warm” and “comfortable” are reasonable thermostat presets. Use [`ArgumentMatcher.oneOf(argumentName:allowedValues:)`](argumentmatcher/oneof(argumentname:allowedvalues:).md) to accept any value from a set, and [`ArgumentMatcher.range(argumentName:minimum:maximum:)`](argumentmatcher/range(argumentname:minimum:maximum:).md) to accept numeric values within a range:

```swift
ModelSample(
    prompt: "I'm feeling a bit cold.",
    expectations: TrajectoryExpectation(
        // Accept either "warm" or "comfortable" as a valid response to feeling cold.
        expected: "set_thermostat", arguments: [
            .oneOf(argumentName: "preset", allowedValues: [
                .string("warm"), .string("comfortable"),
            ]),
        ]
    )
),
ModelSample(
    prompt: "Dim the living room lights a little.",
    expectations: TrajectoryExpectation(
        // Allow any brightness between 20 and 80. "A little" is subjective.
        expected: "set_lights", arguments: [
            .exact(argumentName: "room", value: .string("living room")),
            .range(argumentName: "brightness", minimum: 20, maximum: 80),
        ]
    )
),
```

[`ArgumentMatcher`](argumentmatcher.md) provides nine validation strategies. Choose one based on how precisely you need to constrain the model’s output:

#### Match Complex Tool Calls

The examples above check individual tool calls. For multi-step workflows, you can combine expectations:

- **`ordered`**: Must occur in a specific sequence.
- **`unordered`**: Must occur regardless of position.
- **`disallowed`**: Must never occur.

Some tasks require tools to be called in a specific sequence. Movie night means dimming the lights *before* turning on the TV, not the other way around. Use [`init(ordered:unordered:allowsAdditionalToolCalls:)`](trajectoryexpectation/init(ordered:unordered:allowsadditionaltoolcalls:).md) with an array of [`ToolExpectation`](toolexpectation.md) entries to enforce ordering:

```swift
ModelSample(
    prompt: "Start movie night.",
    expectations: TrajectoryExpectation(
        ordered: [
            // Dim the lights first.
            ToolExpectation("set_lights", arguments: [
                .exact(argumentName: "room", value: .string("living room")),
                .range(argumentName: "brightness", minimum: 5, maximum: 40),
            ]),
            // Then turn on the TV.
            ToolExpectation("set_tv", arguments: [
                .exact(argumentName: "power", value: .string("on")),
            ]),
        ]
    )
),
```

The evaluator scans the transcript sequentially, matching each ordered expectation after the previous one. If the model calls `set_tv` before `set_lights`, the ordered step fails.

Not all workflows require a specific sequence. “Lock up for me.” needs the lights off, the door locked, and the thermostat adjusted, but in any order. Use [`init(unordered:)`](trajectoryexpectation/init(unordered:).md) when only the occurrence of events matters, not the order in which they happen:

```swift
ModelSample(
    prompt: "I'm heading out, lock up for me.",
    expectations: TrajectoryExpectation(
        // All three tools must be called, but in any order.
        unordered: [
            ToolExpectation("set_lights", arguments: [
                .contains(argumentName: "room", substring: "all"),
                .exact(argumentName: "brightness", value: .int(0)),
            ]),
            ToolExpectation("lock_door", arguments: [
                .exact(argumentName: "door", value: .string("front")),
            ]),
            ToolExpectation("set_thermostat", arguments: [
                .exact(argumentName: "preset", value: .string("cool")),
            ]),
        ]
    )
),
```

The evaluator matches each unordered expectation against the entire transcript; position doesn’t matter, only that they happen.

Many workflows mix both. A bedtime routine requires locking the door then dimming the lights (in that order), while closing blinds and adjusting the thermostat can happen at any point:

```swift
ModelSample(
    prompt: "Run my bedtime routine.",
    instructions: """
        The bedtime routine is: lock the front door, then dim the bedroom lights. \
        Also close the bedroom blinds and set the thermostat to cool. Those can \
        happen at any point.
        """,
    expectations: TrajectoryExpectation(
        // These two must happen in this order.
        ordered: [
            ToolExpectation("lock_door", arguments: [
                .exact(argumentName: "door", value: .string("front")),
            ]),
            ToolExpectation("set_lights", arguments: [
                .exact(argumentName: "room", value: .string("bedroom")),
                .range(argumentName: "brightness", minimum: 5, maximum: 20),
            ]),
        ],
        // These can happen at any point during the sequence.
        unordered: [
            ToolExpectation("close_blinds", arguments: [
                .exact(argumentName: "room", value: .string("bedroom")),
            ]),
            ToolExpectation("set_thermostat", arguments: [
                .exact(argumentName: "preset", value: .string("cool")),
            ]),
        ]
    )
),
```

The evaluator checks ordered expectations sequentially, then verifies that every unordered expectation appears somewhere in the transcript. The model must fully satisfy both sets for the strict metric to pass.

You can also disallow specific tool calls. A query that only reads the thermostat must never change settings, even if the model has access to those tools. Use the `disallowed` parameter to define negative constraints:

```swift
ModelSample(
    prompt: "What's the current temperature?",
    expectations: TrajectoryExpectation(
        ordered: [
            ToolExpectation("get_thermostat"),
        ],
        disallowed: [
            // A read-only query must never change settings.
            ToolExpectation("set_thermostat"),
            ToolExpectation("set_lights"),
        ]
    )
),
```

If a disallowed expectation includes argument matchers, the evaluator flags only calls matching those specific arguments. The model can still call the tool with different arguments. To disallow a tool entirely regardless of arguments, omit the matchers.

When your ordered sequence has a position where the model must call multiple tools in any order, use [`anyOrder(_:)`](toolexpectation/anyorder(_:).md) to group them into a single position in the sequence.

By default, [`TrajectoryExpectation`](trajectoryexpectation.md) allows tool calls that don’t match any expectation, so the model is free to call helper tools, retry operations, or make exploratory calls. Set [`allowsAdditionalCalls`](trajectoryexpectation/allowsadditionalcalls.md) to `false` when you want any unmatched call to fail the evaluation.

This example unlocks the front door first, then requires the lights and thermostat in either order, and rejects any tool calls not listed:

```swift
ModelSample(
    prompt: "I'm home, let me in.",
    expectations: TrajectoryExpectation(
        ordered: [
            ToolExpectation("unlock_door", arguments: [
                .exact(argumentName: "door", value: .string("front")),
            ]),
            // Both must happen after the door unlocks, in either order.
            ToolExpectation.anyOrder([
                ToolExpectation("set_lights", arguments: [
                    .exact(argumentName: "room", value: .string("living room")),
                    .exact(argumentName: "brightness", value: .int(100)),
                ]),
                ToolExpectation("set_thermostat", arguments: [
                    .exact(argumentName: "preset", value: .string("warm")),
                ]),
            ]),
        ],
        allowsAdditionalToolCalls: false
    )
),
```

#### Interpret Evaluation Results

[`ToolCallEvaluator`](toolcallevaluator.md) writes two metrics per sample, using the [`Metric`](metric.md) instances you declare on your evaluation. For guidance on using evaluation results to iterate and improve your feature over time, see [`Designing effective evaluations`](designing-effective-evaluations.md).

- **ToolsAllPass**: A strict pass/fail metric. Passes only when the model’s tool calls satisfy every expectation: no missed tools, no wrong arguments, no disallowed calls, and no unexpected calls (when [`allowsAdditionalCalls`](trajectoryexpectation/allowsadditionalcalls.md) is false).
- **ToolsPercentagePass**: A proportional score reporting `matchedExpectations / totalExpectations` as a number between 0 and 1. This gives you an improvement signal even when the strict metric fails.

Use `ToolsAllPass` to track whether the model meets your threshold. Use `ToolsPercentagePass` to measure progress toward that threshold during prompt iteration.

The detailed results show both metrics for each sample. In this figure, the request to lock up the house expects three tools but matches only one, so `ToolsAllPass` fails while `ToolsPercentagePass` reports 0.33. The request that calls every expected tool passes both:

![A screenshot of the detailed tool-calling results in the Xcode Test Report. A table lists each prompt with its ToolsAllPass pass or fail mark and its ToolsPercentagePass score. The first prompt, to lock up the house, fails ToolsAllPass and scores 0.33, and the second prompt, to prepare the house for guests, passes ToolsAllPass and scores 1.](/images/com.apple.evaluations/eval-tool-call-results@2x.png)

Organize tool-call metrics alongside other evaluators using [`group(_:_:)`](metricsaggregator/group(_:_:).md):

```swift
func aggregateMetrics(using aggregator: inout MetricsAggregator) {
    // Group related metrics so the output stays organized.
    aggregator.group("Tool Calling") { group in
        group.computeMean(of: toolsAllPass)
        group.computeMean(of: toolsPercentagePass)
    }
    aggregator.group("Output Quality") { group in
        group.computeMean(of: exactMatch)
    }
}
```

> **Note**: When [`allowsAdditionalCalls`](trajectoryexpectation/allowsadditionalcalls.md) is set to `false`, unexpected calls count against `ToolsPercentagePass` by inflating the denominator. For example, a sample with 2 expected calls and 1 unexpected call reports a score of 0.67 instead of 1.0.

#### Combine Tool Calling Evaluation with Content Evaluation

Accurate tool calling and response quality both matter. A model that calls the right tools but returns an inaccurate or incomplete response still fails the user. Add [`ToolCallEvaluator`](toolcallevaluator.md) alongside other evaluators to measure both dimensions:

```swift
var evaluators: Evaluators {
    // Score tool calls against the trajectory expectations defined on each sample.
    ToolCallEvaluator(allPass: toolsAllPass, percentagePass: toolsPercentagePass)
    // Also check whether the final output matches the expected answer.
    Evaluator { input, subject in
        guard let expected = input.expected else { return exactMatch.ignore() }
        return subject.value == expected ? exactMatch.passing() : exactMatch.failing()
    }
}
```

This pattern lets you verify that the model both uses the right tools and produces the right answer. For subjective quality criteria like tone or helpfulness, see [`Scoring with model-judge evaluators`](scoring-with-model-as-judge-evaluators.md).

#### Run Your Evaluation

Run your tool-calling evaluation with Swift Testing by attaching the [`EvaluationTrait`](evaluationtrait.md) to a test function:

```swift
import Testing
import Evaluations

struct LightControlTests {
    @Test(.evaluates(LightControlEvaluation()))
    func lightControl() async throws {
        let result = EvaluationContext.current.result
        let evaluation = LightControlEvaluation()
        let strict = result.aggregateValue(.mean(of: evaluation.toolsAllPass))
        #expect(strict > 0.9)
    }
}
```

## See Also

- [struct ToolCallEvaluator](toolcallevaluator.md)
  An evaluator that verifies agentic tool calls against an expected trajectory.
- [struct TrajectoryExpectation](trajectoryexpectation.md)
  The expected pattern of tool calls for an evaluation.
- [enum ArgumentMatcher](argumentmatcher.md)
  The values that define how to validate a tool-call argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/evaluating-tool-calling-behavior)*