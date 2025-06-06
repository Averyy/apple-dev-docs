# rotate(by:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Rotates the entity by an angle over an axis.

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
mutating func rotate(by rotation: Rotation3D)
```

## Parameters

- `rotation`: The rotation structure that defines the rotation’s angle and axis.

## See Also

- [func rotate(by: simd_quatd)](rotatable3d/rotate(by:)-usrg.md)
  Rotates the entity by a quaternion.
- [func rotated(by: simd_quatd) -> Self](rotatable3d/rotated(by:)-4gdqe.md)
  Returns the entity that a quaternion rotates.
- [func rotated(by: Rotation3D) -> Self](rotatable3d/rotated(by:)-7bx4w.md)
  Returns the entity that results from applying the specified rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotatable3d/rotate(by:)-1g3rl)*