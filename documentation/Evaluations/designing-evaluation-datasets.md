# Designing datasets to test your feature

**Framework**: Evaluations

Build categorized test datasets that reflect the full range of real-world use of your feature.

#### Overview

Your evaluation is only as good as the inputs you measure. A *dataset*, the text, images, or code you run your feature against, gives you false confidence if it only covers the happy path. Datasets that reflect real usage patterns reveal where your feature actually breaks. Choosing what data to test against is a natural next step after defining your success criteria and scoring approaches. For more details on defining your criteria, see [`Designing specific, measurable criteria in an evaluation suite`](designing-evaluation-criteria.md).

This article guides you through designing datasets that test your feature thoroughly: thinking about who uses your feature, categorizing samples by purpose, sourcing data from multiple channels, and using synthetic generation to expand coverage without sacrificing quality.

#### Think About the People Using Your Feature

Before writing individual test cases, sketch a few *user profiles*: short descriptions of typical users, their goals, and how they phrase requests. Each profile becomes a source of *samples*, the individual inputs you run through your evaluation. Consider the variety of people who interact with your feature: think about their expertise levels, what goals they might have, the way they phrase requests, and the edge cases their usage patterns create.

Each profile needs at least one sample in your dataset. As you expand, add more samples per profile to cover variations within each group.

#### Categorize Samples By Purpose

Separate your test data into categories based on what each sample tests. The categories below cover the range from cases your feature must always handle to inputs you expect it to refuse. They’re a starting point, and you may add others that fit your feature:

- **Golden set**: Core happy-path functionality that must always pass. These are your most representative, well-understood use cases. They define your quality floor.
- **Edge cases**: Uncommon but valid inputs that test boundary behavior. Very short inputs, very long inputs, unusual formatting, ambiguous requests, contradictory constraints.
- **Adversarial inputs**: Attempts to break the feature. Prompt injection, requests for harmful content, attempts to extract system prompts or bypass safety measures.
- **Known failures**: Previously discovered issues captured as regression tests. Every production failure you discover feeds into this category. These prevent fixed issues from reappearing.

Swift Testing’s `@Suite` macro is one way to keep each category isolated and runnable on its own:

```swift
@Suite("Golden") struct GoldenEvaluations { /* ... */ }
@Suite("Edge cases") struct EdgeCaseEvaluations { /* ... */ }
@Suite("Adversarial") struct AdversarialEvaluations { /* ... */ }
@Suite("Known failures") struct KnownFailureEvaluations { /* ... */ }
```

#### Source Your Data Deliberately

No single data source covers everything. Combine these approaches to build a dataset with both depth, reflecting real-world usage, and breadth, covering the full range of ways your feature can be used:

- **Manual creation**: The most common starting point. Create test cases that target specific scenarios, edge cases, or failure modes you hypothesize.
- **Real-world interactions**: After your feature is in use, real inputs reveal unexpected patterns that synthetic data rarely captures. When these inputs come from people using your app, use them only with their permission. For design guidance, see [`Human Interface Guidelines > Privacy`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/privacy).
- **Synthetic generation**: Use [`SampleGenerator`](samplegenerator.md) to expand a small set of manually created samples into a larger dataset. See [`Generating synthetic datasets`](generating-synthetic-evaluation-datasets.md) for the API walkthrough.

Begin with a small number of carefully chosen samples; each represents a distinct scenario your feature needs to handle. Focus on quality over quantity as you begin. After your evaluators are stable and producing useful signals, expand with synthetic generation.

#### Design Effective Seed Samples for Synthetic Generation

Synthetic generation amplifies whatever patterns exist in the seed samples you give the model. *Seed samples* are the small set of hand-written examples that the generator uses as a pattern for producing new ones. If your seeds are narrow, the generated data is narrow. Investing in high-quality seeds produces outsized returns because seed quality has a disproportionate effect on output quality: improving ten mediocre seeds into ten excellent seeds produces a larger quality gain than adding ninety more mediocre seeds.

##### Cover the Axes That Matter

