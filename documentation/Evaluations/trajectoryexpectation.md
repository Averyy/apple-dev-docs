# TrajectoryExpectation

**Framework**: Evaluations  
**Kind**: struct  
**Role**: Structure

The expected pattern of tool calls for an evaluation.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
struct TrajectoryExpectation
```

## Mentions

- [Evaluating tool-calling behavior](./evaluating-tool-calling-behavior.md)
- [Evaluating language model responses](./evaluating-language-model-responses.md)

## Overview

```swift
TrajectoryExpectation(ordered: [
    ToolExpectation("authenticate"),
    ToolExpectation("processResults"),
])
```

`TrajectoryExpectation` specifies expected tool-calling behavior across three axes:

- **Ordered**: Tool calls that must occur in a specific sequence. Use [`ToolExpectation`](./toolexpectation.md) for single sequential steps, or [`anyOrder(_:)`](./toolexpectation/anyorder%28_%29.md) when multiple tools must all be called at a given position but their relative order doesn’t matter.
- **Unordered**: Tool calls that must occur at some point, regardless of when.
- **Disallowed**: Tool calls that must NOT occur.

```swift
TrajectoryExpectation(ordered: [
    ToolExpectation("authenticate"),
    ToolExpectation("processResults"),
])
```

```swift
TrajectoryExpectation(ordered: [
    ToolExpectation("authenticate"),
    .anyOrder([
        ToolExpectation("fetchData"),
        ToolExpectation("fetchMetadata"),
    ]),
    ToolExpectation("processResults"),
], allowsAdditionalToolCalls: false)
```

```swift
TrajectoryExpectation(
    ordered: [
        ToolExpectation("findActivities"),
        ToolExpectation("estimateTravelTime"),
    ],
    unordered: [ToolExpectation("getWeather")],
    disallowed: [ToolExpectation("deleteData")]
)
```

```swift
TrajectoryExpectation(expected: "getWeather", arguments: [
    .exact(argumentName: "location", value: "Paris, France")
])
```

## Topics

### Creating a single-tool expectation
- [init(expected: String, arguments: [ArgumentMatcher])](./trajectoryexpectation/init%28expected,arguments%29.md)
  Creates a trajectory expectation for a single expected tool call.
- [struct ToolExpectation](./toolexpectation.md)
  A specification for an expected tool call, or a group of expectations that can be satisfied in any order.
### Creating multi-tool expectations
- [init(ordered: [ToolExpectation], unordered: [ToolExpectation], allowsAdditionalToolCalls: Bool)](./trajectoryexpectation/init%28ordered,unordered,allowsadditionaltoolcalls%29.md)
  Creates a trajectory expectation with ordered and unordered requirements, and controls whether unmatched tool calls are permitted.
- [init(ordered: [ToolExpectation], unordered: [ToolExpectation], disallowed: [ToolExpectation])](./trajectoryexpectation/init%28ordered,unordered,disallowed%29.md)
  Creates a trajectory expectation with ordered and unordered requirements, plus specific tools that the model must not call.
- [init(unordered: [ToolExpectation])](./trajectoryexpectation/init%28unordered%29.md)
  Creates a trajectory expectation with only unordered requirements.
### Combining expectations
- [var ordered: [ToolExpectation]](./trajectoryexpectation/ordered.md)
  Tool call steps that must be satisfied in sequential order.
- [var unordered: [ToolExpectation]](./trajectoryexpectation/unordered.md)
  Tool calls that must occur at some point, regardless of position.
- [var disallowed: [ToolExpectation]](./trajectoryexpectation/disallowed.md)
  Tools that the model must NOT call.
- [var allowsAdditionalCalls: Bool](./trajectoryexpectation/allowsadditionalcalls.md)
  A Boolean value that indicates whether to allow tool calls that don’t match any expectation.
### Instance Properties
- [var generatedContent: GeneratedContent](./trajectoryexpectation/generatedcontent.md)
  The generated content representation of this trajectory expectation.
### Type Properties
- [static var generationSchema: GenerationSchema](./trajectoryexpectation/generationschema.md)
  The generation schema for this trajectory expectation.
### Default Implementations
- [ConvertibleFromGeneratedContent Implementations](./trajectoryexpectation/convertiblefromgeneratedcontent-implementations.md)

## Relationships

### Conforms To
- [ConvertibleFromGeneratedContent](../FoundationModels/convertiblefromgeneratedcontent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/convertibletogeneratedcontent.md)
- [Copyable](../Swift/copyable.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Escapable](../Swift/escapable.md)
- [Generable](../FoundationModels/generable.md)
- [InstructionsRepresentable](../FoundationModels/instructionsrepresentable.md)
- [PromptRepresentable](../FoundationModels/promptrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tool-call evaluation
- [Evaluating tool-calling behavior](./evaluating-tool-calling-behavior.md)
  Analyze your model’s tool calls against expected trajectories, argument values, and call ordering.
- [struct ToolCallEvaluator](./toolcallevaluator.md)
  An evaluator that verifies agentic tool calls against an expected trajectory.
- [enum ArgumentMatcher](./argumentmatcher.md)
  The values that define how to validate a tool-call argument.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/trajectoryexpectation)*