# matrix

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The projective transform’s underlying matrix.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var matrix: simd_double4x4
```

```c
simd_double4x4 matrix;
```

## See Also

### Inspecting a 3D projective transform’s properties
- [var inverse: ProjectiveTransform3D?](./inverse.md)
  The projective transform’s inverse.
- [var scaleComponent: Size3D](./scalecomponent.md)
  The scale component of the projective transform.
- [var translation: Vector3D](./translation.md)
  The translation component of the projective transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/matrix)*