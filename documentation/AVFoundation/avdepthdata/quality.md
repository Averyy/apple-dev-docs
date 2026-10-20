# AVDepthData.Quality

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum AVDepthDataQuality : NSInteger;
```

## Topics

### Depth quality values
- [AVDepthData.Quality.low](./quality/low.md)
  The depth map is a poor candidate for rendering high-quality depth effects or reconstructing a 3D scene.
- [AVDepthData.Quality.high](./quality/high.md)
  The depth map is a good candidate for rendering high-quality depth effects or reconstructing a 3D scene.
### Initializers
- [init?(rawValue: Int)](./quality/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Evaluating depth data
- [var isDepthDataFiltered: Bool](./isdepthdatafiltered.md)
  A Boolean value indicating whether the depth map contains temporally smoothed data.
- [var depthDataAccuracy: AVDepthData.Accuracy](./depthdataaccuracy.md)
  The general accuracy of depth data map values.
- [AVDepthData.Accuracy](./accuracy.md)
  Values indicating the general accuracy of a depth data map.
- [var depthDataQuality: AVDepthData.Quality](./depthdataquality.md)
  The overall quality of the depth map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/quality)*