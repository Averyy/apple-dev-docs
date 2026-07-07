# LanguageModelExecutorGenerationChannel

**Framework**: Foundation Models  
**Kind**: struct

A type you use to send model output deltas and updates to the framework.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct LanguageModelExecutorGenerationChannel
```

#### Overview

Use this to stream text as your model produces it. You can also use the channel to report metadata and usage that helps developers track what’s happening, like when you want to report model details and token usage updates:

```swift
func respond(
    to request: LanguageModelExecutorGenerationRequest,
    model: MyLanguageModel,
    streamingInto channel: LanguageModelExecutorGenerationChannel
) async throws {

    let entryID = UUID().uuidString

    // Calculate your total and cached tokens counts for the input.
    let totalTokens = 0
    let cachedTokens = 0

    // Send model identification.
    await channel.send(.response(entryID: entryID, action: .updateMetadata([
        "modelID": "my-model-2026-06-08",
        "requestID": request.id.uuidString
    ])))

    // Report prompt token usage upfront.
    await channel.send(.response(
        entryID: entryID,
        action: .updateUsage(
            input: .init(
                totalTokenCount: totalTokens,
                cachedTokenCount: cachedTokens
            ),
            output: .init(
                totalTokenCount: 0,
                reasoningTokenCount: 0
            )
        )
    ))
}
```

## Topics

### Creating a channel instance
- [init()](languagemodelexecutorgenerationchannel/init.md)
  Creates a new generation channel instance.
### Sending an event
- [func send(LanguageModelExecutorGenerationChannel.Event) async](languagemodelexecutorgenerationchannel/send(_:).md)
  Sends a generation event on the channel.
- [LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event.md)
  A generation event sent on a [`LanguageModelExecutorGenerationChannel`](languagemodelexecutorgenerationchannel.md).
### Accessing the event types
- [LanguageModelExecutorGenerationChannel.Metadata](languagemodelexecutorgenerationchannel/metadata.md)
  Snapshot of an entry’s metadata dictionary.
- [LanguageModelExecutorGenerationChannel.Reasoning](languagemodelexecutorgenerationchannel/reasoning.md)
  A reasoning event.
- [LanguageModelExecutorGenerationChannel.ReasoningSignature](languagemodelexecutorgenerationchannel/reasoningsignature.md)
  Payload for a reasoning entry’s signature update.
- [LanguageModelExecutorGenerationChannel.TextFragment](languagemodelexecutorgenerationchannel/textfragment.md)
  Append text to a streaming entry’s current text segment. Used by both `Response/Action/appendText(_:)` and `Reasoning/Action/appendText(_:)`.
- [LanguageModelExecutorGenerationChannel.TextSegmentReplacement](languagemodelexecutorgenerationchannel/textsegmentreplacement.md)
  Replace a streaming entry’s current text segment with `content`.
- [LanguageModelExecutorGenerationChannel.Response](languagemodelexecutorgenerationchannel/response.md)
  A model-generated response event: text, segment replacements, citations, advisories, custom segments, metadata, or usage.
- [LanguageModelExecutorGenerationChannel.ToolCalls](languagemodelexecutorgenerationchannel/toolcalls.md)
  A tool-call lifecycle event, including per-call argument streaming, reasoning, metadata, usage, or retraction.
- [LanguageModelExecutorGenerationChannel.Usage](languagemodelexecutorgenerationchannel/usage.md)
  Snapshot of an entry’s token totals.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)
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
- [struct LanguageModelExecutorGenerationRequest](languagemodelexecutorgenerationrequest.md)
  A type that contains the details for a generation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel)*