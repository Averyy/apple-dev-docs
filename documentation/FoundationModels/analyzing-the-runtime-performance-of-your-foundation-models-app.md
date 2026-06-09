# Analyzing the runtime performance of your Foundation Models app

**Framework**: Foundation Models

Measure how prompts, responses, and tool calls affect token consumption and response times in Instruments.

#### Overview

The Foundation Models instrument surfaces the prompts your app sends to the model, the tools the model calls, where your app spends time, and how your app consumes tokens — all of which helps you understand what your app is doing and when. Depending on the model provider you use, cost can be a factor to consider.

Use the breakdown of token usage to make informed decisions about cached tokens versus generated tokens. By analyzing your app’s model usage patterns, you can identify bottlenecks and apply targeted optimizations that help you reduce context size and improve the quality of your intelligent features. The instrument also provides insight into:

- The instructions, prompt, and response that form each request to the model.
- Where and how the model invokes the custom tools your app provides, along with how long the tool takes to run and its output.
- A per-session breakdown that contains details about how long every request took and how the session consumed tokens through each step.

Together, these insights show how your app interacts with the model and help you identify where to apply optimizations.

#### Launch and Configure Instruments for Recording

Instruments includes a default template you use when analyzing your app’s interactions with the Foundation Models framework. Start by opening Instruments from your Xcode project:

1. In Xcode, choose Product > Profile.
2. In the Template Selection window, select the Foundation Models template.
3. Click Choose.

