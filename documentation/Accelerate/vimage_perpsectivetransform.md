# vImage_PerpsectiveTransform

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A projective-transformation matrix.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct vImage_PerpsectiveTransform
```

```c
typedef struct vImage_PerpsectiveTransform { ... } vImage_PerpsectiveTransform;
```

## Topics

### Creating a projective-transformation structure
- [init()](./vimage_perpsectivetransform/init%28%29.md)
  Creates a projective-transformation structure.
- [init(a: Float, b: Float, c: Float, d: Float, tx: Float, ty: Float, vx: Float, vy: Float, v: Float)](./vimage_perpsectivetransform/init%28a,b,c,d,tx,ty,vx,vy,v%29.md)
  Creates a projective-transformation structure from the specified single-precision values.
- [init?(source: vImage_PerpsectiveTransform.QuadrilateralPoints, destination: vImage_PerpsectiveTransform.QuadrilateralPoints)](./vimage_perpsectivetransform/init%28source,destination%29.md)
  Returns a projective-transformation structure that defines the mapping between a source quadrilateral and a destination quadrilateral.
### Inspecting a projective-transformation structure’s properties
- [var a: Float](./vimage_perpsectivetransform/a.md)
  The top-left cell in the 3 x 3 transformation matrix.
- [var b: Float](./vimage_perpsectivetransform/b.md)
  The top-middle cell in the 3 x 3 transformation matrix.
- [var c: Float](./vimage_perpsectivetransform/c.md)
  The middle-left cell in the 3 x 3 transformation matrix.
- [var d: Float](./vimage_perpsectivetransform/d.md)
  The middle-middle cell in the 3 x 3 transformation matrix.
- [var tx: Float](./vimage_perpsectivetransform/tx.md)
  The x-coordinate translation.
- [var ty: Float](./vimage_perpsectivetransform/ty.md)
  The y-coordinate translation.
- [var vx: Float](./vimage_perpsectivetransform/vx.md)
  The x-component of the projective vector.
- [var vy: Float](./vimage_perpsectivetransform/vy.md)
  The y-component of the projective vector.
- [var v: Float](./vimage_perpsectivetransform/v.md)
  The homogeneous scale factor.
### Type Aliases
- [vImage_PerpsectiveTransform.QuadrilateralPoints](./vimage_perpsectivetransform/quadrilateralpoints.md)
  A tuple of four points that define a quadrilateral.
### Enumerations
- [vImage_PerpsectiveTransform.Interpolation](./vimage_perpsectivetransform/interpolation.md)
  Constants that describe the projective-transformation interpolation method.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Computing a projective transformation from source and destination quadrilaterals
- [Transforming an image in three dimensions](./transforming-an-image-in-three-dimensions.md)
  Create and use a projective transformation to apply a perspective warp to an image.
- [func vImageGetPerspectiveWarp(UnsafePointer<(Float, Float)>, UnsafePointer<(Float, Float)>, UnsafeMutablePointer<vImage_PerpsectiveTransform>, vImage_Flags) -> vImage_Error](./vimagegetperspectivewarp%28_,_,_,_%29.md)
  Returns a projective-transformation structure that defines the mapping between a source quadrilateral and a destination quadrilateral.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_perpsectivetransform)*