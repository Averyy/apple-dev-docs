# Rotation3D.SlerpPath

**Framework**: Spatial  
**Kind**: enum

Constants that define the arc that a slerp operation takes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
enum SlerpPath
```

## Topics

### Enumeration Cases
- [Rotation3D.SlerpPath.automatic](rotation3d/slerppath/automatic.md)
  Spherical linear interpolation along the automatically selected arc between two rotations.
- [Rotation3D.SlerpPath.shortest](rotation3d/slerppath/shortest.md)
  Spherical linear interpolation along the shortest arc between two rotations.
- [Rotation3D.SlerpPath.longest](rotation3d/slerppath/longest.md)
  Spherical linear interpolation along the longest arc between two rotations.
### Instance Methods
- [func hash(into: inout Hasher)](rotation3d/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Operator Functions
- [static func == (Rotation3D, Rotation3D) -> Bool](rotation3d/==(_:_:).md)
  Returns a Boolean value that indicates whether two values are equal.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [static func slerp(from: Rotation3D, to: Rotation3D, t: Double, along: Rotation3D.SlerpPath) -> Rotation3D](rotation3d/slerp(from:to:t:along:).md)
  Returns the spherical linear interpolation along either the shortest or the longest arc between two rotations.
- [var inverse: Rotation3D](rotation3d/inverse.md)
  The inverse of the rotation.
- [static let identity: Rotation3D](rotation3d/identity.md)
  The identity rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/slerppath)*