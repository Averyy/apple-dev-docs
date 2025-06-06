# containsTimeRange(_:)

**Framework**: Core Media  
**Kind**: method

Returns a Boolean value that indicates whether the time range contains another time range.

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
func containsTimeRange(_ range: CMTimeRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if time range contains `range`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `range`: The time range to test for inclusion.

## See Also

- [func containsTime(CMTime) -> Bool](cmtimerange/containstime(_:).md)
  Returns a Boolean value that indicates whether the time range contains a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange/containstimerange(_:))*