Design your seed samples to span the dimensions you care about: difficulty levels, input lengths, phrasing styles, categories, and edge conditions. If your seeds are all short, straightforward, happy-path examples, the synthetic output will be too.

For each dimension of variation in your feature, include at least one seed that represents each end of the spectrum. For example, a task-extraction feature might need seeds that cover:

- Simple and complex inputs
- Every output category
- Inputs with and without temporal information
- Urgent and non-urgent scenarios
- Ambiguous requests where the correct interpretation requires judgment

##### Include Hard and Adversarial Seeds

A useful guideline is to make at least 20-30 percent of your seeds genuinely difficult cases. Models gravitate toward medium difficulty when generating; hard seeds push the generated data toward more challenging examples. Without them, you get a dataset full of straightforward examples that don’t test your feature’s limits.

Similarly, include seeds where the correct behavior is to refuse, flag ambiguity, or produce a partial answer. Without these, synthetic datasets develop a bias toward always producing a complete, confident answer.

> 💡 **Tip**: Mark each seed with its category, difficulty level, and what dimension of quality it tests. This lets you verify that the generated dataset maintains coverage across all dimensions and catch imbalances early.

#### Expand Datasets Within Each Sample Category

Expand your dataset by using [`SampleGenerator`](samplegenerator.md) to generate synthetic samples. Write focused generation prompts for each category or dimension rather than a single prompt that asks for diversity across everything.

This focused approach gives you guaranteed representation across categories, higher per-category quality because each prompt provides focused context, and the ability to iterate on one category without regenerating everything else.

Avoid a single prompt like “generate diverse test cases covering all categories.” That approach produces three problems:

- **Frequency bias.** The model gravitates toward its most common training examples, over-representing typical scenarios.
- **Uneven coverage.** Even when you list categories explicitly, the model doesn’t allocate evenly. Some categories dominate while others barely appear.
- **Diminishing novelty.** As the model generates more items in a single pass, later items tend toward repetition or slight rephrasings.

If your feature has multiple independent dimensions of variation (for example, category and difficulty), generate for combinations of dimensions: work tasks that are urgent, personal tasks that are easy, health tasks that are ambiguous. This cross-product approach provides coverage that a single “diverse” prompt cannot.

In practice, filter your seeds to the category you want to expand and pair them with a prompt that names that category’s characteristics, then repeat for each category you care about:

```swift
// Generate urgent work tasks with tight deadlines.
let workSeeds = dataset.filter { $0.expected?.category == .work }
let workPrompt: Prompt = """
    Generate realistic work tasks with explicit deadlines within 48 hours.
    Vary phrasing: some as direct requests, some as meeting invites, some as
    forwarded messages. Each needs a clear urgency signal.
    """
for try await sample in workSeeds.makeSamples(workPrompt, targetCount: 30) {
    expanded.append(sample)
}

// Separately, generate ambiguous personal tasks with no due date.
let personalSeeds = dataset.filter { $0.expected?.category == .personal }
let personalPrompt: Prompt = """
    Generate personal reminders where the correct category isn't obvious and
    no due date is specified. Include requests that could plausibly be
    errands, home, or health tasks.
    """
for try await sample in personalSeeds.makeSamples(personalPrompt, targetCount: 30) {
    expanded.append(sample)
}
```

#### Compensate for Synthetic Data Limitations

Synthetic generation is valuable for expanding coverage and testing statistical consistency, but it can’t replace careful human-written cases for every situation. It has systematic gaps where the generator’s output can mislead you about your feature’s quality. Compensate by understanding where synthetic data works well, where it falls short, and what failure modes to watch for.

**Strengths**:

Synthetic generation is well-suited to:

- **Format and structure testing.** Evaluating whether a model follows instructions, produces valid output structures, or respects constraints. Format compliance is objectively verifiable.
- **Paraphrase and robustness testing.** Generating surface-level variations of existing samples to test whether your feature handles different phrasings of the same intent.
- **Classification and routing tasks.** Intent classification, topic categorization, and structured extraction all have constrained output spaces that make quality easy to verify.
- **Coverage expansion.** Starting from real evaluation data and expanding to cover underrepresented categories, input lengths, or phrasings.

