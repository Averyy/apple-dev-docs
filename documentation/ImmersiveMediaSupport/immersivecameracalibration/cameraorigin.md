# ImmersiveCameraCalibration.CameraOrigin

**Framework**: Immersive Media Support  
**Kind**: struct

Position information that represents the origin from which to render the calibration in 3D space relative to the user’s eye

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct CameraOrigin
```

## Topics

### Initializers
- [init(from: any Decoder) throws](immersivecameracalibration/cameraorigin/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(left: simd_float3, right: simd_float3)](immersivecameracalibration/cameraorigin/init(left:right:).md)
### Instance Methods
- [func encode(to: any Encoder) throws](immersivecameracalibration/cameraorigin/encode(to:).md)
  Encodes this value into the given encoder.
### Type Properties
- [static let zero: ImmersiveCameraCalibration.CameraOrigin](immersivecameracalibration/cameraorigin/zero.md)
  Holds the default value of (0, 0, 0) for the immersive camera origin i.e zero vector for the left camera and zero vector for the right camera

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ImmersiveCameraCalibration.CameraTextureMapping](immersivecameracalibration/cameratexturemapping.md)
  Represents the matrices used for video frame texture mapping on the camera lens geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/cameraorigin)*