# rangeOfAudioTimeRangeAttributes(intersecting:)

**Framework**: Foundation  
**Kind**: method

Returns the range of indices of the receiver that are part of given time range.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func rangeOfAudioTimeRangeAttributes(intersecting timeRange: CMTimeRange) -> Range<AttributedString.Index>?
```

#### Discussion

The method compares the given time range against the [`AttributeScopes.SpeechAttributes.TimeRangeAttribute`](attributescopes/speechattributes/timerangeattribute.md) attributes of the receiver.

You can use this method to help update an attributed string tracking the volatile or finalized results of a `Transcriber` module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/rangeofaudiotimerangeattributes(intersecting:))*