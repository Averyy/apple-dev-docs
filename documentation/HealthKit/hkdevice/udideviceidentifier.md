# udiDeviceIdentifier

**Framework**: HealthKit  
**Kind**: property

The device identifier portion of the US Food and Drug Administration’s Unique Device Identifier (UDI).

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var udiDeviceIdentifier: String? { get }
```

#### Discussion

The UDI identifies medical devices. You can look up additional information about the device at [`AccessGUDID`](https://developer.apple.comhttp://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/GlobalUDIDatabaseGUDID/ucm444831.htm). For more information, see [`FDA Unique Device Identification`](https://developer.apple.comhttp://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/default.htm).

## See Also

- [var firmwareVersion: String?](hkdevice/firmwareversion.md)
  An arbitrary string representing the current version of the firmware running on the device.
- [var hardwareVersion: String?](hkdevice/hardwareversion.md)
  An arbitrary string representing the hardware version of the device.
- [var localIdentifier: String?](hkdevice/localidentifier.md)
  An identifier that uniquely identifies the device object on the hardware running this code.
- [var manufacturer: String?](hkdevice/manufacturer.md)
  A string representing the device’s manufacturer.
- [var model: String?](hkdevice/model.md)
  A string representing the device’s model.
- [var name: String?](hkdevice/name.md)
  The user-facing name for the device.
- [var softwareVersion: String?](hkdevice/softwareversion.md)
  An arbitrary string representing the version of the software running on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdevice/udideviceidentifier)*