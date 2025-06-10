# AVDepthData.Quality

**Framework**: AVFoundation  
**Kind**: enum

Values indicating the overall quality of a depth data map.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Quality
```

## Topics

### Depth Quality Values
- [AVDepthData.Quality.low](avdepthdata/quality/low.md)
  The depth map is a poor candidate for rendering high-quality depth effects or reconstructing a 3D scene.
- [AVDepthData.Quality.high](avdepthdata/quality/high.md)
  The depth map is a good candidate for rendering high-quality depth effects or reconstructing a 3D scene.
### Initializers
- [init?(rawValue: Int)](avdepthdata/quality/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isDepthDataFiltered: Bool](avdepthdata/isdepthdatafiltered.md)
  A Boolean value indicating whether the depth map contains temporally smoothed data.
- [var depthDataAccuracy: AVDepthData.Accuracy](avdepthdata/depthdataaccuracy.md)
  The general accuracy of depth data map values.
- [AVDepthData.Accuracy](avdepthdata/accuracy.md)
  Values indicating the general accuracy of a depth data map.
- [var depthDataQuality: AVDepthData.Quality](avdepthdata/depthdataquality.md)
  The overall quality of the depth map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/quality)*