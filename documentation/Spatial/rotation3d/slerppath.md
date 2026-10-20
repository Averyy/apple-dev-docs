# Rotation3D.SlerpPath

**Framework**: Spatial  
**Kind**: enum  
**Role**: Enumeration

Constants that define the arc that a slerp operation takes.

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
enum SlerpPath
```

## Topics

### Enumeration Cases
- [Rotation3D.SlerpPath.automatic](./slerppath/automatic.md)
  Spherical linear interpolation along the automatically selected arc between two rotations.
- [Rotation3D.SlerpPath.shortest](./slerppath/shortest.md)
  Spherical linear interpolation along the shortest arc between two rotations.
- [Rotation3D.SlerpPath.longest](./slerppath/longest.md)
  Spherical linear interpolation along the longest arc between two rotations.
### Instance Methods
- [func hash(into: inout Hasher)](./hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Operator Functions
- [static func == (Rotation3D, Rotation3D) -> Bool](./eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two values are equal.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Transforming a 3D rotation structure
- [static func slerp(from: Rotation3D, to: Rotation3D, t: Double, along: Rotation3D.SlerpPath) -> Rotation3D](./slerp%28from,to,t,along%29.md)
  Returns the spherical linear interpolation along either the shortest or the longest arc between two rotations.
- [var inverse: Rotation3D](./inverse.md)
  The inverse of the rotation.
- [static let identity: Rotation3D](./identity.md)
  The identity rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/slerppath)*