# reflected(_:)

**Framework**: Spatial  
**Kind**: method

Returns the reflection direction of the incident vector and a specified unit normal vector.

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
func reflected(_ normal: Vector3D) -> Vector3D
```

## Parameters

- `normal`: The unit normal vector.

## See Also

- [func cross(Vector3D) -> Vector3D](vector3d/cross(_:).md)
  Returns the cross product of the vector and the specified vector.
- [func dot(Vector3D) -> Double](vector3d/dot(_:).md)
  Returns the dot product of the vector and the specified vector.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/vector3d/reflected(_:))*