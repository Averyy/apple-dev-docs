# *=(_:_:)

**Framework**: Spatial  
**Kind**: op  
**Role**: Operator

Computes the product of two rotations and stores the result in the left-hand-side variable.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
static func *= (lhs: inout Rotation3D, rhs: Rotation3D)
```

## Parameters

- `lhs`: The left-hand-side value.
- `rhs`: The right-hand-side value.

## See Also

### Applying arithmetic operations
- [static func * (Rotation3D, Rotation3D) -> Rotation3D](./star%28_,_%29-1tc8f.md)
  Returns the product of two rotations.
- [static func * (Rotation3D, Double) -> Rotation3D](./star%28_,_%29-5dxqv.md)
  Returns the spherical linear interpolation between the identity rotation and the left-hand-side rotation at the right-hand-side interpolation parameter.
- [static func * (Double, Rotation3D) -> Rotation3D](./star%28_,_%29-9t389.md)
  Returns the spherical linear interpolation between the identity rotation and the right-hand-side rotation at the left-hand-side interpolation parameter.
- [func * <T>(Rotation3D, T) -> T](../star%28_,_%29.md)
  Returns the rotatable entity that results from applying the rotatable entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/*=(_:_:))*