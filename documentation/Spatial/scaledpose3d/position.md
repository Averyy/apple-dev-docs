# position

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The scaled pose’s position.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var position: Point3D
```

```c
SPPoint3D position;
```

## See Also

### Inspecting a 3D scaled pose’s properties
- [var matrix: simd_double4x4](./matrix.md)
  The scaled pose’s underlying matrix.
- [var rotation: Rotation3D](./rotation.md)
  The scaled pose’s rotation.
- [var scale: Double](./scale.md)
  The scaled pose’s scale.
- [var inverse: ScaledPose3D](./inverse.md)
  The scaled pose’s inverse.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the notification.
- [static var identity: ScaledPose3D](./identity.md)
  The identity scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/position)*