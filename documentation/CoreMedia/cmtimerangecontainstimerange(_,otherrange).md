# CMTimeRangeContainsTimeRange(_:otherRange:)

**Framework**: Core Media  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether a time range contains another time range.

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
func CMTimeRangeContainsTimeRange(_ range: CMTimeRange, otherRange: CMTimeRange) -> Bool
```

```c
extern Boolean CMTimeRangeContainsTimeRange(CMTimeRange range, CMTimeRange otherRange);
```

## Return Value

[`true`](../Swift/true.md) if `range1` contains `range2`; otherwise, [`false`](../Swift/false.md).

## Parameters

- `range`: The first time range to compare.
- `otherRange`: The second time range to test for inclusion.

## See Also

### Comparing Time Ranges
- [func CMTimeRangeEqual(CMTimeRange, CMTimeRange) -> Bool](./cmtimerangeequal%28_,_%29.md)
  Returns a Boolean value that indicates whether two time ranges are equal.
- [func CMTimeRangeContainsTime(CMTimeRange, time: CMTime) -> Bool](./cmtimerangecontainstime%28_,time%29.md)
  Returns a Boolean value that indicates whether a time range contains a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangecontainstimerange(_:otherrange:))*