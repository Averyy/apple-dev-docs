# isFilteringEnabled

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that determines whether the depth data output should filter depth data to smooth out noise and fill invalid values.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var isFilteringEnabled: Bool { get set }
```

#### Discussion

When this value is [`true`](https://developer.apple.com/documentation/swift/true) (the default), the capture output smooths noise and fills in missing or invalid values (caused by low light or lens occlusion) in depth data maps by temporally interpolating between previous and subsequent frames of captured depth data.

Filtering depth data makes it more useful for applying visual effects to a companion image, but alters the data such that it may no longer be suitable for computer vision tasks. (In an unfiltered depth map, missing values are represented as `NaN`.)

## See Also

- [var alwaysDiscardsLateDepthData: Bool](avcapturedepthdataoutput/alwaysdiscardslatedepthdata.md)
  A Boolean value that determines whether the capture output should discard any depth data that is not processed before the next depth data is captured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturedepthdataoutput/isfilteringenabled)*