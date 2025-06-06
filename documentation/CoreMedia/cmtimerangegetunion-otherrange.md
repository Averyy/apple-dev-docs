# CMTimeRangeGetUnion(_:otherRange:)

**Framework**: Core Media  
**Kind**: func

Returns a new time range with the time elements of the input.

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
func CMTimeRangeGetUnion(_ range: CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange
```

#### Return Value

A time range with the unique time elements of the input.

#### Discussion

The return value contains the smallest range that includes all times that are in either range.

## Parameters

- `range`: The first time range.
- `otherRange`: The second time range.

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
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetintersection(_:otherrange:).md)
  Returns a new time range with the time elements that are common between the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangegetunion(_:otherrange:))*