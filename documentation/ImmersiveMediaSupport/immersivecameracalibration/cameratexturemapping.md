# ImmersiveCameraCalibration.CameraTextureMapping

**Framework**: Immersive Media Support  
**Kind**: struct

A type that holds the matrices used for video frame texture mapping on the camera lens geometry.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CameraTextureMapping
```

## Topics

### Initializers
- [init(from: any Decoder) throws](immersivecameracalibration/cameratexturemapping/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(left: matrix_float3x3, right: matrix_float3x3)](immersivecameracalibration/cameratexturemapping/init(left:right:).md)
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecameracalibration/cameratexturemapping/encode(to:).md)
  Encodes this value into the given encoder.
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
  A type that holds the position information representing the origin from which to render the calibration in 3D space relative to the user’s eye


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/cameratexturemapping)*