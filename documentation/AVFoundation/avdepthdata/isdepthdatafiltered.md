# isDepthDataFiltered

**Framework**: AVFoundation  
**Kind**: property

A Boolean value indicating whether the depth map contains temporally smoothed data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isDepthDataFiltered: Bool { get }
```

#### Discussion

The capture system can smooth noise and fill in missing values (caused by low light or lens occlusion) in depth data maps by temporally interpolating between previous and subsequent frames of captured depth data. Use the [`AVCaptureDepthDataOutput`](avcapturedepthdataoutput.md) [`isFilteringEnabled`](avcapturedepthdataoutput/isfilteringenabled.md) property to control filtering for streaming depth capture, or the [`AVCapturePhotoSettings`](avcapturephotosettings.md) [`isDepthDataFiltered`](avdepthdata/isdepthdatafiltered.md) property to control filtering for depth data captured alongside photo capture.

Filtering depth data makes it more useful for applying visual effects to a companion image, but alters the data such that it may no longer be suitable for computer vision tasks. (In an unfiltered depth map, missing values are represented as `NaN`.)

## See Also

- [var depthDataAccuracy: AVDepthData.Accuracy](avdepthdata/depthdataaccuracy.md)
  The general accuracy of depth data map values.
- [AVDepthData.Accuracy](avdepthdata/accuracy.md)
  Values indicating the general accuracy of a depth data map.
- [var depthDataQuality: AVDepthData.Quality](avdepthdata/depthdataquality.md)
  The overall quality of the depth map.
- [AVDepthData.Quality](avdepthdata/quality.md)
  Values indicating the overall quality of a depth data map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/isdepthdatafiltered)*