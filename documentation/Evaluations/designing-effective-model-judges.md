# Designing effective model-judge evaluators

**Framework**: Evaluations

Configure model-judge evaluators that produce scores you correlate with human review.

#### Overview

When code can’t capture a quality criterion, for example whether an explanation is clear or a tone is appropriate, a [`ModelJudgeEvaluator`](modeljudgeevaluator.md) lets you use a language model to score the output of another model. How well the resulting scores reflect real quality depends on how you configure the evaluator: the scoring levels, the criteria, and the evaluation steps. Careful configuration produces scores that correlate closely with human judgment; rushed or vague configuration produces scores that look precise but measure the wrong things.

This article covers the strategic decisions behind model-judge configuration: choosing the scoring scale, writing observable scoring levels, defining independent criteria, using evaluation steps, accounting for systematic biases, calibrating with human judgment, debugging through rationales, and reference-guided judging. For guidance on when to use a model as judge or a code-based evaluator, see [`Designing specific, measurable criteria in an evaluation suite`](designing-evaluation-criteria.md). For implementation details, see [`Scoring with model-judge evaluators`](scoring-with-model-as-judge-evaluators.md).

#### Choose the Right Scoring Scale

The scale you choose determines both the granularity of your *signal*, the pattern or results, and the reliability of your scores. Finer scales provide more detail but are harder for the model judge to use consistently:

| Scale | Best for | Reliability |
| --- | --- | --- |
| Binary, for example pass or fail | Safety, compliance, format checks, factual correctness | Highest |
| 1–4, or another even-numbered range | General quality, subjective dimensions like tone, clarity, helpfulness | Good |
| Custom categories | Domain-specific distinctions, for example, safe, borderline, or unsafe | Varies by design |

**Start with binary scales for binary judgments.** If a dimension is truly pass or fail, for example, safe or unsafe, on-topic or off-topic, constraint met or violated, use a binary scale. Forcing a multi-point judgment on a binary dimension adds noise without adding signal, because the judge clusters around the middle.

**Use a small, even number of levels for subjective quality.** Fewer levels balance granularity with reliability, and an even number removes the noncommittal middle the model judge can otherwise default to. A 1–4 scale gives the judge four distinguishable options and forces it to commit to either side of the midpoint. Wider scales suffer from score compression: the model judge clusters scores in a narrow range regardless of actual quality differences.

> 💡 **Tip**: Prefer an even number of levels. With no middle value, the model judge cannot fall back on a noncommittal “average” score, and each response gets a verdict on which side of the midpoint it sits. See *Leniency bias* below for more on score compression.

In Evaluations, [`ScoringScale`](scoringscale.md) provides factory methods that match these recommendations: use `.passFail()` for binary judgments and `.numeric()` for scored scales where each level maps to a description of observable features.

```swift
// A binary scale for a safety check.
let safetyScale = ScoringScale.passFail(
    passDescription: "Output is safe and on-topic.",
    failDescription: "Output contains unsafe content or goes off-topic."
)

// A four-point scale for haiku quality.
let haikuScale = ScoringScale.numeric([
    4: "Perfect 5-7-5 form, strongly relevant to the topic, uses vivid imagery.",
    3: "Correct or near-correct form, clearly relevant, some evocative language.",
    2: "Incorrect syllable count, weak topic connection, or lacks poetic quality.",
    1: "Not recognizable as a haiku, off-topic, or incoherent.",
])
```

#### Write Scoring Levels That Describe Observable Features

A common weakness in model-judge evaluators is creating scoring levels that differ only in degree, for example, “good” versus “very good”, rather than in observable characteristics. The model judge cannot reliably distinguish between “excellent quality” and “good quality.” It can, however, distinguish between “all key points addressed with supporting evidence” and “most key points addressed but missing supporting detail.”

Each of your scoring levels needs to describe what a response at that level looks like, not how good it is:

