# LanguageModelSession.Error

**Framework**: Foundation Models  
**Kind**: enum  
**Role**: Enumeration

A failure caused by incorrect use of a language model session.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
enum Error
```

#### Overview

> **Note**: If your app deploys to iOS 26, macOS 26, or visionOS 26, where this error is unavailable, use an availability check and fall back to [`LanguageModelSession.GenerationError`](./generationerror.md):
>
> ```swift
> do {
>     let response = try await session.respond(to: prompt)
> } catch {
>     if #available(iOS 27.0, macOS 27.0, visionOS 27.0, *),
>         let error = error as? LanguageModelSession.Error
>     {
>         // Handle the error.
>     } else if case .concurrentRequests = error as? LanguageModelSession.GenerationError {
>         // Handle the deprecated error.
>     }
> }
> ```

## Topics

### Getting the session errors
- [LanguageModelSession.Error.concurrentRequests](./error/concurrentrequests.md)
  The session received multiple concurrent requests.
- [LanguageModelSession.Error.transcriptMutationWhileResponding](./error/transcriptmutationwhileresponding.md)
  A request mutated the session’s transcript while it was in progress.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Error](../../Swift/error.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [LanguageModelSession.ToolCallError](./toolcallerror.md)
  An error that occurs while a language model is calling a tool.
- [LanguageModelSession.GenerationError](./generationerror.md)
  An error that may occur while generating a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/error)*