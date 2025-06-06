# CMTIMERANGE_IS_VALID(_:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether a time range is valid.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst ?+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func CMTIMERANGE_IS_VALID(_ range: CMTimeRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `range` is valid; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `range`: The time range.

## See Also

- [func CMTIMERANGE_IS_EMPTY(CMTimeRange) -> Bool](cmtimerange_is_empty(_:).md)
  Returns a Boolean value that indicates whether a time range has a duration of zero.
- [func CMTIMERANGE_IS_INDEFINITE(CMTimeRange) -> Bool](cmtimerange_is_indefinite(_:).md)
  Returns a Boolean value that indicates whether a time range is indefinite.
- [func CMTIMERANGE_IS_INVALID(CMTimeRange) -> Bool](cmtimerange_is_invalid(_:).md)
  Returns a Boolean value that indicates whether a time range is invalid.
- [func CMTimeRangeGetEnd(CMTimeRange) -> CMTime](cmtimerangegetend(_:).md)
  Returns a time value that represents the end of a time range.
- [func CMTimeRangeGetIntersection(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetintersection(_:otherrange:).md)
  Returns a new time range with the time elements that are common between the input.
- [func CMTimeRangeGetUnion(CMTimeRange, otherRange: CMTimeRange) -> CMTimeRange](cmtimerangegetunion(_:otherrange:).md)
  Returns a new time range with the time elements of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange_is_valid(_:))*