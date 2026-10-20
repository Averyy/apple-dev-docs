# ImmersiveCameraCalibration.CalibrationType

**Framework**: Immersive Media Support  
**Kind**: enum  
**Role**: Enumeration

A value that represents the calibration type used to generate camera calibration geometry.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum CalibrationType
```

## Topics

### Enumeration Cases
- [ImmersiveCameraCalibration.CalibrationType.immersiveCameraLensDefinition(_:)](./calibrationtype/immersivecameralensdefinition%28_%29.md)
  A value that represents a calibration type that uses coefficients to present each camera lens.
- [ImmersiveCameraCalibration.CalibrationType.usdzMesh(_:)](./calibrationtype/usdzmesh%28_%29.md)
  A value that represents a calibration type that uses a calibration mesh containing the calibration for each lens represented as a mesh inside a USDZ file.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Calibration configuration
- [struct ImmersiveCameraLensDefinition](../immersivecameralensdefinition.md)
  This type holds the ILPD lens configuration parameters to generate a camera calibration type instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/calibrationtype)*