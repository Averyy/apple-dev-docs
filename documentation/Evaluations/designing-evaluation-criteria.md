# Designing specific, measurable criteria in an evaluation suite

**Framework**: Evaluations

Define quality for your feature by choosing measurable criteria, scoring approaches, and ground-truth strategies.

#### Overview

Deciding what to measure in your evaluations means defining success for your feature: *criteria* specify your measurable standards of quality. [`Designing effective evaluations`](designing-effective-evaluations.md) explains why evaluation matters and how its life cycle works; once you understand this evaluation process, your next step is defining your criteria. Well-defined criteria help you build strong evaluations. Vague criteria produce vague signals, but precise criteria tell you specifically where your feature succeeds and where it fails.

This article details the strategic decisions behind evaluation design: defining measurable targets, identifying quality dimensions, choosing between scoring approaches, and selecting the right *ground-truth*, or verified accurate results. Most features combine several criteria into an *evaluation suite*, mixing rule-based checks, scored quality dimensions, and model-judge assessments to cover what a single approach can’t.

#### Define Success As Measurable Targets

Before writing any evaluation code, identify what success looks like for your feature. Every quality goal needs to become a specific, measurable target that code can verify.

Consider what your feature needs to accomplish and what might go wrong. Each goal becomes an individual criterion with a clear measurement:

| Goal | Criterion | Measurement |
| --- | --- | --- |
| Responses respect constraints. | Output stays within stated limits. | Pass or fail per constraint |
| Output is factually grounded. | Claims are supported by provided context. | Score 1–4 on factual scale |
| Feature handles diverse inputs. | Quality is consistent across input categories. | Standard deviation of category mean scores |
| Includes no harmful content. | Output avoids unsafe or inappropriate material. | Pass if no safety violations detected |

Start with the criteria that matter most to your users. You can always add more dimensions later as you begin to understand the points of failure in your feature.

#### Identify Quality Dimensions

A single feature typically needs to satisfy several independent quality dimensions. Consider each of these, with at least one criterion per dimension that matters to your feature:

- **Task fidelity**: The response correctly accomplishes what it’s supposed to. For example, a summarizer captures the key points or a planner stays within budget.
- **Consistency**: The model produces similar quality across varied inputs. For example, a summarizer produces equally useful output for a two-sentence memo and a ten-page report.
- **Tone and style**: The output matches your app’s voice. For example, a professional email is actually professional or instructions are at the right level for the audience.
- **Safety**: The model avoids harmful or inappropriate content. For example, it refuses adversarial prompts gracefully.
- **Privacy preservation**: The model avoids revealing private data or information outside its intended scope. For example, a customer-support assistant answers questions about the current user’s orders without surfacing details from other customers.
- **Latency and cost**: The model responds within acceptable time and token budgets for your use case. For example, responses to queries don’t take too long or require too many tokens, slowing down your feature.

Not every dimension applies to every feature. Choose the dimensions that represent real risk or real value for people using your feature, and assign at least one evaluator to each.

> 💡 **Tip**: Start with two or three evaluators that cover your most important quality dimensions. Add more as you learn where your feature tends to fail.

#### Choose the Right Scoring Approach

Evaluations give you two main evaluation mechanisms: code-based evaluators and model-judge. The right approach depends on how you define correctness for each criterion. Start with the simplest approach that gives reliable signals, and move to more sophisticated methods only when needed:

| Approach | Use when | Speed | Cost | Reproducibility |
| --- | --- | --- | --- | --- |
| Code-based ([`Evaluator`](evaluator.md)) | Correctness has a computable definition, for example, exact match, schema validation, or range check. | Instant | Free | Perfect |
| Model judge ([`ModelJudgeEvaluator`](modeljudgeevaluator.md)) | Quality is subjective or requires reasoning, for example, helpfulness, tone, or accuracy of classification. | Seconds | Inference cost | High with well-defined scoring levels |
| Human review | High stakes, calibrating model-judge evaluators, or discovering gaps in your scoring dimensions. | Minutes or more | Expensive | Variable |

**Use code when you can.** If the criterion is computable, a code-based evaluator is faster, cheaper, and perfectly reproducible. Checking whether a response stays within a word limit is a code check. Validating that structured output conforms to a schema is a code check. Verifying that a numeric answer falls within an expected range is a code check. These never need a model judge. For example, verifying a word limit takes just a few lines with [`Evaluator`](evaluator.md):

```swift
Evaluator { input, subject in
    subject.value.split(separator: " ").count <= 200
        ? wordLimit.passing() : wordLimit.failing()
}
```

**Use a model judge when code can’t capture the criterion.** Determining whether an explanation is clear, whether a tone is appropriate, or whether a summary captures the important points requires reasoning about language and context. This is where [`ModelJudgeEvaluator`](modeljudgeevaluator.md) provides value. The quality of a model-judge evaluation depends on your scoring levels: make each level specific enough that two independent reviewers are likely to assign the same score.

**Use humans to calibrate, not to score at scale.** Human review is too slow and expensive for routine evaluation. Its value is in calibrating your automated evaluators: run a small set of human-scored samples, compare them against your model-judge scores, and refine your scoring levels where they disagree.

For implementation details, see [`Evaluating language model responses`](evaluating-language-model-responses.md) for a complete walkthrough, and [`Scoring with model-judge evaluators`](scoring-with-model-as-judge-evaluators.md) for model-judge configurations.

For best practices on configuring model-judge evaluators, including scoring scales, bias mitigation, and calibration, see [`Designing effective model-judge evaluators`](designing-effective-model-judges.md).

#### Choose the Right Ground Truth Strategy

Different scoring strategies relate to ground truth in different ways. Understanding this distinction helps you choose the right approach for each criterion:

- **Explicit ground truth**: You have a predefined correct answer for each input, and you compare the model’s output against it. A math problem has one right answer. A classification task has a known label. The evaluator measures how closely the model’s output matches the expected result.
- **Rule-based (implicit ground truth)**: The rule itself is the truth. A word count check doesn’t need a golden answer for each sample because the rule “200 words or fewer” applies universally. Format checks, schema validation, and constraint verification all fall into this category.
- **No ground truth**: For open-ended output where multiple answers are equally valid, you use a model judge or pre-trained classifier to assess quality. Whether an explanation is clear or a recommendation is useful has no single right answer, but a model judge can reason about quality criteria you define.

Most evaluation suites combine all three approaches. A feature might check format compliance (rule-based), compare answers against known-correct values for a core set (explicit ground truth), and use a model judge for subjective quality on everything else (no ground truth).

> 💡 **Tip**: Use a model that is more capable than the model being evaluated as the judge. This reduces the chance of the judge sharing the same gaps as the model under test.

## See Also

- [struct Metric](metric.md)
  A named metric that carries a result value.
- [struct Evaluator](evaluator.md)
  A closure-based evaluator.
- [struct MetricsAggregator](metricsaggregator.md)
  A utility for computing aggregate statistics from evaluation metrics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/designing-evaluation-criteria)*