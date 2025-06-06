# localIdentifier

**Framework**: HealthKit  
**Kind**: property

An identifier that uniquely identifies the device object on the hardware running this code.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var localIdentifier: String? { get }
```

#### Discussion

For example, Bluetooth peripherals that store data directly into HealthKit use the peripheral’s CoreBluetooth UUID. This ID is only valid on the current hardware running the app. For example, connecting the same Bluetooth device to an iPhone and an Apple Watch produces two different local identifiers. Similarly, updating a device changes the local identifier. Device objects with different local identifiers appear as separate devices in the HealthKit Store.

## See Also

- [var udiDeviceIdentifier: String?](hkdevice/udideviceidentifier.md)
  The device identifier portion of the US Food and Drug Administration’s Unique Device Identifier (UDI).
- [var firmwareVersion: String?](hkdevice/firmwareversion.md)
  An arbitrary string representing the current version of the firmware running on the device.
- [var hardwareVersion: String?](hkdevice/hardwareversion.md)
  An arbitrary string representing the hardware version of the device.
- [var manufacturer: String?](hkdevice/manufacturer.md)
  A string representing the device’s manufacturer.
- [var model: String?](hkdevice/model.md)
  A string representing the device’s model.
- [var name: String?](hkdevice/name.md)
  The user-facing name for the device.
- [var softwareVersion: String?](hkdevice/softwareversion.md)
  An arbitrary string representing the version of the software running on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdevice/localidentifier)*