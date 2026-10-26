# SPProjectiveTransform3DIsValid

**Framework**: Spatial  
**Kind**: func  
**Role**: Function

A Boolean value that indicates whether the transform is a valid transform.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```c
static bool SPProjectiveTransform3DIsValid(SPProjectiveTransform3D transform);
```

## See Also

### Checking characteristics
- [func is3DProjection() -> Bool](./projectivetransform3d/is3dprojection%28%29.md)
  Returns a Boolean value that indicates whether the transform is a 3D projection.
- [var isAffine: Bool](./projectivetransform3d/isaffine.md)
  A Boolean value that indicates whether the transform is affine.
- [var isInvertible: Bool](./projectivetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [SPProjectiveTransform3DIsUniformOverDimensions](./spprojectivetransform3disuniformoverdimensions.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [SPProjectiveTransform3DInvalid](./spprojectivetransform3dinvalid.md)
  The null transform that represents an invalid value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/spprojectivetransform3disvalid)*