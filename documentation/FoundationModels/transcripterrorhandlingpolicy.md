# TranscriptErrorHandlingPolicy

**Framework**: Foundation Models  
**Kind**: struct

Options for controlling how a language model session manages the transcript when errors occur.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct TranscriptErrorHandlingPolicy
```

## Topics

### Error handling policies
- [static let preserveTranscript: TranscriptErrorHandlingPolicy](transcripterrorhandlingpolicy/preservetranscript.md)
  A policy that keeps the current transcript as is.
- [static let revertTranscript: TranscriptErrorHandlingPolicy](transcripterrorhandlingpolicy/reverttranscript.md)
  A policy that reverts the transcript back to the state it was in just before the most recent request.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var transcriptErrorHandlingPolicy: TranscriptErrorHandlingPolicy?](languagemodelsession/transcripterrorhandlingpolicy.md)
  The session’s policy for managing the transcript when errors occur.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcripterrorhandlingpolicy)*