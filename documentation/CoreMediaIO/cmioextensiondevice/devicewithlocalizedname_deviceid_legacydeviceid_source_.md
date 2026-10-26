# deviceWithLocalizedName:deviceID:legacyDeviceID:source:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new extension device with an optional legacy device identifier.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```objc
+ (instancetype) deviceWithLocalizedName:(NSString *) localizedName deviceID:(NSUUID *) deviceID legacyDeviceID:(NSString *) legacyDeviceID source:(id<CMIOExtensionDeviceSource>) source;
```

#### Return Value

A new device instance.

## Parameters

- `localizedName`: A localized name for the device.
- `deviceID`: A universally unique device identifier value.
- `legacyDeviceID`: A string device identifier for backward compatibility with existing CMIO DAL clients. The value you provide can differ from the value of `deviceID.UUIDString`.

  Set this argument to `nil` if your device has no backward-compatibility requirements.
- `source`: An extension-specific object that conforms to the [`CMIOExtensionDeviceSource`](../cmioextensiondevicesource.md) protocol.

## See Also

### Creating a Device
- [+ deviceWithLocalizedName:deviceID:source:](./devicewithlocalizedname_deviceid_source_.md)
  Returns a new extension device.
- [convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)](./init%28localizedname,deviceid,source%29.md)
  Creates an extension device.
- [init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)](./init%28localizedname,deviceid,legacydeviceid,source%29.md)
  Creates an extension device with an optional legacy device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/devicewithlocalizedname:deviceid:legacydeviceid:source:)*