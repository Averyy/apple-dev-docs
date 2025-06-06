# CMCalibratedMagneticField

**Framework**: Core Motion  
**Kind**: struct

Calibrated magnetic field data and an estimate of the accuracy of the calibration.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CMCalibratedMagneticField
```

## Topics

### Initializers
- [init()](cmcalibratedmagneticfield/init.md)
  Initializes the magnetic field to a set of default values.
- [init(field: CMMagneticField, accuracy: CMMagneticFieldCalibrationAccuracy)](cmcalibratedmagneticfield/init(field:accuracy:).md)
  Initializes the magnetic field to the specified set of values.
### Accessing the Field Values
- [var field: CMMagneticField](cmcalibratedmagneticfield/field.md)
  A structure containing 3-axis calibrated magnetic field data. See the description of the [`CMMagneticField`](cmmagneticfield.md) structure.
- [var accuracy: CMMagneticFieldCalibrationAccuracy](cmcalibratedmagneticfield/accuracy.md)
  An enum-constant value that indicates the accuracy of the magnetic field estimate. See [`CMMagneticFieldCalibrationAccuracy`](cmmagneticfieldcalibrationaccuracy.md).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var magneticField: CMCalibratedMagneticField](cmdevicemotion/magneticfield.md)
  Returns the magnetic field vector with respect to the device.
- [enum CMMagneticFieldCalibrationAccuracy](cmmagneticfieldcalibrationaccuracy.md)
  Indicates the calibration accuracy of a magnetic field estimate


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmcalibratedmagneticfield)*