- **Describe features, not feelings.** “Perfect AABBA rhyme, strong meter, and a surprising punchline” is actionable. “Excellent limerick” is not.
- **Make adjacent levels distinguishable.** The difference between a 3 and a 4 needs to be specific enough that two independent reviewers would agree. If two levels blur together, either merge them or sharpen the descriptions.
- **Anchor every level equally.** Invest as much effort describing the middle of the scale as the extremes. Vague middle levels cause the judge to default to them.
- **Describe boundary cases.** Explain what pushes a response from one level to the next: “A response with correct structure but rough execution is a 3, not a 4.”

#### Define Independent Criteria

Each criterion you ask the model judge to evaluate needs to measure one distinct aspect of quality. Bundling multiple dimensions into a single criterion, for example, “the response is accurate, well-written, and helpful”, makes it impossible for the model judge to score a response that excels on one dimension but fails on another.

To check independence, consider whether a response can score high on criterion A but low on criterion B. If not, they likely overlap and you need to merge or sharpen them. In Evaluations, [`ScoreDimension`](scoredimension.md) captures this principle: each dimension has its own name, description, and [`ScoringScale`](scoringscale.md), keeping criteria separate.

Keep the set of criteria manageable. Typically, scoring three or four dimensions in a single model-judge call maintains quality comparable to single-dimension calls. Beyond four or five dimensions, attention decay causes the judge to give less consideration to later criteria. Group related dimensions together, but keep independent concerns, for example, safety versus quality, in separate evaluator calls.

#### Use Evaluation Steps to Improve Scoring

Asking the model judge to reason through each criterion step by step before it assigns a score is a key improvement you can make to your scoring accuracy. *Chain-of-thought* evaluation, where the model explains its reasoning as it scores, improves correlation with human judgment because it forces the model as judge to engage with the content of the response rather than defaulting to shallow heuristics.

Structure your evaluation steps to mirror how an expert annotator typically approaches evaluating the same content:

1. Examine each criterion independently, with specific guidance on what to look for.
2. End with a synthesis step that weighs all criteria together before assigning a score.

In Evaluations, include these steps in the [`instructions`](modeljudgeprompt/instructions.md) you provide to [`ModelJudgeEvaluator`](modeljudgeevaluator.md).

Without evaluation steps, the model judge can form an immediate assessment based on surface features like length or formatting, then assign a score that matches that first impression.

#### Account for Model Judge Biases

A model judge can have systematic biases that you need to account for in your evaluation design. Awareness of these biases helps you interpret results accurately and design mitigations where needed.

- **Verbosity bias**: Model judges tend to rate longer responses higher, even when the additional length adds no value. A response padded with plausible-sounding but redundant content can score higher than a concise, correct one. Mitigate this by including conciseness as an explicit criterion, or by adding instructions that longer responses don’t automatically receive higher scores.
- **Leniency bias (score compression)**: Without calibration, model judges avoid extreme scores and cluster in the middle of the scale. On an odd-numbered scale like 1–5, the middle value becomes a safe default that masks meaningful differences in quality, with most scores falling at 3 or 4. Use an even number of levels so the judge has to commit to either side of the midpoint, then mitigate further by writing detailed descriptions at every scoring level (especially the extremes), including a few-shot examples that demonstrate low scores are expected and appropriate, and using structured generation to constrain the model judge to defined scale values.
- **Self-enhancement bias**: Models tend to rate outputs from their own model family more favorably than outputs from other models. When possible, use a different model as the judge than the model being evaluated. Use a more capable model as the judge, because stronger models show less style-based bias and evaluate more on substance.
- **Position bias (pairwise only)**: In pairwise comparisons, the model judge may prefer whichever response it reads first, regardless of actual quality. If you use pairwise evaluation for A/B testing, run comparisons in both orderings and only trust verdicts where both orderings agree.

#### Calibrate with Human Judgment

How you configure your model judge affects the validity of its scores. The most effective way to validate your configuration is to compare the model-judge’s scores against human scores on a shared calibration set:

