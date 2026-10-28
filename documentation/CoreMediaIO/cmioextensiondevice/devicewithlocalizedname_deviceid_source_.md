# deviceWithLocalizedName:deviceID:source:

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Type Method

Returns a new extension device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 10.7+

## Declaration

```objc
+ (instancetype) deviceWithLocalizedName:(NSString *) localizedName deviceID:(NSUUID *) deviceID source:(id<CMIOExtensionDeviceSource>) source;
```

## Return Value

A new device instance.

## Parameters

- `localizedName`: A localized name for the device.
- `deviceID`: A universally unique device identifier value.
- `source`: An extension-specific object that conforms to the [`CMIOExtensionDeviceSource`](../cmioextensiondevicesource.md) protocol.

## See Also

### Creating a Device
- [+ deviceWithLocalizedName:deviceID:legacyDeviceID:source:](./devicewithlocalizedname_deviceid_legacydeviceid_source_.md)
  Returns a new extension device with an optional legacy device identifier.
- [convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)](./init%28localizedname,deviceid,source%29.md)
  Creates an extension device.
- [init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)](./init%28localizedname,deviceid,legacydeviceid,source%29.md)
  Creates an extension device with an optional legacy device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/devicewithlocalizedname:deviceid:source:)*