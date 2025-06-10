# AVDepthData.Accuracy

**Framework**: AVFoundation  
**Kind**: enum

Values indicating the general accuracy of a depth data map.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum Accuracy
```

#### Overview

The accuracy of a depth data map is highly dependent on the camera calibration data used to generate it. If the camera’s focal length cannot be precisely determined at the time of capture, a scaling error in the z (depth) plane is introduced. If the camera’s optical center can’t be precisely determined at capture time, a principal point error is introduced, leading to an offset error in the disparity estimate.

These values report the accuracy of a map’s values with respect to its reported units.

## Topics

### Accuracy Values
- [AVDepthData.Accuracy.relative](avdepthdata/accuracy/relative.md)
  Values within the depth data map are usable for foreground/background separation, but are not absolutely accurate in the physical world.
- [AVDepthData.Accuracy.absolute](avdepthdata/accuracy/absolute.md)
  Values within the depth map are absolutely accurate within the physical world.
### Initializers
- [init?(rawValue: Int)](avdepthdata/accuracy/init(rawvalue:).md)

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
- [var depthDataQuality: AVDepthData.Quality](avdepthdata/depthdataquality.md)
  The overall quality of the depth map.
- [AVDepthData.Quality](avdepthdata/quality.md)
  Values indicating the overall quality of a depth data map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/accuracy)*