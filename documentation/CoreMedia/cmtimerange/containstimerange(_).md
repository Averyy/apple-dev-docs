# containsTimeRange(_:)

**Framework**: Core Media  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the time range contains another time range.

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
func containsTimeRange(_ range: CMTimeRange) -> Bool
```

#### Return Value

[`true`](../../Swift/true.md) if time range contains `range`; otherwise, [`false`](../../Swift/false.md).

## Parameters

- `range`: The time range to test for inclusion.

## See Also

### Finding Elements
- [func containsTime(CMTime) -> Bool](./containstime%28_%29.md)
  Returns a Boolean value that indicates whether the time range contains a time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmtimerange/containstimerange(_:))*