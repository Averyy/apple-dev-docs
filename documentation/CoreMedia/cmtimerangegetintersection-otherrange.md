# CMTimeRangeGetIntersection(_:otherRange:)

**Framework**: Core Media  
**Kind**: func

Returns a new time range with the time elements that are common between the input.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTimeRangeGetIntersection(_ range: CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange
```

#### Return Value

A time range that represents the largest intersection of the input.

## Parameters

- `range`: The first time range to intersect.
- `otherRange`: The second time range to intersect.

## See Also

- [func CMTIMERANGE_IS_EMPTY(CMTimeRange) -> Bool](cmtimerange_is_empty(_:).md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [func CMTIMERANGE_IS_INDEFINITE(CMTimeRange) -> Bool](cmtimerange_is_indefinite(_:).md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [func CMTIMERANGE_IS_INVALID(CMTimeRange) -> Bool](cmtimerange_is_invalid(_:).md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [func CMTIMERANGE_IS_VALID(CMTimeRange) -> Bool](cmtimerange_is_valid(_:).md)
  Returns a Boolean value that indicates whether a time range is valid.
- [func CMTimeRangeGetEnd(CMTimeRange) -> CMTime](cmtimerangegetend(_:).md)
  Returns a time value that represents the end of a time range.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetunion(_:otherrange:).md)
  Returns a new time range with the time elements of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangegetintersection(_:otherrange:))*