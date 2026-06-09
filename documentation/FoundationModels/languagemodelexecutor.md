# LanguageModelExecutor

**Framework**: Foundation Models  
**Kind**: protocol

A protocol that defines the interface for responding to session requests.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol LanguageModelExecutor : Sendable
```

#### Overview

An executor is the bridge between the framework types and the system that actually generates the tokens, like a server API or a local inference engine. A [`LanguageModel`](languagemodel.md) pairs with exactly one executor type and the framework instantiates the executor from the [`Configuration`](languagemodelexecutor/configuration.md) the model provides.

Every request can include preferences that control generation:

- **[`GenerationOptions`](generationoptions.md)**: Configures the sampling strategy, temperature, and maximum response length.
- **[`ContextOptions`](contextoptions.md)**: Configures the prompting behavior and thinking effort.

When the framework calls [`respond(to:model:streamingInto:)`](languagemodelexecutor/respond(to:model:streaminginto:).md), handle converting the transcript into the format your model expects and applying generation options. In some cases, you may need to fall back when your model can’t do exactly what was asked, like using temperature to approximate sampling options:

```swift
// Parse generation and context options
func respond(
    to request: LanguageModelExecutorGenerationRequest,
    model: MyLanguageModel,
    streamingInto channel: LanguageModelExecutorGenerationChannel
) async throws {

    // The request includes a sampling set to `greedy`, but your
    // model only uses temperature.
    if request.generationOptions.samplingMode == .greedy {
        // Use the temperature of `0` to approximate the intention.
    }

    // ...
}
```

Use [`LanguageModelExecutorGenerationChannel`](languagemodelexecutorgenerationchannel.md) to stream incremental events back as generation progresses. You don’t return a value or close the channel explicitly. The channel finishes when the method returns or when an error is thrown.

## Topics

### Creating an executor
- [init(configuration: Self.Configuration) throws](languagemodelexecutor/init(configuration:).md)
  Creates an executor from a configuration.
- [associatedtype Configuration : Hashable, Sendable](languagemodelexecutor/configuration.md)
### Prewarming the model
- [func prewarm(model: Self.Model, transcript: Transcript)](languagemodelexecutor/prewarm(model:transcript:).md)
  The system invokes this method in response to prewarming the session and provides an opportunity to load assets into memory or pre-fill caches.
- [associatedtype Model : LanguageModel](languagemodelexecutor/model.md)
  The model type this executor processes requests for.
### Handling the response
- [func respond(to: LanguageModelExecutorGenerationRequest, model: Self.Model, streamingInto: LanguageModelExecutorGenerationChannel) async throws](languagemodelexecutor/respond(to:model:streaminginto:).md)
  Creates a response stream containing deltas.

## Relationships

### Inherits From
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)
  Prevent repeated token processing by preserving the cached state across turns.
- [protocol LanguageModel](languagemodel.md)
  A protocol that you use to interface with a model.
- [struct LanguageModelCapabilities](languagemodelcapabilities.md)
  A set of capabilities that a language model provides.
- [struct LanguageModelExecutorGenerationChannel](languagemodelexecutorgenerationchannel.md)
  A type you use to send model output deltas and updates to the framework.
- [struct LanguageModelExecutorGenerationRequest](languagemodelexecutorgenerationrequest.md)
  A type that contains the details for a generation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutor)*