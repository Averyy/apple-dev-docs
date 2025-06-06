# leftEyeTransform

**Framework**: ARKit  
**Kind**: property

A transform matrix indicating the position and orientation of the face’s left eye.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var leftEyeTransform: simd_float4x4 { get }
```

#### Discussion

The translation aspect of this matrix indicates the position of the center of the eyeball, relative to the position represented by the anchor’s [`transform`](aranchor/transform.md). The positive z-axis points from the center of the eyeball in the direction of the pupil.

Rotational aspects of the matrix indicate the orientation of the eyeball—for example, a rotation about the x-axis directs the pupil upward or downward. The eye does not rotate about the z-axis.

![Diagram showing the coordinate axis origin defined by the leftEyeTransform, representing both the position and rotation of the eye relative to the face anchor.](https://docs-assets.developer.apple.com/published/47eb6b76104af8170145e3fa9a15abcf/media-3001546%402x.png)

## See Also

- [var rightEyeTransform: simd_float4x4](arfaceanchor/righteyetransform.md)
  A transform matrix indicating the position and orientation of the face’s right eye.
- [var lookAtPoint: simd_float3](arfaceanchor/lookatpoint.md)
  A position in face coordinate space estimating the direction of the face’s gaze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arfaceanchor/lefteyetransform)*