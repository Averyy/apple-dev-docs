# Evaluating prompts to measure performance and improve model responses

**Framework**: Foundation Models

Systematically measure and improve the quality of your prompts by using structured evaluation.

#### Overview

Prompt evaluation is the practice of thoroughly testing your prompts against real-world scenarios to measure quality, catch failures early, and confidently improve your feature over time.

When adding generative capabilities to your app, you write prompts that tell the model what to do. A prompt might ask the model to summarize text, answer questions, generate content, or make recommendations based on a person’s input.

Writing a prompt that works for one or two test cases might be straightforward in your app. The challenge comes when you need to verify that your prompt works reliably across many scenarios, and that modifying your prompt improves quality instead of silently breaking existing functionality.

Starting with prompt evaluation doesn’t require building a complete system immediately. Begin with a single critical quality criterion and a handful of test scenarios. As you see the value — catching a failure you might have missed, making an improvement with confidence, or tracking quality over time — expand your coverage.

##### Understand Why Prompt Evaluation Matters

Unlike traditional software where the output is predictable and repeatable, generative models introduce unique challenges that make evaluation essential.

The response you get from a model can vary even though you provide the same exact input. This variation comes from the probabilistic nature of how the model generates text, and from updates to the underlying model that you don’t control.

Traditional software testing relies on exact matches, like whether a function returns the value `42`. With generative models, the response quality depends on nuanced criteria, like “Generate a recipe that’s appropriate for beginners.” Handle subjectiveness by translating your requirements into objective and measurable criteria. For example, you might determine that a recipe for a beginner involves three to six ingredients and takes less than 20 minutes to make.

Adding a single word to your prompt can dramatically change the model’s behavior. A change that improves one type of input might break others. Without systematic evaluation, it’s impossible to know whether a modification is genuinely beneficial or if it introduces a new problem.

It’s important to remember that the response a model generates reaches a person. For example, a recipe app that suggests ingredients to someone with dietary restrictions or a summarization tool that misrepresents key information. By evaluating how the model responds to your app’s prompts, you can catch potentially harmful failures to help protect people who use your app.

##### Transform Vague Goals Into Measurable Criteria

The first step in evaluating prompts is transforming vague quality goals into concrete, measurable criteria. Instead of hoping your feature works well, you define exactly what success looks like in quantifiable terms.

Consider a recipe recommendation feature that starts with the following informal goals:

- Recipes need to respect dietary restrictions.
- Suggestions need to match the person’s cooking skill level.
- The app needs to be helpful.

These goals are a good start, but they’re too vague to measure. Evaluation requires translating the goals into specific, testable criteria:

- **Dietary compliance**: 100 percent of the recommended recipes avoid all ingredients the person marked as dietary restrictions. This is a pass or fail measurement with zero tolerance for violations.
- **Skill level alignment**: The complexity rating of recipes the model generates deviates by no more than `0.5` points on a one-to-three point scale from the person’s stated skill level. This is a numeric measurement with a defined threshold.
- **Helpfulness**: 90 percent of recommendations receive positive ratings when evaluated against a standardized rubric that covers relevance, clarity, and actionability. This transforms subjective quality into a measurable percentage.

This transformation from something that seems good to something that meets defined criteria is what makes for a useful evaluation. You replace personal judgment with objective measurements that you can track, automate, and compare over time.

##### Examine the Anatomy of an Evaluation

A complete evaluation system has three core components working together: test inputs, quality criteria, and the measurement methods you use.

Test inputs are the realistic scenarios your feature needs to handle. For a recipe app, this includes:

- Common dietary needs, like vegetarianism
- Complex cases with multiple restrictions
- Edge cases, like contradictory requirements
- Adversarial inputs designed to break the system

The diversity and quality of your test scenarios directly determines how much you can trust your evaluation results.

Quality criteria are the specific measurements you take for each test. Each criterion examines one aspect of quality and reveals a complete picture of your feature’s behavior. In a recipe app, you might check whether the output:

- Respects the person’s dietary needs
- Matches the requested difficulty level
- Avoids duplicates
- Excludes dangerous ingredients

For each quality criterion, you need a way to automatically check if the output meets the standard. Some checks are straightforward, like checking a recipe list to see if it contains a forbidden ingredient. Others might require more sophisticated approaches, like when you try to determine if a recipe explanation is appropriate for a beginner.

When you run an evaluation, each test input flows through your feature’s prompt and the model generates output. That output is then automatically checked against all your quality criteria, producing a set of measurements —– pass-fail results, numeric scores, or percentage ratings —– that tell you exactly how well your prompt performs.

##### Understand Measurement Approaches

Different quality criteria require different measurement approaches. Knowing which approach to use helps you build comprehensive evaluations.

