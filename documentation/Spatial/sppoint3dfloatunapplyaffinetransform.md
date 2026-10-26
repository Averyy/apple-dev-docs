# SPPoint3DFloatUnapplyAffineTransform

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```c
static SPPoint3DFloat SPPoint3DFloatUnapplyAffineTransform(SPPoint3DFloat point, SPAffineTransform3DFloat transform);
```

#### Return Value

The transformed point.

#### Discussion

Returns a point that’s transformed by the inverse of the specified affine transform.

## Parameters

- `point`: The source point.
- `transform`: The affine transform that the function unapplies to the point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/sppoint3dfloatunapplyaffinetransform)*