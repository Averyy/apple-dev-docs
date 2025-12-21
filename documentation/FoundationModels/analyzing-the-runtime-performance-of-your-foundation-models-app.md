# Analyzing the runtime performance of your Foundation Models app

**Framework**: Foundation Models

Optimize token consumption and improve response times by profiling your app’s model usage with Instruments.

#### Overview

Use Instruments to analyze the runtime performance, resource usage, and behavior of your app. Instruments provides several tools to help you understand how responsive your app is and what kind of power impact it has on the system, as well as diagnose hitches and more.

The Foundation Models instrument provides details about the interactions your app has with the on-device model, so you can get insight into:

- When the system loads model assets
- How long it takes to start receiving a response from the model
- What the token usage is across individual sessions
- Where the model invokes any custom tools your app provides

The Foundation Models instrument helps you identify exactly where your app spends time and uses tokens. By analyzing your app’s model usage patterns, you can identify bottlenecks and apply targeted optimizations to improve responsiveness and runtime performance.

Use additional instruments — alongside the Foundation Models instrument — to understand the impact your model interactions have on thermal state, power, and other system resources.

#### Launch and Configure Instruments for Recording

Start by opening Instruments from your Xcode project:

1. From the Xcode Product menu, choose Profile.
2. In the Template Selection window, select the Blank template and click Choose.
3. Click the “+ Instrument” button in the toolbar to add an instrument.
4. Search for “Foundation Models” and drag the instrument into your document.

