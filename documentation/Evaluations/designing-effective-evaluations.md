# Designing effective evaluations

**Framework**: Evaluations

Design evaluations that tell you how well your feature works, why it fails, and where to focus next.

#### Overview

When you build an intelligence-powered feature, an early milestone is getting it working for a handful of cases. The harder work comes next: making sure your feature handles the full range of inputs it meets in production, and that fixes for one problem don’t silently break cases that already work.

Evaluation gives you that signal. This article covers the practices that turn ad-hoc tests into evaluations you can rely on: how to define measurable criteria, structure your dataset, interpret results, and iterate without overfitting. For the API walkthrough of running an evaluation, see [`Evaluating language model responses`](evaluating-language-model-responses.md).

#### Adapt Your Testing Approach for Model Responses

Testing an intelligence-powered feature includes some unique complexities that impact how you design a robust evaluation approach:

- **Probabilistic outputs**: The same input can produce different responses across runs due to sampling and model updates.
- **Fuzzy correctness**: Success often depends on nuanced criteria like “helpful tone” or “appropriate for beginners” that a string match can’t verify.
- **External model changes**: The underlying model can change without any code changes on your end, shifting behavior between releases.
- **Context sensitivity**: Small differences in prompt wording or input formatting can cause large swings in output quality.
- **High stakes**: Model outputs directly affect user trust. A single wrong answer can erode confidence in your entire application.

Traditional unit tests verify deterministic behavior in code: if a test passes today, it passes tomorrow unless you change the code. Intelligence-powered features break this assumption. Build a robust evaluation practice, so you can maintain consistent quality at scale.

#### Treat Evaluations As Your Living Specification

A traditional specification document becomes outdated the moment you start building. A comprehensive set of evaluations stays useful because it is:

- **Executable**: It programmatically defines what “correct” looks like.
- **Precise**: It replaces vague goals with measurable targets.
- **Always current**: It runs against every change, providing an up-to-the-minute view of feature quality.

In Evaluations, the [`Evaluation`](evaluation.md) protocol captures these three attributes directly: it bundles the feature under test, the test dataset, the evaluators, and the result aggregation into a single, runnable definition.

Thinking of your evaluation as your specification forces you to define, from the beginning, exactly what your feature must do, what it must not do, and how you measure the difference.

##### Create Precise Measurable Criteria

Evaluation transforms a subjective “is this good?” into a precise, measurable signal that you can track over time. What “looks good” to you isn’t a scalable quality signal; you might approve an output that seems reasonable without noticing a subtle error that a user with more context might catch immediately.

Turn vague goals into concrete, measurable targets:

| Vague goal | Precise criterion |
| --- | --- |
| “Stay within budget.” | 100% compliance with stated budget ceiling (pass/fail) |
| “Be helpful.” | Greater than 90% task success rate on common query benchmark |
| “Match the user’s skill level.” | Complexity score (1–4) within 0.5 of stated preference |
| “Generate accurate tags.” | 95% of tags classify as factual descriptors, not subjective reactions |

The pattern is the same regardless of your feature: replace vague, subjective impressions with criteria that code or model-as-judge evaluators can verify. For guidance on defining measurable criteria, see [`Designing specific, measurable criteria in an evaluation suite`](designing-evaluation-criteria.md).

#### Adopt an Evaluation Driven Development Life Cycle

Successful intelligence-powered features are built in a tight feedback loop where evaluation drives every step. It’s not the last step before shipping; it’s part of every step from the beginning.

1. **Plan.** Define your feature and its success metrics. Describe what “correct” looks like and the quality dimensions that matter.
2. **Develop.** Write the prompts, choose a model, and build the feature.
3. **Evaluate.** Run the feature against a test dataset and score the outputs with your defined metrics.
4. **Analyze.** Find where the feature fails and why. Determine, for example, whether failures are concentrated in a specific category of input or type of request.
5. **Improve.** Refine prompts, adjust model settings, or add test cases, then repeat steps 3-5.

Each pass through this loop produces measurable feedback, so you iterate with confidence instead of guessing. Before you start building, you need to know what success looks like.

Small changes show up as score shifts, so you can iterate toward a better feature without introducing regressions.

#### Avoid the Cost of Skipping Evaluation

Skipping systematic evaluation can quietly undermine your product in ways that don’t become obvious until it’s too late:

- **Silent regressions**: A prompt tweak that fixes one edge case might silently break several others. Without evaluation, you won’t know until people using your feature complain.
- **False confidence**: Passing a handful of manual checks can mask issues that surface under real-world usage. Five good results don’t tell you about the five hundred that fail.
- **Inability to measure progress**: Without quantified scores, you cannot tell whether a change is a genuine improvement or simply a different set of tradeoffs. You lose the ability to compare approaches objectively.
- **Erosion of user trust**: Inconsistent or incorrect outputs erode trust over time, sometimes from a single bad experience.
- **Compounding drift**: Each unverified change compounds. Over weeks of development, your feature can drift far from its original quality level without any single change appearing to be the cause.

