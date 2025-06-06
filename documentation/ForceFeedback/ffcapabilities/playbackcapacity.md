# playbackCapacity

**Framework**: Force Feedback  
**Kind**: property

The maximum number of created effects that can be simultaneously played via calls to FFEffectStart. This number will always be equal to or less than the storageCapacity. A device driver may allow more effects to be created than the physical device can actually handle. Therefore, this number is an important parameter for FF designers.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.2+

## Declaration

```swift
var playbackCapacity: UInt32
```

## See Also

- [var driverVer: NumVersion](ffcapabilities/driverver.md)
  Specifies the version number of the force-feedback device driver, using a NumVersion structure.
- [var emulatedEffects: UInt32](ffcapabilities/emulatedeffects.md)
  FFCapabilitiesEffectType flags that identify all effect types not directly supported by the device, but emulated by the plugIn.
- [var ffAxes: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8)](ffcapabilities/ffaxes.md)
  An array of values that describe the axes on which force-feedback is present.
- [var ffSpecVer: NumVersion](ffcapabilities/ffspecver.md)
  Specifies the version number of the FF API specification supported by this plugIn. It should be specified using the fields of the NumVersion structure. The first version of the FF API specification is 1.0.0f0.
- [var firmwareVer: NumVersion](ffcapabilities/firmwarever.md)
  Specifies the firmware revision of the device, using a NumVersion structure.
- [var hardwareVer: NumVersion](ffcapabilities/hardwarever.md)
  Specifies the hardware revision of the device, using a NumVersion structure.
- [var numFfAxes: UInt32](ffcapabilities/numffaxes.md)
  The number of controller axes that provide force feedback. Indicates the number of valid elements in ffAxes.
- [var storageCapacity: UInt32](ffcapabilities/storagecapacity.md)
  The maximum number of effects that can be created via calls to FFDeviceCreateEffect and coexist at any one time. This may or may not be different from the playbackCapacity, depending on device driver complexity.
- [var subType: UInt32](ffcapabilities/subtype.md)
  The force-feedback subcategory which best identifies the device’s FF capabilities.
- [var supportedEffects: UInt32](ffcapabilities/supportedeffects.md)
  FFCapabilitiesEffectType flags that identify all effect types supported by the plugIn/device (including driver-emulated effects).


---

*[View on Apple Developer](https://developer.apple.com/documentation/forcefeedback/ffcapabilities/playbackcapacity)*