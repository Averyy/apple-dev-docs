# rangeOfAudioTimeRangeAttributes(intersecting:)

**Framework**: Foundation  
**Kind**: method

Returns the range of the attributed string that is within the given time range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func rangeOfAudioTimeRangeAttributes(intersecting timeRange: CMTimeRange) -> Range<AttributedString.Index>?
```

#### Return Value

The range of the string’s intersecting text, or `nil` if the string has no intersecting text.

#### Discussion

The method compares the given time range against the [`AttributeScopes.SpeechAttributes.TimeRangeAttribute`](attributescopes/speechattributes/timerangeattribute.md) attributes of the string. The time ranges in the string should be in ascending order, but not necessarily contiguous, and the string can include runs without a time range attribute.

You can use this method to help update an attributed string that tracks the volatile or finalized results of a `SpeechTranscriber` or `DictationTranscriber` module.

## Parameters

- `timeRange`: An audio time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/rangeofaudiotimerangeattributes(intersecting:))*