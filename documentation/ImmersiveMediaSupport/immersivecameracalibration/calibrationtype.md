# ImmersiveCameraCalibration.CalibrationType

**Framework**: Immersive Media Support  
**Kind**: enum

An enum representing the calibration type used to generate camera calibration geometry.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
enum CalibrationType
```

## Topics

### Enumeration Cases
- [ImmersiveCameraCalibration.CalibrationType.meiRives](immersivecameracalibration/calibrationtype/meirives.md)
  Calibrations that use coefficients to present each camera lens.
- [ImmersiveCameraCalibration.CalibrationType.usdzMesh](immersivecameracalibration/calibrationtype/usdzmesh.md)
  USDZ mesh calibration: uses a calibration mesh containing the calibration for each lens represented as a mesh inside a USDZ file.
### Initializers
- [init?(rawValue: String)](immersivecameracalibration/calibrationtype/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Instance Properties
- [var rawValue: String](immersivecameracalibration/calibrationtype/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ImmersiveCameraCalibration.CalibrationType.RawValue](immersivecameracalibration/calibrationtype/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Default Implementations
- [Equatable Implementations](immersivecameracalibration/calibrationtype/equatable-implementations.md)
- [RawRepresentable Implementations](immersivecameracalibration/calibrationtype/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivecameracalibration/calibrationtype)*