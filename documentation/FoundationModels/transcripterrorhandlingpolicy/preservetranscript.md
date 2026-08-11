# preserveTranscript

**Framework**: Foundation Models  
**Kind**: property

A policy that keeps the current transcript as is.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
static let preserveTranscript: TranscriptErrorHandlingPolicy
```

#### Discussion

The last entry of the transcript may be partially generated.

## See Also

- [static let revertTranscript: TranscriptErrorHandlingPolicy](transcripterrorhandlingpolicy/reverttranscript.md)
  A policy that reverts the transcript back to the state it was in just before the most recent request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/transcripterrorhandlingpolicy/preservetranscript)*