# rotation(to:)

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns the rotation around the origin from the first point to the second point.

**Availability**:
- iOS 16.0+ - Deprecated in 17.0
- iPadOS 16.0+ - Deprecated in 17.0
- Mac Catalyst 16.0+ - Deprecated in 17.0
- macOS 13.0+ - Deprecated in 14.0
- tvOS 16.0+ - Deprecated in 17.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 9.0+ - Deprecated in 10.0

> **Deprecated**: Use `SPVector3DRotationToVector`.

## Declaration

```swift
func rotation(to other: Point3D) -> Rotation3D
```

```c
static SPRotation3D SPPoint3DRotationToPoint(SPPoint3D point, SPPoint3D other);
```

#### Return Value

The rotation between two points.

## Parameters

- `other`: The second point that the function computes the rotation to.

## See Also

### Deprecated symbols
- [var origin: Point3D](./origin.md)
- [var simd: simd_double3](./simd.md)
  A simd three-element vector that contains the x-, y-, and z-coordinate values.
- [SPPoint3DGetOrigin](../sppoint3dgetorigin.md)
  The location of the point.
- [SPPoint3DTranslate](../sppoint3dtranslate-8xo6b.md)
  Returns a point with an origin that’s offset by the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/point3d/rotation(to:))*