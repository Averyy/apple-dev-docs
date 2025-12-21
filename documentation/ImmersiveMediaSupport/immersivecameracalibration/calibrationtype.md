# ImmersiveCameraCalibration.CalibrationType

**Framework**: Immersive Media Support  
**Kind**: enum

A value that represents the calibration type used to generate camera calibration geometry.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum CalibrationType
```

## Topics

### Enumeration Cases
- [ImmersiveCameraCalibration.CalibrationType.immersiveCameraLensDefinition(_:)](immersivecameracalibration/calibrationtype/immersivecameralensdefinition(_:).md)
  A value that represents a calibration type that uses coefficients to present each camera lens.
- [ImmersiveCameraCalibration.CalibrationType.usdzMesh(_:)](immersivecameracalibration/calibrationtype/usdzmesh(_:).md)
  A value that represents a calibration type that uses a calibration mesh containing the calibration for each lens represented as a mesh inside a USDZ file.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/calibrationtype)*