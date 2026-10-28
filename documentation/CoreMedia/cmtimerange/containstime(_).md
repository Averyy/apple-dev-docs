# containsTime(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the time range contains a time.

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
func containsTime(_ time: CMTime) -> Bool
```

## Return Value

[`true`](../../Swift/true.md) if the time range contains the `time` value; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `time`: A time value to test for in the time range.

## See Also

### Finding Elements
- [func containsTimeRange(CMTimeRange) -> Bool](./containstimerange%28_%29.md)
  Returns a Boolean value that indicates whether the time range contains another time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange/containstime(_:))*