![A screenshot that shows the Template Selection window with the Foundation Models](https://docs-assets.developer.apple.com/published/5e5ee21d294f4845e34a2a24a0bfddbf/analyzing-the-runtime-performance-of-your-foundation-models-app-template-selector%402x.png)

#### Record App Interactions to Gather Data

Before reviewing your app’s performance, check that your development device isn’t under thermal pressure or busy with other work. This helps you ensure that the device is in a good performance state, which can influence your analysis. When you record a run, use your app as normal and focus on interactions that perform requests to the model. Begin gathering data by clicking the Record Trace button in the upper-left corner or by choosing File > Record Trace:

![A screenshot of Instruments that shows the record button in the upper-left](https://docs-assets.developer.apple.com/published/2071901785d7cf1f4d991e1c155a84ff/analyzing-the-runtime-performance-of-your-foundation-models-app-record%402x.png)

Because a recording captures and stores all Foundation Models prompts and responses in an unencrypted form, Instruments presents an alert when you begin recording. The captured data can include sensitive information, so handle trace files accordingly, and use this feature in a manner consistent with the [`Apple Developer Program License Agreement`](https://developer.apple.comhttps://developer.apple.com/support/terms/apple-developer-program-license-agreement/). After starting the recording, perform actions that interact with the model, wait for the responses to complete, then click Stop to end recording.

#### Get to Know the Instrument

The primary timeline shows events the instrument measures. The width of each component on the timeline indicates latency.

![A screenshot of Instruments displaying the Foundation Models instrument track](https://docs-assets.developer.apple.com/published/7b0fffd5593cdb6f4c121f03a4cf776e/analyzing-the-runtime-performance-of-your-foundation-models-app-record-analysis%402x.png)

The Foundation Models track appears in your timeline, with several lanes that provide insight into your recording:

- ****Session****: The start and end points that reflect the length of time a session is in an active state.
- ****Request****: The time it takes to perform a request within a session.
- ****Instructions****: The instructions associated with the request.
- ****Model Inference****: The time the system takes to process the input prompt and compute the response.
- ****Tool****: The time a tool call occurs and the length of time it takes to perform work.
- ****Model Loading****: The time the system needs to load model data from storage before fulfilling a request.

Choose View > Zoom > Zoom in to review activity at a more granular time scale.

The Inspector shows several details for the request, like the instructions, prompt, response, duration, and token metrics. To view a detailed breakdown of the duration of a request:

1. Click the Foundation Models instrument.
2. Select View > Detail Area > Tree.
3. Select the Model Inference you want to analyze.
4. If the inspector isn’t visible, choose View > Show Inspector.

![A screenshot of Instruments displaying the Inspector. The inspector displays](https://docs-assets.developer.apple.com/published/d2c98d58dc9fa79313699aa471a92514/analyzing-the-runtime-performance-of-your-foundation-models-app-token-duration%402x.png)

The Inspector shows a breakdown of duration details:

- ****Total Duration****: The total end-to-end time from starting the request to completing the response.
- ****Response Duration****: The time spent generating the response, which excludes any input processing.
- ****Time to First Token****: The wait time before the model starts streaming its response.

#### Monitor Token Usage

When you prompt a language model, the model breaks down the input text into small fragments called *tokens*. Each token is typically a word or a piece of a word. The token count includes instructions, prompts, and outputs for a session instance. If your session processes a large number of tokens that exceed the context window, the framework throws the error [`LanguageModelError.contextSizeExceeded(_:)`](languagemodelerror/contextsizeexceeded(_:).md). For more information on managing the context window size, see [`Managing the context window`](managing-the-context-window.md).

More output tokens generally require more processing time. Additionally, processing time depends on the task you perform. For example, summarizing a document requires much less processing time than generating a new article, because it’s mostly a reading task for the model.

The cost of text varies between characters and symbols versus discrete words. For example, the word `Sourdough` might be one token, but a phone number like `+1-(408)-555-0123` might use over ten tokens because of the characters and symbols.

High token counts affect both initial processing time and memory usage. Use the inspector to view a detailed breakdown of token metrics for the request:

![A screenshot of Instruments displaying the Inspector. The inspector displays](https://docs-assets.developer.apple.com/published/297704ddc6a5a5643f0be378aa373d40/analyzing-the-runtime-performance-of-your-foundation-models-app-token-metrics%402x.png)

The Inspector shows a variety of token metrics:

- ****Total Tokens****: The total tokens the model processes, which equals the consumed input tokens plus the generated output tokens.
- ****Consumed Tokens****: The input tokens the model consumes, including the prompt, instructions, transcript, and other prompt metadata like tool definitions.
- ****Generated Tokens****: The output tokens the model generates in its response.
- ****Cached Tokens****: The input tokens the system reuses from a previous model request, which avoids reprocessing them to speed up the time to first token.

The cache hit rate is the percentage of input tokens the system serves from the prefix cache, and depends on the model provider you use. For more information about caching, see [`Optimizing key-value caching in language model sessions`](optimizing-key-value-caching-in-language-model-sessions.md).

#### Reduce Token Consumption

A lower token count improves performance and helps you stay within context limits.

The `includeSchemaInPrompt` parameter in [`streamResponse(generating:includeSchemaInPrompt:options:prompt:)`](languagemodelsession/streamresponse(generating:includeschemainprompt:options:prompt:).md) tells the framework to include information about [`Generable`](generable.md) types in your prompts before processing the request. Doing so improves the output quality, but requires that the model consumes more input tokens. If you’ve already made a similar request or provided examples in your instructions, you can exclude the schema in subsequent requests. Excluding the schema removes redundant schema information and can save hundreds of tokens per request. To further optimize token usage, consider whether you need nested [`Generable`](generable.md) types in a parent type. The model needs more context to handle nested [`Generable`](generable.md) schema details.

When you no longer need the schema data for your session, set `includeSchemaInPrompt` to `false`:

```swift
do {
    // Stream a response from the model and exclude the schema for your 
    // custom type.
    for try await partial in session.streamResponse(to: myPrompt,
                                                    generating: MyCustomItinerary.self,
                                                    includeSchemaInPrompt: false) {
        // Handle the partial result.
    }
} catch {
    // Handle the error that the method throws.
}
```

After you make this change, record a new trace and use the Inspector panel to check that the token counts remain within your intended budget. A lower total token count translates to faster initial processing. For more context window management techniques, see [`Managing the context window`](managing-the-context-window.md).

## See Also

- [Evaluating prompts to measure performance and improve model responses](evaluating-prompts-to-measure-performance-and-improve-model-responses.md)
  Systematically measure and improve the quality of your prompts by using structured evaluation.
- [Evaluating language model responses](../Evaluations/evaluating-language-model-responses.md)
  Build an evaluation that runs your intelligence-powered feature against samples and scores each response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/analyzing-the-runtime-performance-of-your-foundation-models-app)*