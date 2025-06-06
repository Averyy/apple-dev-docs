# center

**Framework**: ARKit  
**Kind**: property

The center point of the plane relative to its anchor position.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var center: simd_float3 { get }
```

#### Discussion

When ARKit first detects a plane, the resulting [`ARPlaneAnchor`](arplaneanchor.md) object has a [`center`](arplaneanchor/center.md) value of `(0,0,0)`, indicating that the translation portion of the anchor’s [`transform`](aranchor/transform.md) value locates the plane’s center point.

As scene analysis and plane detection continues, ARKit may determine that a previously detected plane anchor is part of a larger real-world surface, increasing the [`extent`](arplaneanchor/extent.md) width and length values. The plane’s new boundaries may not be symmetric around its initial position, so the [`center`](arplaneanchor/center.md) point changes relative to the anchor’s (unchanged) [`transform`](aranchor/transform.md) matrix.

Although the type of this property is [`vector_float3`](https://developer.apple.com/documentation/simd/vector_float3), a plane anchor is always two-dimensional, and is always positioned in only the x and z directions relative to its [`transform`](aranchor/transform.md) position. (That is, the y-component of this vector is always zero.)

## See Also

- [var planeExtent: ARPlaneExtent](arplaneanchor/planeextent.md)
  The estimated width, length, and y-axis rotation of the detected plane.
- [class ARPlaneExtent](arplaneextent.md)
  The size and y-axis rotation of a detected plane.
- [var extent: simd_float3](arplaneanchor/extent.md)
  The estimated width and length of the detected plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arplaneanchor/center)*