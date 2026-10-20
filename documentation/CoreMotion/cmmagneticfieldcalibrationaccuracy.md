# CMMagneticFieldCalibrationAccuracy

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

Indicates the calibration accuracy of a magnetic field estimate

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum CMMagneticFieldCalibrationAccuracy
```

```c
enum CMMagneticFieldCalibrationAccuracy : int;
```

#### Overview

One of the `enum` constants of the `CMMagneticFieldCalibrationAccuracy` type is the value of the accuracy field of the [`CMCalibratedMagneticField`](./cmcalibratedmagneticfield.md) structure returned from the [`magneticField`](./cmdevicemotion/magneticfield.md) property.

## Topics

### Constants
- [CMMagneticFieldCalibrationAccuracy.uncalibrated](./cmmagneticfieldcalibrationaccuracy/uncalibrated.md)
  The magnetic field estimate is not calibrated.
- [CMMagneticFieldCalibrationAccuracy.low](./cmmagneticfieldcalibrationaccuracy/low.md)
  The accuracy of the magnetic field calibration is low.
- [CMMagneticFieldCalibrationAccuracy.medium](./cmmagneticfieldcalibrationaccuracy/medium.md)
  The accuracy of the magnetic field calibration is medium.
- [CMMagneticFieldCalibrationAccuracy.high](./cmmagneticfieldcalibrationaccuracy/high.md)
  The accuracy of the magnetic field calibration is high.
### Initializers
- [init?(rawValue: Int32)](./cmmagneticfieldcalibrationaccuracy/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Calibrated Magnetic Field
- [var magneticField: CMCalibratedMagneticField](./cmdevicemotion/magneticfield.md)
  Returns the magnetic field vector with respect to the device.
- [struct CMCalibratedMagneticField](./cmcalibratedmagneticfield.md)
  Calibrated magnetic field data and an estimate of the accuracy of the calibration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmagneticfieldcalibrationaccuracy)*