# containsTime(_:)

**Framework**: Core Media  
**Kind**: method

Returns a Boolean value that indicates whether the time range contains a time.

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
func containsTime(_ time: CMTime) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the time range contains the `time` value; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `time`: A time value to test for in the time range.

## See Also

- [func containsTimeRange(CMTimeRange) -> Bool](cmtimerange/containstimerange(_:).md)
  Returns a Boolean value that indicates whether the time range contains another time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange/containstime(_:))*