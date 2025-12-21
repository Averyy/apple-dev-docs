# HKMetadataKeyAppleDeviceCalibrated

**Framework**: HealthKit  
**Kind**: var

The key for metadata indicating whether the system had data from a sufficient amount of calibrated sensors when recording the sample.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let HKMetadataKeyAppleDeviceCalibrated: String
```

#### Discussion

This key takes a Boolean value. If it’s [`true`](https://developer.apple.com/documentation/Swift/true), the system has enough high-quality data to make an accurate estimate. If it’s [`false`](https://developer.apple.com/documentation/Swift/false), the system provides an estimate based on data that may be less accurate.

The key is read-only.

## See Also

- [let HKMetadataKeyDeviceSerialNumber: String](hkmetadatakeydeviceserialnumber.md)
  The key for the serial number of the device that generated the data.
- [let HKMetadataKeyUDIDeviceIdentifier: String](hkmetadatakeyudideviceidentifier.md)
  The device identifier portion of a device’s UDI (unique device identifier).
- [let HKMetadataKeyUDIProductionIdentifier: String](hkmetadatakeyudiproductionidentifier.md)
  The production identifier portion of a device’s UDI (unique device identifier).
- [let HKMetadataKeyDigitalSignature: String](hkmetadatakeydigitalsignature.md)
  A digital signature that can be used to validate the origin of the HealthKit object.
- [let HKMetadataKeyDeviceName: String](hkmetadatakeydevicename.md)
  The name of the device that took this reading.
- [let HKMetadataKeyDeviceManufacturerName: String](hkmetadatakeydevicemanufacturername.md)
  The name of the manufacturer of the device that took this reading.
- [let HKMetadataKeyDevicePlacementSide: String](hkmetadatakeydeviceplacementside.md)
  The key for metadata indicating the placement of the device that measured a sample.
- [enum HKDevicePlacementSide](hkdeviceplacementside.md)
  Values that indicate the placement of the device that measured a sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyappledevicecalibrated)*