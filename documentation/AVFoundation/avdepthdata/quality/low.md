# AVDepthData.Quality.low

**Framework**: AVFoundation  
**Kind**: case

The depth map is a poor candidate for rendering high-quality depth effects or reconstructing a 3D scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case low
```

#### Discussion

Low quality occurs when the process generating the depth map (such as inference of depth from disparity on a device with dual cameras) cannot find enough distinct key points in the input images, resulting in a large number of invalid depth values in the (pre-filtered) map.

## See Also

- [AVDepthData.Quality.high](avdepthdata/quality/high.md)
  The depth map is a good candidate for rendering high-quality depth effects or reconstructing a 3D scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avdepthdata/quality/low)*