# isUniform(overDimensions:)

**Framework**: Spatial  
**Kind**: method

Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func isUniform(overDimensions: Dimension3DSet) -> Bool
```

## Parameters

- `overDimensions`: The dimensions that the function checks over.

## See Also

- [func is3DProjection() -> Bool](projectivetransform3d/is3dprojection.md)
  Returns a Boolean value that indicates whether the transform is a 3D projection.
- [var isAffine: Bool](projectivetransform3d/isaffine.md)
  A Boolean value that indicates whether the transform is affine.
- [var isInvertible: Bool](projectivetransform3d/isinvertible.md)
  Returns a Boolean value that indicates whether the transform is invertible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/isuniform(overdimensions:))*