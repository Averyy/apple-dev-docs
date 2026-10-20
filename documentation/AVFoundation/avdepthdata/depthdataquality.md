# depthDataQuality

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The overall quality of the depth map.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var depthDataQuality: AVDepthData.Quality { get }
```

```objc
@property (readonly) AVDepthDataQuality depthDataQuality;
```

#### Discussion

A device typically generates depth data maps by comparing images and calculating disparity. If features are lacking in either input image, it may be difficult to find matching key points, resulting in a depth data map with substantial holes. These holes can be filled with depth data filtering, but still may produce a map of overall poor quality.

If a depth data map suffers from insufficient features, the capture system marks it as [`AVDepthData.Quality.low`](./quality/low.md) quality, indicating that the depth map is a poor candidate for rendering high-quality depth effects or reconstructing a 3D scene. A depth map with [`AVDepthData.Quality.high`](./quality/high.md) quality is feature-rich, contains a high level of detail, making it a good candidate for rendering high-quality depth effects or reconstructing a 3D scene.

## See Also

### Evaluating depth data
- [var isDepthDataFiltered: Bool](./isdepthdatafiltered.md)
  A Boolean value indicating whether the depth map contains temporally smoothed data.
- [var depthDataAccuracy: AVDepthData.Accuracy](./depthdataaccuracy.md)
  The general accuracy of depth data map values.
- [AVDepthData.Accuracy](./accuracy.md)
  Values indicating the general accuracy of a depth data map.
- [AVDepthData.Quality](./quality.md)
  Values indicating the overall quality of a depth data map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/depthdataquality)*