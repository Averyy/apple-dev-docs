# substringRange

**Framework**: Speech  
**Kind**: property

The range information for the transcription segment’s substring, relative to the overall transcription.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var substringRange: NSRange { get }
```

#### Discussion

Use the range information to find the position of the segment within the [`formattedString`](sftranscription/formattedstring.md) property of the [`SFTranscription`](sftranscription.md) object containing this segment.

## See Also

- [var substring: String](sftranscriptionsegment/substring.md)
  The string representation of the utterance in the transcription segment.
- [var alternativeSubstrings: [String]](sftranscriptionsegment/alternativesubstrings.md)
  An array of alternate interpretations of the utterance in the transcription segment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sftranscriptionsegment/substringrange)*