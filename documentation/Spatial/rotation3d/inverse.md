# inverse

**Framework**: Spatial  
**Kind**: property

The inverse of the rotation.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var inverse: Rotation3D { get }
```

## See Also

- [static func slerp(from: Rotation3D, to: Rotation3D, t: Double, along: Rotation3D.SlerpPath) -> Rotation3D](rotation3d/slerp(from:to:t:along:).md)
  Returns the spherical linear interpolation along either the shortest or the longest arc between two rotations.
- [Rotation3D.SlerpPath](rotation3d/slerppath.md)
  Constants that define the arc that a slerp operation takes.
- [static let identity: Rotation3D](rotation3d/identity.md)
  The identity rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/inverse)*