![A screenshot that shows the Instruments app’s default UI for a blank template,](https://docs-assets.developer.apple.com/published/6743063b98571aa8c97ddeb0df398064/analyzing-the-runtime-performance-of-your-foundation-models-app-template%402x.png)

Before you begin recording a session, consider adding additional instruments that can help you understand the impact your app has on system resources, like Time Profiler, CPU Profiler, and Power Profiler:

> **Note**: Some instruments, like Power Profiler, aren’t available to use with Simulator.

After you configure your template for analyzing your Foundation Models usage, choose File > Save As Template, to make it easier to reuse the same configuration when launching Instruments.

#### Record App Interactions to Gather Data

Before reviewing the performance of your app, first check that your development device isn’t under thermal pressure or busy with other work. This helps you ensure that the device is in a good performance state, which can influence your analysis. When you record a run, use your app as normal and focus on interactions that perform requests to the model. Begin gathering data by clicking the Record Trace button on the top left or by choosing File > Record Trace:

![A screenshot of Instruments that shows the record button in the top left of the](https://docs-assets.developer.apple.com/published/617a8158d453868be06fd695771b6f38/analyzing-the-runtime-performance-of-your-foundation-models-app-record%402x.png)

After you perform actions that generate model responses, wait for the responses to complete, then click Stop to end recording.

#### Get to Know the Instrument

The primary timeline consists of events that the instrument measures. The width of each component on the timeline indicates latency. The Foundation Models track appears in your timeline, with several graphs that provide insight into your session and assets:

The following image shows the Foundation Models instrument after recording a trace:

![A screenshot of Instruments after recording a session. It shows the timeline](https://docs-assets.developer.apple.com/published/311c5c444b1dedb67f45d16417464af1/analyzing-the-runtime-performance-of-your-foundation-models-app-record-analysis%402x.png)

To review what is happening at a more granular level, press Command-Plus Sign to zoom in, or Command-Minus Sign to zoom out of the timeline:

![A screenshot of the timeline in Instruments after zooming into the](https://docs-assets.developer.apple.com/published/118cd8356bb67df21df422f0e7fd7293/analyzing-the-runtime-performance-of-your-foundation-models-app-timeline%402x.png)

#### Understand Token Usage

When you prompt a language model, the model breaks down the input text into little fragments called tokens. Each token is typically a word or a piece of a word. The token count includes instructions, prompts, and outputs for a session instance. If your session processes a large number of tokens that exceed the context window, the framework throws the error [`LanguageModelSession.GenerationError.exceededContextWindowSize(_:)`](languagemodelsession/generationerror/exceededcontextwindowsize(_:).md). For more information on managing the context window size, see [`TN3193: Managing the on-device foundation model’s context window`](https://developer.apple.com/documentation/Technotes/tn3193-managing-the-on-device-foundation-model-s-context-window).

More output tokens generally require more processing time. Additionally, processing time depends on the task you perform. For example, summarizing a document requires much less processing time than writing a new article, because it’s mostly a reading task for the model.

The cost of text varies between characters of symbols versus discrete words. For example, the word “Sourdough” might be one token, but a phone number like +1-(408)-555-0123 might use over ten tokens because of the characters and symbols.

High token counts affect both initial processing time and memory usage. The Inference detail area shows token metrics for each session. Token counts above 1000 may slow down response generation, especially on older devices. When you are testing runtime performance, compare token counts across different app interactions to identify which prompts consume the most tokens.

To compare token counts:

1. Click the Foundation Models instrument.
2. Select View > Detail Area > Inference.

The following image shows the details about a single session, including a breakdown of where the session spent time:

![A screenshot of the detail area in Instruments. It shows details about a single](https://docs-assets.developer.apple.com/published/b15c566d66da4437c96491356c4d7e7f/analyzing-the-runtime-performance-of-your-foundation-models-app-inference%402x.png)

The Inference detail area reveals a breakdown of the session calls during the recorded trace. It also includes:

For each request, Instruments provides additional details:

By default, the entire timeline is in a selected state. If you want to focus on a specific time frame to understand more about the performance at a specific point in time, click and drag inside the timeline to select the range you want to analyze, or press Command-Plus Sign to zoom in and Command-Minus Sign to zoom out.

#### Optimize Model Loading with Prewarming

Asset-loading delays appear as gaps between the start of a request and the first token generation. A delay of several hundred milliseconds before tokens start appearing means that your app loads the model after a person makes a request. If you know that your app needs to make a call to the model soon, use the [`prewarm(promptPrefix:)`](languagemodelsession/prewarm(promptprefix:).md) method to load the model before you need to call it. Preload the model when you have at least one second before calling a respond method. This technique moves loading time away from the critical response path to improve the responsiveness of your app.

```swift
// Create a session.
var session = LanguageModelSession()

// Prewarm the session when a person navigates to a screen that uses the session.
session.prewarm()
```

A prompt prefix helps the model prepare for similar requests, reducing the time to first token. When you know the type of requests a person is about to make, improve performance by providing a prefix that matches your app’s common prompt patterns. For example, if your app generates itineraries, prewarm the model with the prefix you expect to use for each request:

```swift
// Prewarm with context about the likely request.
session.prewarm(promptPrefix: "Generate a travel itinerary for")
```

After implementing prewarming, profile your app again to verify that asset loading happens before the request is made — eliminating delays in the critical path.

#### Reduce Token Consumption

A lower token count improves performance and helps you stay within context limits.

The `includeSchemaInPrompt` parameter in [`streamResponse(generating:includeSchemaInPrompt:options:prompt:)`](languagemodelsession/streamresponse(generating:includeschemainprompt:options:prompt:).md) tells the framework to include information about [`Generable`](generable.md) types in your prompts before processing the request. Doing so improves the output quality, but requires that the model consumes more input tokens. If you already made a similar request or provided examples in your system instructions, you can exclude the schema in subsequent requests. Excluding the schema removes redundant schema information and can save hundreds of tokens per request. To further optimize token usage, consider whether you need nested [`Generable`](generable.md) types in a parent type. More context is necessary to handle nested [`Generable`](generable.md) schema details.

When you no longer need the schema data for your session, set `includeSchemaInPrompt` to `false`:

```swift
let response = try await session.streamResponse(
    prompt: prompt,
    generable: MyCustomItinerary.self,
    options: .init(includeSchemaInPrompt: false)
)
```

After you make this change, the Inference section of the Foundation Models instrument displays lower maximum token counts, which translates to faster initial processing. The following screenshot shows the input token count — with `includeSchemaInPrompt` set to `true` — after running three generation requests:

![A screenshot of the detail area that shows information about requests made](https://docs-assets.developer.apple.com/published/91f1f378bba3472565354d5e2f76e6b6/analyzing-the-runtime-performance-of-your-foundation-models-app-schema-1%402x.png)

The following image shows similar requests, with `includeSchemaInPrompt` set to `false`:

![A screenshot of the detail area that shows information about requests made](https://docs-assets.developer.apple.com/published/c2fc46ed8f3bafa9afbf743aa8365c7e/analyzing-the-runtime-performance-of-your-foundation-models-app-schema-2%402x.png)

#### Verify Your Optimizations

When you perform runtime optimization updates in your code, profile your app each time to confirm that the changes improve performance. Compare the new timeline with your previous recordings, and rename each recording from the sidebar based on what changed between runs, to help indicate what the run involved.

Successful prewarming moves asset loading earlier in the timeline and before an app makes a request to the model. This reduces the amount of time a session takes to start generating a response to the request and shortens the time an app waits to perform additional requests or UI updates. The following image shows a request being made to the model after an app calls [`prewarm(promptPrefix:)`](languagemodelsession/prewarm(promptprefix:).md):

![A screenshot of the timeline in Instruments after zooming into the](https://docs-assets.developer.apple.com/published/bfc4d9fb531e4312903d7019bc746547/analyzing-the-runtime-performance-of-your-foundation-models-app-verify-changes%402x.png)

When you evaluate your app, look for these improvements in each recording:

- Asset loading happens before the app makes the request.
- The first tokens appear immediately after the session starts processing the request.
- The Inference detail area shows lower token counts.
- The overall session and tool-calling response times meet the intended user experience.

## See Also

- [Prompting an on-device foundation model](prompting-an-on-device-foundation-model.md)
  Tailor your prompts to get effective results from an on-device model.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/analyzing-the-runtime-performance-of-your-foundation-models-app)*