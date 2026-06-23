# LanguageModelSession.Error

**Framework**: Foundation Models  
**Kind**: enum

A failure caused by incorrect use of a language model session.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
enum Error
```

## Topics

### Getting the session errors
- [LanguageModelSession.Error.concurrentRequests](languagemodelsession/error/concurrentrequests.md)
  Multiple requests were made to the session concurrently.
- [LanguageModelSession.Error.transcriptMutationWhileResponding](languagemodelsession/error/transcriptmutationwhileresponding.md)
  The session’s transcript was mutated while a request was in progress.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Escapable](../Swift/Escapable.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LanguageModelSession.ToolCallError](languagemodelsession/toolcallerror.md)
  An error that occurs while a language model is calling a tool.
- [LanguageModelSession.GenerationError](languagemodelsession/generationerror.md)
  An error that may occur while generating a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/error)*