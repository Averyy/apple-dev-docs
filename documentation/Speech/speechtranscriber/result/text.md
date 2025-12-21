# text

**Framework**: Speech  
**Kind**: property

The most likely interpretation of the audio in this range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var text: AttributedString { get }
```

#### Discussion

An empty string indicates that the audio contains no recognizable speech and, for results in the volatile range, that previous results for this range are revoked.

This value is the first (most likely) element of [`alternatives`](speechtranscriber/result/alternatives.md).

## See Also

- [let alternatives: [AttributedString]](speechtranscriber/result/alternatives.md)
  All the alternative interpretations of the audio in this range. The interpretations are in descending order of likelihood.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechtranscriber/result/text)*