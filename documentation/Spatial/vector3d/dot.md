# dot(_:)

**Framework**: Spatial  
**Kind**: method

Returns the dot product of the vector and the specified vector.

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
func dot(_ other: Vector3D) -> Double
```

## Parameters

- `other`: The second vector.

## See Also

- [func cross(Vector3D) -> Vector3D](vector3d/cross(_:).md)
  Returns the cross product of the vector and the specified vector.
- [var length: Double](vector3d/length.md)
  The length of the vector.
- [var lengthSquared: Double](vector3d/lengthsquared.md)
  The square of the length of the vector.
- [func normalize()](vector3d/normalize.md)
  Normalizes the mutable vector.
- [var normalized: Vector3D](vector3d/normalized.md)
  A new vector that represents the normalized copy of the current vector.
- [func projected(Vector3D) -> Vector3D](vector3d/projected(_:).md)
  Returns the vector projected onto the specified vector.
- [func reflected(Vector3D) -> Vector3D](vector3d/reflected(_:).md)
  Returns the reflection direction of the incident vector and a specified unit normal vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d/dot(_:))*