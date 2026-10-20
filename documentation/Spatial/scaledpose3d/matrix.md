# matrix

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The scaled pose’s underlying matrix.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS
- watchOS 11.0+

## Declaration

```swift
var matrix: simd_double4x4 { get }
```

## See Also

### Inspecting a 3D scaled pose’s properties
- [var position: Point3D](./position.md)
  The scaled pose’s position.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/matrix)*