**Weaknesses**:

Synthetic generation tends to fall short for:

- **Domain-expert knowledge.** Medical, legal, or scientific evaluation data requires domain expertise. Models produce plausible-sounding but subtly incorrect reference answers precisely where correctness matters most.
- **Adversarial and safety testing.** Synthetic adversarial prompts tend to be predictable patterns the model has already been trained to handle. Real human-crafted attacks are more creative and expose gaps that generated attacks miss.
- **Long-tail distributions.** If your real usage has a heavy-tailed distribution, synthetic data under-represents the tails. Models tend to converge on the most common patterns, producing increasingly “typical” outputs.
- **Cultural and contextual nuance.** Questions that depend on regional knowledge, cultural context, or temporal facts get flattened into generic patterns that miss real-world diversity.

**Failure modes**:

When reviewing synthetic output, watch for these patterns:

- **Mode collapse.** The generator produces variations of a few patterns rather than genuinely diverse samples. If you cluster the output and find most samples in one or two clusters, the data lacks variety.
- **Difficulty collapse.** Generated samples converge toward medium difficulty. Very easy and very hard cases are underrepresented relative to your seeds.
- **Answer leakage.** The generated prompt contains enough hints to make the expected answer trivially derivable, making the evaluation too easy.
- **Distributional shift.** The synthetic distribution doesn’t match real-world usage, so evaluation results don’t predict production performance.

#### Validate Synthetic Output Before Relying on It

Validate your generated data before you trust it as your evaluation benchmark. Use a layered approach:

**Programmatic validation.** Pass a `validator` closure to the generator to reject samples that fail basic quality checks: empty fields, format violations, obviously incorrect labels. This catches the most common errors automatically.

**Category balance checks.** After generation, verify that the output distribution matches your intended distribution. If you asked for coverage across five categories, check that you actually got meaningful representation in all five rather than heavy concentration in two or three.

**Human spot-checking.** Manually review a random 5-10 percent sample of generated data. Look for factual errors in reference answers, trivial or unanswerable questions, answer leakage in the prompt, and distribution skew.

**Self-consistency checks.** Generate multiple answers to the same question. If the answers vary wildly, the question may be ambiguous or the reference answer unreliable. This catches subtle quality issues that other validation methods miss.

**Deduplication.** The generator removes identical prompts automatically, but semantically similar samples with different surface wording may still cluster too tightly. Decide whether near-duplicates help (testing robustness to phrasing variation) or hurt (skewing your distribution toward a single scenario).

> ❗ **Important**: Synthetic data expands coverage and tests statistical consistency, but it doesn’t replace carefully designed edge cases or real-world failure data. The most valuable test cases still come from production failures and deliberate adversarial thinking. Maintain at least 20-30 percent human-written samples alongside synthetic ones as a calibration anchor.

#### Decide How Much Data Is Enough

For evaluation datasets, more is not always better. Unlike training data, evaluation datasets have diminishing returns: you need coverage and quality, not volume. A well-constructed set of 100-500 samples can be more discriminating than a noisy set of 5,000, which might have duplicates, ambiguous expected outputs, or samples that don’t actually probe the dimensions you care about.

Practical ranges to consider:

- **Single feature evaluation.** 100-500 samples with coverage across difficulty levels and input subtypes.
- **Multi-feature benchmark.** 50-200 samples per feature or category.
- **Statistical power.** To detect a 5-percent accuracy difference with 95-percent confidence, you need approximately 400 samples.

Start small, focus on quality, and expand only when your evaluators are stable and you need broader statistical coverage.

## See Also

- [Generating synthetic datasets](generating-synthetic-evaluation-datasets.md)
  Expand a small set of manually written evaluation samples into a larger dataset.
- [struct ModelSample](modelsample.md)
  A general-purpose language model evaluation sample.
- [protocol Loader](loader.md)
  A protocol for types that supply a dataset for evaluation.
- [actor SampleGenerator](samplegenerator.md)
  An actor that generates evaluation samples using a language model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/designing-evaluation-datasets)*