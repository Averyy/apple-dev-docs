# init(localizedName:deviceID:legacyDeviceID:source:)

**Framework**: Core Media I/O  
**Kind**: init

Creates an extension device with an optional legacy device identifier.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)
```

## Parameters

- `localizedName`: A localized name for the device.
- `deviceID`: A universally unique device identifier value.
- `legacyDeviceID`: Set this argument to   if your device has no backward-compatibility requirements.
- `source`: An extension-specific object that conforms to the   protocol.

## See Also

- [convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)](cmioextensiondevice/init(localizedname:deviceid:source:).md)
  Creates an extension device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/init(localizedname:deviceid:legacydeviceid:source:))*