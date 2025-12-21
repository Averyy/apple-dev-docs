# rangeOfAudioTimeRangeAttributes(intersecting:)

**Framework**: Foundation  
**Kind**: method

Returns the range of indices of the receiver that are part of given time range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func rangeOfAudioTimeRangeAttributes(intersecting timeRange: CMTimeRange) -> Range<AttributedString.Index>?
```

#### Discussion

The method compares the given time range against the [`AttributeScopes.SpeechAttributes.TimeRangeAttribute`](attributescopes/speechattributes/timerangeattribute.md) attributes of the receiver.

You can use this method to help update an attributed string that tracks the volatile or finalized results of a `SpeechTranscriber` or `DictationTranscriber` module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/rangeofaudiotimerangeattributes(intersecting:))*