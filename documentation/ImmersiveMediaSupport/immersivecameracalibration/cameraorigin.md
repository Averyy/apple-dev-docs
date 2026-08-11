# ImmersiveCameraCalibration.CameraOrigin

**Framework**: Immersive Media Support  
**Kind**: struct

A type that holds the position information representing the origin from which to render the calibration in 3D space relative to the person’s eye.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct CameraOrigin
```

#### Overview

Coordinates are in meters.

## Topics

### Initializers
- [init(left: Point3DFloat, right: Point3DFloat)](immersivecameracalibration/cameraorigin/init(left:right:).md)
### Type Properties
- [static let zero: ImmersiveCameraCalibration.CameraOrigin](immersivecameracalibration/cameraorigin/zero.md)
  The default immersive camera origin.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [ImmersiveCameraCalibration.CameraTextureMapping](immersivecameracalibration/cameratexturemapping.md)
  A type that holds the matrices used for video frame texture mapping on the camera lens geometry.
- [class ImmersiveCameraMeshCalibration](immersivecamerameshcalibration.md)
  Calibration mesh geometry based on USDZ data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/cameraorigin)*