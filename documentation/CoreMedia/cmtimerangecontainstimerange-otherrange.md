# CMTimeRangeContainsTimeRange(_:otherRange:)

**Framework**: Core Media  
**Kind**: func

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

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `range1` contains `range2`; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `range`: The first time range to compare.
- `otherRange`: The second time range to test for inclusion.

## See Also

- [func CMTimeRangeEqual(CMTimeRange, CMTimeRange) -> Bool](cmtimerangeequal(_:_:).md)
  Returns a Boolean value that indicates whether two time ranges are equal.
- [func CMTimeRangeContainsTime(CMTimeRange, time: CMTime) -> Bool](cmtimerangecontainstime(_:time:).md)
  Returns a Boolean value that indicates whether a time range contains a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangecontainstimerange(_:otherrange:))*