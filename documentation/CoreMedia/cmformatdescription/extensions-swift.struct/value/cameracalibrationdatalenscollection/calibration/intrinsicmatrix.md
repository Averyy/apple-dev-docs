# intrinsicMatrix

**Framework**: Core Media  
**Kind**: property

The 3x3 camera intrinsic matrix for camera calibration.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var intrinsicMatrix: simd_float3x3
```

#### Discussion

It has the following contents: | fx | s  | cx | |  0 | fy | cy | |  0 |  0 |  1 | fx and fy are the focal length in pixels. For square pixels, they will have the same value. cx and cy are the coordinates of the principal point. The origin is the upper left of the frame. s is an optional skew factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmformatdescription/extensions-swift.struct/value/cameracalibrationdatalenscollection/calibration/intrinsicmatrix)*