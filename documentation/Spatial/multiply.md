# *(_:_:)

**Framework**: Spatial  
**Kind**: op

Returns the rotatable entity that results from applying the rotatable entity.

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
func * <T>(lhs: Rotation3D, rhs: T) -> T where T : Rotatable3D
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

- [static func * (Rotation3D, Rotation3D) -> Rotation3D](rotation3d/*(_:_:)-1tc8f.md)
  Returns the product of two rotations.
- [static func * (Rotation3D, Double) -> Rotation3D](rotation3d/*(_:_:)-5dxqv.md)
  Returns the spherical linear interpolation between the identity rotation and the left-hand-side rotation at the right-hand-side interpolation parameter.
- [static func * (Double, Rotation3D) -> Rotation3D](rotation3d/*(_:_:)-9t389.md)
  Returns the spherical linear interpolation between the identity rotation and the right-hand-side rotation at the left-hand-side interpolation parameter.
- [static func *= (inout Rotation3D, Rotation3D)](rotation3d/*=(_:_:).md)
  Computes the product of two rotations and stores the result in the left-hand-side variable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/*(_:_:))*