- **Rule-based measurement**: Applies fixed, deterministic logic that checks objective properties, like answering whether the output contains forbidden words or ingredients. This measurement works well when you write explicit logic to verify correctness.
- **Comparison to ground truth**: Measures how closely the output matches a known correct answer. For some tasks, prepare example outputs that represent exactly what you want the model to generate. For example, you can have a verified answer for factual questions. A measurement technique, like string similarity, helps quantify how close the model’s output comes to the ideal answer.
- **Semantic similarity**: Evaluates the meaning rather than the exact wording. By converting text to embeddings — mathematical representations of meaning — you can measure how conceptually similar outputs are, even when they don’t share the exact phrases. This approach is particularly valuable when there are many valid ways to express the same information.
- **Model-based judgment**: Uses another model to evaluate outputs. Just as humans can judge whether text is *helpful* or *creative*, you can prompt models to make similar judgments. This approach works well for nuanced criteria like tone, creativity, or adherence to complex guidelines. However, it’s important to verify the judging model’s assessment align with human judgment before relying on its scores.

Most robust evaluations combine multiple approaches. For example, measuring the effectiveness of a recipe recommendation might use rule-based checking for dietary compliance, comparison to ground truth for ingredient accuracy, and model-based judgment to rate the difficulty.

##### Build Your Evaluation Dataset

Your evaluation is only as good as the scenarios you test against. A narrow dataset might make a flawed prompt appear perfect, while a comprehensive dataset reveals issues before they reach the people who use your app.

Key success scenarios represent your core use cases, which are the common interactions that your feature must handle well. For a recipe app, this includes simple requests with a single dietary restriction, straightforward ingredient combinations, and typical time constraints. These are scenarios you expect to pass consistently.

Challenge scenarios push the boundaries of what your app does. Edge cases involve unusual but valid inputs, like zero cooking time, contradictory preferences, or rare ingredient combinations. Adversarial inputs deliberately try to break your feature, like “Give me a vegan steak recipe,” which tests how the model handles conflicts. Known failure modes capture specific scenarios where your prompt previously failed, and ensures you don’t regress.

If your feature serves people across different regions, experience levels, or use cases, your dataset needs examples from each category. This prevents your evaluation from optimizing for one group while missing problems that affect others.

You might start a dataset with scenarios you manually create that target specific requirements. As people use your feature, real interactions reveal unexpected patterns and edge cases you can add. Consider using a generative model to build additional test scenarios by creating synthetic data that explores variations, like “Generate 50 different ways a person might ask for a low-carb recipe.”

##### Follow the Evaluation Driven Workflow

Evaluation isn’t a one-time verification step — it’s a continuous cycle that drives quality improvement throughout development. The cycle follows five steps:

1. Define the key success scenarios.
2. Develop with testability in mind.
3. Run systemic evaluations.
4. Analyze patterns in failures.
5. Make targeted improvements.

Before writing any prompt, identify what your feature needs to accomplish and how you’ll measure it. This process forces clarity about requirements and prevents building toward vague goals.

As you write your prompt and build your features, simultaneously create your test scenarios and measurement criteria. This parallel development process helps verify that your evaluation reflects real requirements.

Execute your complete evaluation suite frequently to know exactly where your feature succeeds and where it needs improvement. Each test scenario flows through your prompt, generates output, and gets measured against all of your quality criteria.

When a test fails, look for patterns to determine whether the failures relate to a specific problem, like dietary restrictions in a recipe app. Do certain complexity levels perform worse or does the model struggle with particular phrasings? Patterns help you identify the underlying issues to address.

Based on your analysis, you may need to refine your prompt, adjust the model settings, or expand your test coverage. When you make these changes, immediately re-run the full evaluation suite to verify the change worked and didn’t introduce regressions elsewhere in your app.

This iterative refinement process, often called *hill climbing*, systematically improves quality. Small, measured changes accumulate into significant improvements, with evaluation providing continuous feedback about whether you’re moving in the right direction.

##### Prevent Regressions

One of evaluation’s most valuable benefits is regression prevention. As your feature evolves, evaluation verifies that improvements in one area don’t silently break functionality elsewhere.

For example, you might change a prompt in your recipe app to generate more creative suggestions. When you add *creative and surprising* to your instructions, it’s not clear whether the change works. Without evaluation, you might manually check a few examples that show more interesting recipes and ship the change. But with evaluations, you immediately see the full impact across your app. You might see that creative scores improved, but dietary compliance dropped because the unusual ingredient combinations included dietary restrictions. Or maybe beginner-appropriate recipes became too complex.

Your evaluation suite catches these trade-offs and lets you refine the approach before it reaches the people who use your app. Evaluations become more important over time as prompts naturally accumulate complexity and with the model receives updates. Each modification to a prompt carries risk, so introducing automated evaluation provides a safety net that catches issues immediately.

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
- [Updating prompts for new model versions](updating-prompts-for-new-model-versions.md)
  Manage the prompts your app uses by versioning them to make the most out of model improvements.
- [Analyzing the runtime performance of your Foundation Models app](analyzing-the-runtime-performance-of-your-foundation-models-app.md)
  Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.
- [class LanguageModelSession](languagemodelsession.md)
  An object that represents a session that interacts with a language model.
- [struct Instructions](instructions.md)
  Details you provide that define the model’s intended behavior on prompts.
- [struct Prompt](prompt.md)
  A prompt from a person to the model.
- [struct Transcript](transcript.md)
  A linear history of entries that reflect an interaction with a session.
- [struct GenerationOptions](generationoptions.md)
  Options that control how the model generates its response to a prompt.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/evaluating-prompts-to-measure-performance-and-improve-model-responses)*