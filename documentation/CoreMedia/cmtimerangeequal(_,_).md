# CMTimeRangeEqual(_:_:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether two time ranges are equal.

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
func CMTimeRangeEqual(_ range1: CMTimeRange, _ range2: CMTimeRange) -> Bool
```

```c
extern Boolean CMTimeRangeEqual(CMTimeRange range1, CMTimeRange range2);
```

## Return Value

[`true`](../Swift/true.md) if the two time ranges are equal; otherwise, [`false`](../Swift/false.md).

## Parameters

- `range1`: The first time range to compare.
- `range2`: The second time range to compare.

## See Also

### Comparing Time Ranges
- [func CMTimeRangeContainsTime(CMTimeRange, time: CMTime) -> Bool](./cmtimerangecontainstime%28_,time%29.md)
  Returns a Boolean value that indicates whether a time range contains a time.
- [func CMTimeRangeContainsTimeRange(CMTimeRange, otherRange: CMTimeRange) -> Bool](./cmtimerangecontainstimerange%28_,otherrange%29.md)
  Returns a Boolean value that indicates whether a time range contains another time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangeequal(_:_:))*