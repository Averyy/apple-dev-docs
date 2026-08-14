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
  The session received multiple concurrent requests.
- [LanguageModelSession.Error.transcriptMutationWhileResponding](languagemodelsession/error/transcriptmutationwhileresponding.md)
  A request mutated the session’s transcript while it was in progress.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Error](../swift/error.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [LanguageModelSession.ToolCallError](languagemodelsession/toolcallerror.md)
  An error that occurs while a language model is calling a tool.
- [LanguageModelSession.GenerationError](languagemodelsession/generationerror.md)
  An error that may occur while generating a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/error)*