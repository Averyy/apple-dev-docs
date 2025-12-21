# CMTimeRangeContainsTime(_:time:)

**Framework**: Core Media  
**Kind**: func

Returns a Boolean value that indicates whether a time range contains a time.

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
func CMTimeRangeContainsTime(_ range: CMTimeRange, time: CMTime) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `range` contains the `time` value; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `range`: A time range.
- `time`: A time value to test for in the time range.

## See Also

- [func CMTimeRangeEqual(CMTimeRange, CMTimeRange) -> Bool](cmtimerangeequal(_:_:).md)
  Returns a Boolean value that indicates whether two time ranges are equal.
- [func CMTimeRangeContainsTimeRange(CMTimeRange, otherRange: CMTimeRange) -> Bool](cmtimerangecontainstimerange(_:otherrange:).md)
  Returns a Boolean value that indicates whether a time range contains another time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerangecontainstime(_:time:))*