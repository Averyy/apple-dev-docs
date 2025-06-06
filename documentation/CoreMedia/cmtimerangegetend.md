# CMTimeRangeGetEnd(_:)

**Framework**: Core Media  
**Kind**: func

Returns a time value that represents the end of a time range.

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
func CMTimeRangeGetEnd(_ range: CMTimeRange) -> CMTime
```

#### Return Value

A time structure.

## Parameters

- `range`: The time range from which to find the end of the time range.

## See Also

- [func CMTIMERANGE_IS_EMPTY(CMTimeRange) -> Bool](cmtimerange_is_empty(_:).md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [func CMTIMERANGE_IS_INDEFINITE(CMTimeRange) -> Bool](cmtimerange_is_indefinite(_:).md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [func CMTIMERANGE_IS_INVALID(CMTimeRange) -> Bool](cmtimerange_is_invalid(_:).md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [func CMTIMERANGE_IS_VALID(CMTimeRange) -> Bool](cmtimerange_is_valid(_:).md)
  Returns a Boolean value that indicates whether a time range is valid.
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetintersection(_:otherrange:).md)
  Returns a new time range with the time elements that are common between the input.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetunion(_:otherrange:).md)
  Returns a new time range with the time elements of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangegetend(_:))*