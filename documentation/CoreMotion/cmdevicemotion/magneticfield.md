# magneticField

**Framework**: Core Motion  
**Kind**: property

Returns the magnetic field vector with respect to the device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var magneticField: CMCalibratedMagneticField { get }
```

#### Discussion

The [`CMCalibratedMagneticField`](cmcalibratedmagneticfield.md) returned by this property gives you the total magnetic field in the device’s vicinity without device bias. Unlike the [`magneticField`](cmmagnetometerdata/magneticfield.md) property of the [`CMMagnetometerData`](cmmagnetometerdata.md) class, these values reflect the earth’s magnetic field plus surrounding fields, minus device bias.

If the device does not have a magnetometer, the `accuracy` field of the property’s value (a [`CMCalibratedMagneticField`](cmcalibratedmagneticfield.md) structure) is [`CMMagneticFieldCalibrationAccuracy.uncalibrated`](cmmagneticfieldcalibrationaccuracy/uncalibrated.md).

## See Also

- [struct CMCalibratedMagneticField](cmcalibratedmagneticfield.md)
  Calibrated magnetic field data and an estimate of the accuracy of the calibration.
- [enum CMMagneticFieldCalibrationAccuracy](cmmagneticfieldcalibrationaccuracy.md)
  Indicates the calibration accuracy of a magnetic field estimate


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdevicemotion/magneticfield)*