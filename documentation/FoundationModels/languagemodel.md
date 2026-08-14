# LanguageModel

**Framework**: Foundation Models  
**Kind**: protocol

A protocol that you use to interface with a model.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
protocol LanguageModel : Sendable
```

## Mentions

- [Adding server-side intelligence with Private Cloud Compute](adding-server-side-intelligence-with-private-cloud-compute.md)
- [Running a Core AI model in a Foundation Models session](running-a-core-ai-model-in-a-foundation-models-session.md)

#### Overview

Implement this protocol to create a bridge between a model and the framework. The protocol describes the capabilities and the configuration for your model. An [`Executor`](languagemodel/executor.md) does the work of translating framework types into the types your platform expects, and streams results back through [`LanguageModelExecutorGenerationChannel`](languagemodelexecutorgenerationchannel.md). Because most of the work is done in the executor, keep the type that adopts this protocol intentionally light.

When your implementation is ready to adopt, distribute your solution with Swift Package Manager so developers can easily integrate it into their project. After they add your package, they simply initialize a [`LanguageModelSession`](languagemodelsession.md) with your model:

```swift
// Initialize a session with a custom server model.
let session = LanguageModelSession(model: MyCustomServerLanguageModel())
// Use the same API surface to prompt the model.
let response = try await session.respond(to: "Tell me a joke!")
```

## Topics

### Inspecting model capabilities
- [var capabilities: LanguageModelCapabilities](languagemodel/capabilities.md)
  The capabilities of this language model.
### Getting the executor configuration
- [var executorConfiguration: Self.Executor.Configuration](languagemodel/executorconfiguration.md)
  A configuration for an executor capable of running this model.
- [associatedtype Executor : LanguageModelExecutor](languagemodel/executor.md)

## Relationships

### Inherits From
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
### Conforming Types
- [PrivateCloudComputeLanguageModel](privatecloudcomputelanguagemodel.md)
- [SystemLanguageModel](systemlanguagemodel.md)

## See Also

- [Running a Core AI model in a Foundation Models session](running-a-core-ai-model-in-a-foundation-models-session.md)
  Send requests on device to an open source model you export with Core AI to get a consistent API experience.
- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)
  Prevent repeated token processing by preserving the cached state across turns.
- [struct LanguageModelCapabilities](languagemodelcapabilities.md)
  A set of capabilities that a language model provides.
- [protocol LanguageModelExecutor](languagemodelexecutor.md)
  A protocol that defines the interface for responding to session requests.
- [struct LanguageModelExecutorGenerationChannel](languagemodelexecutorgenerationchannel.md)
  A type you use to send model output deltas and updates to the framework.
- [struct LanguageModelExecutorGenerationRequest](languagemodelexecutorgenerationrequest.md)
  A type that contains the details for a generation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodel)*