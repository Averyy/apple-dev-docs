# HKMetadataKeyDigitalSignature

**Framework**: HealthKit  
**Kind**: var

A digital signature that can be used to validate the origin of the HealthKit object.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKMetadataKeyDigitalSignature: String
```

## Mentions

- [Adding Digital Signatures](adding-digital-signatures.md)

#### Discussion

The digital signature is intended to provide data integrity for sample data produced by trusted (tamper resistant) measuring devices. Use the Cryptographic Message Syntax (CMS) to sign data returned by your device (such as timestamps, values, and so forth) using ASN.1 encoding with Distinguished Encoding Rules (DER). The entire signature should be further encoded using base64. Recommended digest is SHA256, and recommended cipher is FIPS PUB 186-4 Digital Signature Standard Elliptic Curve P-256. CMS is specified in IETF RFC 5652. For more information, see Adding Digital Signatures in `HealthKit`.

## See Also

- [let HKMetadataKeyDeviceSerialNumber: String](hkmetadatakeydeviceserialnumber.md)
  The key for the serial number of the device that generated the data.
- [let HKMetadataKeyUDIDeviceIdentifier: String](hkmetadatakeyudideviceidentifier.md)
  The device identifier portion of a device’s UDI (unique device identifier).
- [let HKMetadataKeyUDIProductionIdentifier: String](hkmetadatakeyudiproductionidentifier.md)
  The production identifier portion of a device’s UDI (unique device identifier).
- [let HKMetadataKeyDeviceName: String](hkmetadatakeydevicename.md)
  The name of the device that took this reading.
- [let HKMetadataKeyDeviceManufacturerName: String](hkmetadatakeydevicemanufacturername.md)
  The name of the manufacturer of the device that took this reading.
- [let HKMetadataKeyDevicePlacementSide: String](hkmetadatakeydeviceplacementside.md)
  The key for metadata indicating the placement of the device that measured a sample.
- [enum HKDevicePlacementSide](hkdeviceplacementside.md)
  Values that indicate the placement of the device that measured a sample.
- [let HKMetadataKeyAppleDeviceCalibrated: String](hkmetadatakeyappledevicecalibrated.md)
  The key for metadata indicating whether the system had data from a sufficient amount of calibrated sensors when recording the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeydigitalsignature)*