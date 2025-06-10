# DictationTranscriber.Result

**Framework**: Speech  
**Kind**: struct

A phrase or passage of transcribed speech. The phrases are sent in order.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Result
```

#### Overview

If the transcriber is configured to send volatile results, each phrase is sent one or more times as the interpretation gets better and better until it is finalized.

## Topics

### Instance Properties
- [let alternatives: [AttributedString]](dictationtranscriber/result/alternatives.md)
  All the alternative interpretations of the audio in this range. The interpretations are in descending order of likelihood.
- [var text: AttributedString](dictationtranscriber/result/text.md)
  The most likely interpretation of the audio in this range. Always equal to the first element of [`alternatives`](dictationtranscriber/result/alternatives.md).

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SpeechModuleResult](speechmoduleresult.md)

## See Also

- [DictationTranscriber.ContentHint](dictationtranscriber/contenthint.md)
  Expected characteristics of the spoken audio content and its delivery.
- [DictationTranscriber.Preset](dictationtranscriber/preset.md)
  Predefined transcriber configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/result)*