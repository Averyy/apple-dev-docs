# manufacturer

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A string representing the device’s manufacturer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var manufacturer: String? { get }
```

```objc
@property (readonly, nullable) NSString * manufacturer;
```

## See Also

### Accessing Data About a Device
- [var udiDeviceIdentifier: String?](./udideviceidentifier.md)
  The device identifier portion of the US Food and Drug Administration’s Unique Device Identifier (UDI).
- [var firmwareVersion: String?](./firmwareversion.md)
  An arbitrary string representing the current version of the firmware running on the device.
- [var hardwareVersion: String?](./hardwareversion.md)
  An arbitrary string representing the hardware version of the device.
- [var localIdentifier: String?](./localidentifier.md)
  An identifier that uniquely identifies the device object on the hardware running this code.
- [var model: String?](./model.md)
  A string representing the device’s model.
- [var name: String?](./name.md)
  The user-facing name for the device.
- [var softwareVersion: String?](./softwareversion.md)
  An arbitrary string representing the version of the software running on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdevice/manufacturer)*