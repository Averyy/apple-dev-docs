# scale

**Framework**: Spatial  
**Kind**: property  
**Role**: Instance Property

The scaled pose’s scale.

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
var scale: Double
```

```c
double scale;
```

## See Also

### Inspecting a 3D scaled pose’s properties
- [var matrix: simd_double4x4](./matrix.md)
  The scaled pose’s underlying matrix.
- [var position: Point3D](./position.md)
  The scaled pose’s position.
- [var rotation: Rotation3D](./rotation.md)
  The scaled pose’s rotation.
- [var inverse: ScaledPose3D](./inverse.md)
  The scaled pose’s inverse.
- [var customMirror: Mirror](./custommirror.md)
  A mirror that reflects the notification.
- [static var identity: ScaledPose3D](./identity.md)
  The identity scaled pose.
- [SPScaledPose3DGet4x4Matrix](../spscaledpose3dget4x4matrix.md)
  Returns a 4 x 4 matrix that represents the scaled pose’s translation, rotation, and scale.
- [SPScaledPose3DGetInverse](../spscaledpose3dgetinverse.md)
  Returns a new scaled pose with the inverse matrix of the specified scaled pose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spatial/scaledpose3d/scale)*