# alternativeSubstrings

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property

An array of alternate interpretations of the utterance in the transcription segment.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var alternativeSubstrings: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * alternativeSubstrings;
```

## See Also

### Transcribing the segment
- [var substring: String](./substring.md)
  The string representation of the utterance in the transcription segment.
- [var substringRange: NSRange](./substringrange.md)
  The range information for the transcription segment’s substring, relative to the overall transcription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sftranscriptionsegment/alternativesubstrings)*