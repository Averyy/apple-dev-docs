# init(localizedName:deviceID:source:)

**Framework**: Core Media I/O  
**Kind**: init

Creates an extension device.

**Availability**:
- Mac Catalyst 15.4+

## Declaration

```swift
convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)
```

## Parameters

- `localizedName`: A localized name for the device.
- `deviceID`: A universally unique device identifier value.
- `source`: An extension-specific object that conforms to the   protocol.

## See Also

- [init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)](cmioextensiondevice/init(localizedname:deviceid:legacydeviceid:source:).md)
  Creates an extension device with an optional legacy device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/init(localizedname:deviceid:source:))*