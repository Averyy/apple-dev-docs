# alternatives

**Framework**: Speech  
**Kind**: property

All the alternative interpretations of the audio in this range. The interpretations are in descending order of likelihood.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
let alternatives: [AttributedString]
```

#### Discussion

The array will not be empty, but may contain an empty string, indicating an alternative where the audio has no transcription.

To receive alternatives, set the [`SpeechTranscriber.ReportingOption.alternativeTranscriptions`](speechtranscriber/reportingoption/alternativetranscriptions.md) option.

## See Also

- [var text: AttributedString](speechtranscriber/result/text.md)
  The most likely interpretation of the audio in this range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/result/alternatives)*