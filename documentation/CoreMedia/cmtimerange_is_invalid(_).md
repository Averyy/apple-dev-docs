# CMTIMERANGE_IS_INVALID(_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a time range is invalid.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTIMERANGE_IS_INVALID(_ range: CMTimeRange) -> Bool
```

## Return Value

[`true`](../Swift/true.md) if `range` is invalid; otherwise, [`false`](../Swift/false.md).

## Parameters

- `range`: A time range.

## See Also

### Inspecting Time Ranges
- [func CMTIMERANGE_IS_EMPTY(CMTimeRange) -> Bool](./cmtimerange_is_empty%28_%29.md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [func CMTIMERANGE_IS_INDEFINITE(CMTimeRange) -> Bool](./cmtimerange_is_indefinite%28_%29.md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [func CMTIMERANGE_IS_VALID(CMTimeRange) -> Bool](./cmtimerange_is_valid%28_%29.md)
  Returns a Boolean value that indicates whether a time range is valid.
- [func CMTimeRangeGetEnd(CMTimeRange) -> CMTime](./cmtimerangegetend%28_%29.md)
  Returns a time value that represents the end of a time range.
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetintersection%28_,otherrange%29.md)
  Returns a new time range with the time elements that are common between the input.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](./cmtimerangegetunion%28_,otherrange%29.md)
  Returns a new time range with the time elements of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange_is_invalid(_:))*