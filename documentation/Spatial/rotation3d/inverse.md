# inverse

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

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

```c
static SPRotation3D SPRotation3DInverse(SPRotation3D rotation);
```

## See Also

### Transforming a 3D rotation structure
- [static func slerp(from: Rotation3D, to: Rotation3D, t: Double, along: Rotation3D.SlerpPath) -> Rotation3D](./slerp%28from,to,t,along%29.md)
  Returns the spherical linear interpolation along either the shortest or the longest arc between two rotations.
- [Rotation3D.SlerpPath](./slerppath.md)
  Constants that define the arc that a slerp operation takes.
- [static let identity: Rotation3D](./identity.md)
  The identity rotation.
- [SPRotation3DSlerp](../sprotation3dslerp.md)
  Returns the spherical linear interpolation along the shortest arc between two rotations.
- [SPRotation3DSlerpLongest](../sprotation3dslerplongest.md)
  Returns the spherical linear interpolation along the longest arc between two rotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/rotation3d/inverse)*