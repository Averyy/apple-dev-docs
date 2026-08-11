# Running a Core AI model in a Foundation Models session

**Framework**: Foundation Models

Send requests on device to an open source model you export with Core AI to get a consistent API experience.

#### Overview

By default, the Foundation Models framework provides access to the same on-device and server models that power Apple Intelligence. With these models, you can build privacy-preserving intelligent features while allowing your app to perform generative tasks offline. The framework provides a consistent API experience for using any language model, including those you bring from other model providers. Use other on-device models when you need to:

- Access specialized capabilities that the model provides.
- Support a range of devices that might not support Apple Intelligence.
- Maintain cross-platform support.

With [`Core AI`](https://developer.apple.com/documentation/CoreAI), you can deploy AI models within your app and load them into the same language model session API you already use. Only the model you pass into [`init(model:tools:instructions:)`](languagemodelsession/init(model:tools:instructions:).md) changes.

> **Note**: Running and integrating a Core AI model requires macOS 27, iOS 27, and Xcode 27 or later.

#### Export an Open Source Model

The open-source [`coreai-models`](https://developer.apple.comhttps://github.com/apple/coreai-models) Swift package provides model export recipes and utilities for building on-device AI with [`Core AI`](https://developer.apple.com/documentation/CoreAI). The package contains `CoreAILanguageModel`, which conforms to the `LanguageModel` protocol, and you can use it to easily load an on-device model and prepare it to run.

Discover open source models to export by following these steps:

1. Open Terminal.
2. Install the `uv` package manager.
3. Clone the Core AI models repository.
4. Change to the `coreai-models` directory.

To discover models that Core AI supports, use Terminal to list the models from the registry, like this:

```bash
# List the models that the registry supports and their export presets.
uv run coreai.model.registry --list-models
```

Core AI exports an open source model into a resource folder you bundle with your app. The folder contains an `.aimodel` file alongside the tokenizer and any other resources the model needs.

The model registry list provides the identifer column `HF_ID` that you use when exporting the model. Choose a model around 0.6B parameters as a good first choice because it downloads quickly and runs comfortably on device. Because models are specialized to the device they run on, you need to export a model for the platform you target, as shown here:

```bash
# Export the model for macOS.
uv run coreai.llm.export HF_ID

# Export the same model for iOS.
uv run coreai.llm.export HF_ID --platform iOS
```

After the export completes, add the folder to your app so your code can load it at runtime.

> **Note**: Each model in the registry has its own README with the exact export recipe and any model-specific requirements. Review the `models` directory in `coreai-models` for additional details.

#### Load the Exported Model Into a Session

Create a `CoreAILanguageModel` from the URL of the exported resource folder, then pass it to a [`LanguageModelSession`](languagemodelsession.md). To access `CoreAILanguageModel`, add `coreai-models` as a package dependency in Xcode by following these steps:

1. Select File > Add Package Dependencies.
2. In the search bar, enter [`coreai-models`](https://developer.apple.comhttps://github.com/apple/coreai-models).
3. Select `coreai-models`.
4. Choose Add Package.
5. In the view that appears, click None next to `CoreAILM` and choose your app from the drop-down selector.
6. Choose Add Package.

Because `CoreAILanguageModel` conforms to [`LanguageModel`](languagemodel.md), you initialize the session the same way you do with the on-device or server-based model, as follows:

```swift
import FoundationModels
import CoreAILanguageModels

// Locate the Core AI resource folder you export and bundle it with your app.
guard let modelURL = Bundle.main.url(forResource: "The model name",
                                     withExtension: nil) { 
    // Handle the missing resource. 
}

// Load the model and create a session that runs requests through it.
let model = try await CoreAILanguageModel(resourcesAt: modelURL)
let session = LanguageModelSession(model: model)
```

Loading is asynchronous because the framework compiles the model and loads its tokenizer before the first request. Load a model ahead of time when you know a request is at least a second or two away so it’s ready when a person interacts with your feature. For more information about compiling models in advance, see [`Compiling Core AI models ahead of time`](https://developer.apple.com/documentation/CoreAI/compiling-core-ai-models-ahead-of-time).

#### Run Requests Through the Session

After you create the session, the API is identical regardless of which model backs it. The [`respond(to:options:)`](languagemodelsession/respond(to:options:).md) and stream methods, along with any [`Tool`](tool.md) instances and [`Instructions`](instructions.md) you configure, carry over without modification:

```swift
// Prompt the Core AI model exactly as you would the built-in models.
let meetingTranscript = ""
let response = try await session.respond(
    to: "Summarize the key points from this meeting transcript: \(meetingTranscript)."
)
```

To show output as the model produces it, use [`streamResponse(to:options:)`](languagemodelsession/streamresponse(to:options:).md) instead. For more information about prompting, tools, and structured output, see [`Generating content and performing tasks with Foundation Models`](generating-content-and-performing-tasks-with-foundation-models.md).

#### Handle Reasoning Output

Some open source models are reasoning models that produce intermediate chain-of-thought before their final answer. Core AI recognizes this content and routes it into the transcript as a [`Transcript.Entry.reasoning(_:)`](transcript/entry/reasoning(_:).md) segment rather than person-facing text. As a result, it doesn’t appear in the response content a person sees. Reviewing the reasoning helps you understand why the model produced a particular answer, which is useful when you debug prompts.

Whether a model reasons, and how much, depends on the model you export. Check model reasoning by inspecting its capabilities, as shown here:

```swift
if model.capabilities.contains(.reasoning) {
    // The model supports reasoning.
}
```

#### Profile the Models Runtime Performance

Core AI selects an inference engine for the device automatically, running the model on the GPU, CPU, or Apple Neural Engine, depending on how you export it. To measure load times, token counts, and per-request latency, use the Foundation Models instrument. For more information, see [`Analyzing the runtime performance of your Foundation Models app`](analyzing-the-runtime-performance-of-your-foundation-models-app.md).

## See Also

- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)
  Prevent repeated token processing by preserving the cached state across turns.
- [protocol LanguageModel](languagemodel.md)
  A protocol that you use to interface with a model.
- [struct LanguageModelCapabilities](languagemodelcapabilities.md)
  A set of capabilities that a language model provides.
- [protocol LanguageModelExecutor](languagemodelexecutor.md)
  A protocol that defines the interface for responding to session requests.
- [struct LanguageModelExecutorGenerationChannel](languagemodelexecutorgenerationchannel.md)
  A type you use to send model output deltas and updates to the framework.
- [struct LanguageModelExecutorGenerationRequest](languagemodelexecutorgenerationrequest.md)
  A type that contains the details for a generation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/running-a-core-ai-model-in-a-foundation-models-session)*