1. Have two or three human annotators score 20–50 responses using your scoring criteria and levels.
2. Run the model judge on the same set and compare.
3. Refine your criteria, scoring levels, or instructions where the model as judge systematically disagrees with humans; add evaluation steps, or add *few-shot* examples, a small number of worked examples that demonstrate the desired scoring, to the model-judge’s instructions.
4. Measure agreement with a metric like Cohen’s Kappa or another inter-rater reliability measure, rather than raw agreement rate, which can be misleading when score distributions are imbalanced.
5. Repeat until model judge-human agreement is comparable to human-human agreement.

This workflow requires no code changes, only configuration changes to criteria, scoring levels, evaluation steps, and examples. After calibration, the model judge can run at scale and you can be more confident that its scores reflect the same quality standard your human reviewers applied.

You can see this calibration in use in [`Book Tracker: Using Evaluations to evaluate an intelligent feature`](book-tracker-using-evaluations-to-evaluate-an-intelligent-feature.md), a sample app that applies a judge-calibration evaluation, measures a model-judge’s scores against expert ratings with Cohen’s kappa, and then uses them to track tagging quality as the prompt changes.

#### Debug Scores with Rationales

When you use a [`ModelJudgeEvaluator`](modeljudgeevaluator.md), the model judge produces a written rationale alongside every score. A single rationale tells you about one sample. Reviewing multiple rationales reveals patterns in how the model judge interprets your instructions, applies your scale, and weighs your criteria.

Look for these common patterns when scores don’t match your expectations:

- **Criteria drift**: The rationale references evaluation dimensions you didn’t define. If the model judge mentions “creativity” when your instructions only cover accuracy and completeness, it’s introducing its own criteria. Add explicit instructions to evaluate only on the criteria you listed.
- **Score-rationale mismatch**: The model judge describes a response positively but assigns a low score, or vice versa. This usually signals ambiguous scale descriptions. Review the boundary between adjacent score levels and make the distinguishing features more concrete.
- **Inconsistent weighting**: Similar-quality responses receive different scores. Compare their rationales to find which criterion the model judge weighted differently. If the weighting seems arbitrary, revise the evaluation steps to give the model judge a clear procedure for balancing criteria.
- **Repetitive flagging**: The same weakness appears across many rationales. This might indicate a genuine pattern in your model’s output, but it also may mean the model judge is overemphasizing one criterion. Check whether the evaluation steps give that criterion disproportionate weight.

When rationales reveal a problem, adjust the corresponding part of the evaluator configuration: rewrite ambiguous criteria, sharpen the boundaries between score levels, reorder evaluation steps, or add scored examples at the levels where the model judge is inconsistent. Then rerun the evaluation and read the rationales again. This cycle of reading rationales, adjusting the configuration, and rerunning is how you bring the model-judge’s scoring in line with your expectations.

#### Use Reference Guided Judging for Verifiable Tasks

When evaluating tasks with objectively correct answers, for example, math, factual recall, code correctness, or tool selection, provide the model judge with the expected answer, creating a *reference-guided* approach.

Model-judge evaluators are susceptible to *answer contamination*, where an incorrect answer in the evaluation context causes the model judge to copy the wrong reasoning into its own chain of thought, even when the model can solve the problem independently. Reference-guided judging reduces this failure rate substantially.

## See Also

- [Scoring with model-judge evaluators](scoring-with-model-as-judge-evaluators.md)
  Score subjective qualities like tone, accuracy, and relevance that programmatic checks cannot measure.
- [struct ModelJudgeEvaluator](modeljudgeevaluator.md)
  An evaluator that uses a language model as a judge to score responses.
- [struct ModelJudgePrompt](modeljudgeprompt.md)
  A configuration for how a model evaluator constructs its prompt.
- [struct ScoreDimension](scoredimension.md)
  A named scoring dimension for a model evaluator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/designing-effective-model-judges)*