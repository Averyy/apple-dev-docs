# init(a:b:c:d:tx:ty:vx:vy:v:)

**Framework**: Accelerate  
**Kind**: init

Creates a projective-transformation structure from the specified single-precision values.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
init(a: Float, b: Float, c: Float, d: Float, tx: Float, ty: Float, vx: Float, vy: Float, v: Float)
```

## Parameters

- `a`: The top-left cell in the 3 x 3 transformation matrix.
- `b`: The top-middle cell in the 3 x 3 transformation matrix.
- `c`: The middle-left cell in the 3 x 3 transformation matrix.
- `d`: The middle-middle cell in the 3 x 3 transformation matrix.
- `tx`: The x-coordinate translation.
- `ty`: The y-coordinate translation.
- `vx`: The x-component of the projective vector.
- `vy`: The y-component of the projective vector.
- `v`: The homogeneous scale factor.

## See Also

- [init()](vimage_perpsectivetransform/init.md)
  Creates a projective-transformation structure.
- [init?(source: vImage_PerpsectiveTransform.QuadrilateralPoints, destination: vImage_PerpsectiveTransform.QuadrilateralPoints)](vimage_perpsectivetransform/init(source:destination:).md)
  Returns a projective-transformation structure that defines the mapping between a source quadrilateral and a destination quadrilateral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_perpsectivetransform/init(a:b:c:d:tx:ty:vx:vy:v:))*