A quantified score for your feature’s performance means you can make objective decisions, track quality over time, compare different prompts or models, and set a clear threshold for what “good enough to ship” means.

#### Understand the Components of an Evaluation

As described in [`Evaluating language model responses`](evaluating-language-model-responses.md), to create an evaluation, you:

- Provide input as a dataset of samples with expected outputs.
- Define the subject: the intelligence-powered feature you are testing.
- Add evaluators that score each response against metrics you define.
- Aggregate those scores into a metric summary you compare across runs.

Your dataset determines what your evaluation can tell you. A well-designed dataset includes golden samples that represent core functionality, edge cases that probe boundaries, and adversarial inputs that test failure modes. If an input category isn’t represented, your evaluation is silent about it. For guidance on structuring datasets, see [`Designing datasets to test your feature`](designing-evaluation-datasets.md). For scaling datasets with synthetic generation, see [`Generating synthetic datasets`](generating-synthetic-evaluation-datasets.md).

Evaluations supports two kinds of evaluators:

- Code-based evaluators verify criteria with computable definitions: format compliance, word limits, schema validation, exact matches. They are instant, free, and perfectly reproducible.
- Model-as-judge evaluators score subjective qualities that code can’t capture: tone, clarity, helpfulness, accuracy of open-ended responses. A language model reads the output and scores it against scoring levels you define. For best practices on configuring model-as-judge evaluators, see [`Designing effective model-as-judge evaluators`](designing-effective-model-judges.md).

#### Analyze Your Results for Patterns

Running an evaluation gives you measurable data on how your feature is performing. Follow these best practices as you interpret the results, form hypotheses about failures, make targeted changes, and verify the improvements across your dataset.

An evaluation produces an [`EvaluationResult`](evaluationresult.md) with two primary views of your data: [`summary`](evaluationresult/summary.md) with aggregate statistics and [`detailed`](evaluationresult/detailed.md) with per-sample scores. Both matter, and they tell you different things.

- **Summary**: Shows overall health. A 95-percent pass rate sounds strong. A mean score of 4.2 out of 5 suggests the feature is working well. These numbers track progress across runs and let you compare approaches.
- **Detailed view**: Reveals patterns. That 95-percent pass rate might hide the fact that every failure comes from one category of input. The 5 percent that fail could represent an entire use case. Always inspect individual failures to understand their structure.

When reviewing results, look for:

- **Clusters of failure**: Determine whether failures are concentrated in a specific input type or category of request. Concentrated failure points to a systematic issue rather than random noise.
- **Near-misses**: Samples that scored 3 out of 5 are as informative as outright failures. They show you where the feature is fragile and likely to regress with further changes.
- **Unexpected passes**: If a sample you expected to fail actually passes, your mental model of the feature’s behavior is incomplete. Investigate why the sample passed, then update the expected value or document the pass so future runs catch any regression.

Organize your results into the categories you defined in your dataset (golden set, edge cases, adversarial, known failures) to see which areas are strong and which need attention. For more information about organizing your data into categories, see [`Designing datasets to test your feature`](designing-evaluation-datasets.md).

Different metric types call for different summary statistics: use the mean of pass or fail metrics to get a pass rate directly, and the median of scored metrics to resist outlier skew. [`MetricsAggregator`](metricsaggregator.md) supports both approaches:

```swift
aggregator.computeMean(of: safetyCheck)   // Pass rate for binary metrics.
aggregator.computeMedian(of: qualityScore) // Central tendency for scored metrics.
```

> ❗ **Important**: Always verify that your metric is measuring what you think it is. A perfect score can be misleading: a bias evaluation that returns zero bias might mean your model is unbiased, or it might mean your model isn’t answering the questions at all. When scores seem too good, inspect the underlying outputs to confirm the metric captures genuine quality, not an artifact of unexpected behavior.

#### Iterate Through an Improvement Cycle

The Improve step in the life cycle has its own loop. When you identify a failure pattern, follow this cycle to fix it without introducing new problems:

1. **Hypothesize.** Form a specific theory about why the failure occurs. Don’t just observe “the output is wrong.” Ask why. The model might misunderstand the constraint or be missing context. It might be overemphasizing one part of the input and ignoring another.
2. **Modify.** Make a targeted change based on your hypothesis. This might be a prompt revision, an adjustment to the system instructions, a change in how context is provided, or a different model configuration. Keep the change focused on your hypothesis so you can attribute any improvement (or regression) to a specific cause.

For example, if a feature produces outputs that violate a stated constraint, you might revise the system instructions:

*Before:* “You are a helpful assistant. Follow the user’s preferences.”

*After:* “You are a helpful assistant. Strictly adhere to all stated constraints. When the user specifies limits, treat them as hard requirements rather than suggestions.”

1. **Re-run.** Run the entire evaluation suite, not just the failing samples. A targeted prompt change can fix one category while introducing regressions elsewhere. Stronger constraint language might fix boundary violations but make the model too rigid for open-ended requests.
2. **Compare.** Check whether the previously failing samples now pass and whether all other samples maintained their scores. If the fix caused a new failure, you have a new hypothesis to investigate.

Each iteration of this cycle either raises your score or teaches you something new about your feature’s failure modes.

#### Avoid Overfitting As You Iterate

As you iterate through the improvement cycle, there is a risk of *overfitting*: tuning your prompts so precisely to your test cases that improvements stop generalizing to real-world inputs. A prompt engineered to pass 50 specific test cases might fail on the 51st because it’s optimized for your dataset’s quirks rather than the underlying quality criteria.

Guard against this with a *holdout* set: a portion of your dataset that you never use during prompt development. Run your evaluation against the holdout set periodically, not after every change but at milestones, to verify that your gains are real. If your development set scores keep climbing but your holdout set scores plateau or decline, you’re overfitting.

Here are some additional safeguards:

- **Vary your inputs.** If all your test cases share similar characteristics, for example, similar length, complexity, and phrasing, your prompt might work perfectly for that profile but fail on inputs that differ. Include variation in your dataset from the start.
- **Watch for brittle fixes.** If a change requires very specific wording to work, it may be fragile. Prefer changes that teach the model a principle over changes that enumerate specific prohibitions.
- **Test with new data periodically.** As real users interact with your feature, add fresh samples that you never tuned your prompt against. These are your best signal for generalization.

To see these practices in use in a complete app, where a model as judge is calibrated against expert scores so you can trust it while iterating on a prompt, see [`Book Tracker: Using Evaluations to evaluate an intelligent feature`](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md).

#### Capture Result Failures to Prevent Regressions

When you discover an input that your model handles poorly, add it to your dataset with the expected behavior documented. Over time, your dataset becomes a regression suite that prevents previously fixed issues from reappearing. For more information about structuring your dataset, see [`Designing datasets to test your feature`](designing-evaluation-datasets.md).

Here’s a straightforward workflow:

1. A failure surfaces (through user feedback, manual review, or monitoring).
2. You reproduce the failure as a test case with the input and the expected behavior.
3. You add it to your “known failures” dataset category.
4. You fix the issue (prompt change, model setting, or feature logic).
5. The test case remains permanently, catching any future change that might reintroduce the problem.

This creates an incrementing effect: your quality level can only go up. Each failure you capture and fix becomes a permanent guard against regression.

#### Grow Your Evaluation Suite Over Time

Start with small evaluations and build them into a comprehensive evaluation suite over time. Here’s what that might look like:

- **Week one.** Define 2-3 evaluators covering your most critical quality dimensions. Build a golden set of 10-20 samples that represent core functionality. This gives you a baseline to iterate against.
- **First month.** Add challenge sets as you discover failure modes. Introduce a model-as-judge for subjective dimensions that code can’t capture. Your dataset grows to 30-50 samples across categories.
- **Ongoing.** Incorporate people’s interactions with your feature, with their permission. Use [`SampleGenerator`](samplegenerator.md) to test statistical consistency at volume. Add new quality dimensions as your understanding deepens. Periodically review whether existing evaluators still measure what matters.

As your feature evolves, your evaluation evolves with it. Remove evaluators that no longer provide useful signals. Split evaluators that are measuring too many things at once. Add evaluators when you discover new failure modes.

#### Integrate Evaluations Into Your Workflow

Evaluations provide the most value when you run them consistently and treat the results as actionable. Run evaluations on:

- **Every prompt change.** Even small wording adjustments can cause unexpected shifts in model behavior. Run your full suite after every modification.
- **Model updates.** When the underlying model changes (through an OS update or API version bump), re-evaluate. Model changes can shift behavior without any code changes on your end.
- **Tool modifications.** If your feature uses tools, changes to tool definitions or available tools can affect how the model reasons about its task.

Track metadata across runs. Label each evaluation run with the model name, dataset version, and prompt version so you can correlate changes in scores with specific modifications.

Reuse evaluation criteria beyond testing. The assertions you write for evaluation can also serve as runtime guardrails. A format check that catches invalid output in your test suite can reject invalid output in production. A content filter in your evaluation can run as a safety check on live responses. Building your evaluation criteria with reuse in mind creates a shared quality language between testing and production.

Treat evaluation runs like continuous integration checks. They catch regressions early, before changes reach production, and they give you confidence that improvements are real rather than illusory.

## See Also

- [Evaluating language model responses](evaluating-language-model-responses.md)
  Build an evaluation that runs your intelligence-powered feature against samples and scores each response.
- [Book Tracker: Using Evaluations to evaluate an intelligent feature](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md)
  Measure and improve the quality of your app’s intelligence-powered features using the Evaluations framework.
- [protocol Evaluation](evaluation.md)
  A type that defines an evaluation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/designing-effective-evaluations)*