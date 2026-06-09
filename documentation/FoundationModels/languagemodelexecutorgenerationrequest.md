# LanguageModelExecutorGenerationRequest

**Framework**: Foundation Models  
**Kind**: struct

A type that contains the details for a generation request.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct LanguageModelExecutorGenerationRequest
```

#### Overview

A generation request is the input payload that [`respond(to:model:streamingInto:)`](languagemodelexecutor/respond(to:model:streaminginto:).md) handles. It bundles everything the executor needs to translate a framework call into a backend request, like the conversation so far, what tools are available, and so on.

## Topics

### Creating a generation request
- [init(id: UUID, transcript: Transcript, enabledTools: [Transcript.ToolDefinition], schema: GenerationSchema?, generationOptions: GenerationOptions, contextOptions: ContextOptions, metadata: [String : any Sendable & Codable & Equatable])](languagemodelexecutorgenerationrequest/init(id:transcript:enabledtools:schema:generationoptions:contextoptions:metadata:).md)
  Creates a new generation request.
### Configuring a generation request
- [var id: UUID](languagemodelexecutorgenerationrequest/id.md)
  A request id for logging and tracing purposes
- [var metadata: [String : any Sendable & Codable & Equatable]](languagemodelexecutorgenerationrequest/metadata.md)
  Metadata to attach to the request
- [var contextOptions: ContextOptions](languagemodelexecutorgenerationrequest/contextoptions.md)
  Settings that configure how the model is prompted
- [var enabledToolDefinitions: [Transcript.ToolDefinition]](languagemodelexecutorgenerationrequest/enabledtooldefinitions.md)
  The subset tool definitions that the model is allowed to call
- [var generationOptions: GenerationOptions](languagemodelexecutorgenerationrequest/generationoptions.md)
  Generation options that control sampling behavior
- [var schema: GenerationSchema?](languagemodelexecutorgenerationrequest/schema.md)
  An optional schema dictating the required output format
- [var transcript: Transcript](languagemodelexecutorgenerationrequest/transcript.md)
  A transcript to generate the next entry for

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationrequest)*