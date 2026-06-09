# respond(to:model:streamingInto:)

**Framework**: Foundation Models  
**Kind**: method  
**Required**: Yes

Creates a response stream containing deltas.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func respond(to request: LanguageModelExecutorGenerationRequest, model: Self.Model, streamingInto channel: LanguageModelExecutorGenerationChannel) async throws
```

#### Discussion

> **Note**: If the model declares that it does not have a given capability via [`capabilities`](languagemodel/capabilities.md), then the system will automatically throw a `LanguageModelSession.GenerationError.unsupportedCapability` instead of invoking this method. You do not need to manually validate the request for any functionality captured by [`LanguageModelCapabilities`](languagemodelcapabilities.md).

## Parameters

- `request`: The generation request.
- `model`: The model instance for this request, providing live model state.
- `channel`: A channel used to send events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutor/respond(to:model:streaminginto:))*