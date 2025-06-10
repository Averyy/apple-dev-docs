# alternatives

**Framework**: Speech  
**Kind**: property

All the alternative interpretations of the audio in this range. The interpretations are in descending order of likelihood.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
let alternatives: [AttributedString]
```

#### Discussion

The array will not be empty, but may contain an empty string, indicating an alternative where the audio has no transcription.

## See Also

- [var text: AttributedString](dictationtranscriber/result/text.md)
  The most likely interpretation of the audio in this range. Always equal to the first element of [`alternatives`](dictationtranscriber/result/alternatives.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/dictationtranscriber/result/alternatives)*