# ImmersiveCameraMeshCalibration

**Framework**: Immersive Media Support  
**Kind**: class

Calibration mesh geometry based on USDZ data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class ImmersiveCameraMeshCalibration
```

#### Overview

This class is associated with the calibration type ‘usdzMesh’ and is used for calibration performed by camera lens provider using usdz.

## Topics

### Initializers
- [init(name: String, usdzData: Data)](immersivecamerameshcalibration/init(name:usdzdata:).md)
  Creates an instance of `ImmersiveCameraMeshCalibration`.
### Instance Properties
- [let name: String](immersivecamerameshcalibration/name.md)
- [let usdzData: Data](immersivecamerameshcalibration/usdzdata.md)

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [ImmersiveCameraCalibration.CameraOrigin](immersivecameracalibration/cameraorigin.md)
  A type that holds the position information representing the origin from which to render the calibration in 3D space relative to the person’s eye.
- [ImmersiveCameraCalibration.CameraTextureMapping](immersivecameracalibration/cameratexturemapping.md)
  A type that holds the matrices used for video frame texture mapping on the camera lens geometry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecamerameshcalibration)*