# ImmersiveCameraCalibration.CameraTextureMapping

**Framework**: Immersive Media Support  
**Kind**: struct

A type that holds the matrices used for video frame texture mapping on the camera lens geometry.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CameraTextureMapping
```

## Topics

### Initializers
- [init(left: matrix_float3x3, right: matrix_float3x3)](immersivecameracalibration/cameratexturemapping/init(left:right:).md)
### Type Properties
- [static let identity: ImmersiveCameraCalibration.CameraTextureMapping](immersivecameracalibration/cameratexturemapping/identity.md)
  The default camera texture matrix for the immersive camera.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ImmersiveCameraCalibration.CameraOrigin](immersivecameracalibration/cameraorigin.md)
  A type that holds the position information representing the origin from which to render the calibration in 3D space relative to the person’s eye.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/cameratexturemapping)*