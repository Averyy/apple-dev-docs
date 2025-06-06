# rotated(by:)

**Framework**: Spatial  
**Kind**: method  
**Required**: Yes

Returns the entity that results from applying the specified rotation.

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
func rotated(by rotation: Rotation3D) -> Self
```

## Parameters

- `rotation`: The rotation structure that defines the rotation’s angle and axis.

## See Also

- [func rotate(by: simd_quatd)](rotatable3d/rotate(by:)-usrg.md)
  Rotates the entity by a quaternion.
- [func rotate(by: Rotation3D)](rotatable3d/rotate(by:)-1g3rl.md)
  Rotates the entity by an angle over an axis.
- [func rotated(by: simd_quatd) -> Self](rotatable3d/rotated(by:)-4gdqe.md)
  Returns the entity that a quaternion rotates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotatable3d/rotated(by:)-7bx4w)*