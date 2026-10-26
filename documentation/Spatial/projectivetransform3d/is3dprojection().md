# is3DProjection()

**Framework**: Spatial  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value that indicates whether the transform is a 3D projection.

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
func is3DProjection() -> Bool
```

```c
static bool SPProjectiveTransform3DIs3DProjection(SPProjectiveTransform3D transform);
```

## See Also

### Checking characteristics
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](./isuniform%28overdimensions%29.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var isAffine: Bool](./isaffine.md)
  A Boolean value that indicates whether the transform is affine.
- [var isInvertible: Bool](./isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.
- [SPProjectiveTransform3DIsUniformOverDimensions](../spprojectivetransform3disuniformoverdimensions.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [SPProjectiveTransform3DIsValid](../spprojectivetransform3disvalid.md)
  A Boolean value that indicates whether the transform is a valid transform.
- [SPProjectiveTransform3DInvalid](../spprojectivetransform3dinvalid.md)
  The null transform that represents an invalid value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/is3dprojection())*