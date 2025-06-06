# slerp(from:to:t:along:)

**Framework**: Spatial  
**Kind**: method

Returns the spherical linear interpolation along either the shortest or the longest arc between two rotations.

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
static func slerp(from: Rotation3D, to: Rotation3D, t: Double, along path: Rotation3D.SlerpPath = .shortest) -> Rotation3D
```

#### Return Value

A new rotation. When `t = 0.0`, the result is the `from` rotation. When `t = 1.0`, the result is the `to` rotation. For any other value of `t`, the result is a spherical linear interpolation between the two rotations.

## Parameters

- `from`: The starting rotation.
- `to`: The ending rotation.
- `t`: The position along the interpolation that’s between   and  .
- `path`: An enumeration that specifies whether the interpolation should be along the shortest or the longest path between the two rotations.

## See Also

- [Rotation3D.SlerpPath](rotation3d/slerppath.md)
  Constants that define the arc that a slerp operation takes.
- [var inverse: Rotation3D](rotation3d/inverse.md)
  The inverse of the rotation.
- [static let identity: Rotation3D](rotation3d/identity.md)
  The identity rotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/slerp(from:to:t:along:))*