# CMTimeRangeGetEnd(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

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

```c
extern CMTime CMTimeRangeGetEnd(CMTimeRange range);
```

## Return Value

A time structure.

## Parameters

- `range`: The time range from which to find the end of the time range.

## See Also

### Inspecting Time Ranges
- [func CMTIMERANGE_IS_EMPTY(CMTimeRange) -> Bool](./cmtimerange_is_empty%28_%29.md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [func CMTIMERANGE_IS_INDEFINITE(CMTimeRange) -> Bool](./cmtimerange_is_indefinite%28_%29.md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [func CMTIMERANGE_IS_INVALID(CMTimeRange) -> Bool](./cmtimerange_is_invalid%28_%29.md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [func CMTIMERANGE_IS_VALID(CMTimeRange) -> Bool](./cmtimerange_is_valid%28_%29.md)
  Returns a Boolean value that indicates whether a time range is valid.
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetintersection%28_,otherrange%29.md)
  Returns a new time range with the time elements that are common between the input.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetunion%28_,otherrange%29.md)
  Returns a new time range with the time elements of the input.
- [CMTIMERANGE_IS_EMPTY](./cmtimerange_is_empty.md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [CMTIMERANGE_IS_INDEFINITE](./cmtimerange_is_indefinite.md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [CMTIMERANGE_IS_INVALID](./cmtimerange_is_invalid.md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [CMTIMERANGE_IS_VALID](./cmtimerange_is_valid.md)
  Returns a Boolean value that indicates whether a time range is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangegetend(_:))*