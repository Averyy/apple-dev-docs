# CMTIMERANGE_IS_INDEFINITE

**Framework**: Core Media  
**Kind**: macro  
**Role**: Macro

Returns a Boolean value that indicates whether a time range is indefinite.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```c
#define CMTIMERANGE_IS_INDEFINITE(range)
```

#### Return Value

`true` if `range` is indefinite; otherwise, `false`.

#### Discussion

An indefinite time range has either an indefinite start or an indefinite duration, or both.

## Parameters

- `range`: The time range to be tested for finiteness.

## See Also

### Inspecting Time Ranges
- [CMTIMERANGE_IS_EMPTY](./cmtimerange_is_empty.md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [CMTIMERANGE_IS_INVALID](./cmtimerange_is_invalid.md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [CMTIMERANGE_IS_VALID](./cmtimerange_is_valid.md)
  Returns a Boolean value that indicates whether a time range is valid.
- [func CMTimeRangeGetEnd(CMTimeRange) -> CMTime](./cmtimerangegetend%28_%29.md)
  Returns a time value that represents the end of a time range.
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetintersection%28_,otherrange%29.md)
  Returns a new time range with the time elements that are common between the input.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetunion%28_,otherrange%29.md)
  Returns a new time range with the time elements of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange_is_indefinite)*