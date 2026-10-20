# isInvertible

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

Returns a Boolean value that indicates whether the transform is invertible.

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
var isInvertible: Bool { get }
```

```c
static bool SPProjectiveTransform3DIsInvertible(SPProjectiveTransform3D transform);
```

## See Also

### Checking characteristics
- [func is3DProjection() -> Bool](./is3dprojection%28%29.md)
  Returns a Boolean value that indicates whether the transform is a 3D projection.
- [func isUniform(overDimensions: Dimension3DSet) -> Bool](./isuniform%28overdimensions%29.md)
  Returns a Boolean value that indicates whether the transform scales equally over the specified dimensions.
- [var isAffine: Bool](./isaffine.md)
  A Boolean value that indicates whether the transform is affine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/projectivetransform3d/isinvertible)*