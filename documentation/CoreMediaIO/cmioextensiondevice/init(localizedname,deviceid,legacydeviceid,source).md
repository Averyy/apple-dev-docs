# init(localizedName:deviceID:legacyDeviceID:source:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates an extension device with an optional legacy device identifier.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)
```

```objc
- (instancetype) initWithLocalizedName:(NSString *) localizedName deviceID:(NSUUID *) deviceID legacyDeviceID:(NSString *) legacyDeviceID source:(id<CMIOExtensionDeviceSource>) source;
```

## Parameters

- `localizedName`: A localized name for the device.
- `deviceID`: A universally unique device identifier value.
- `legacyDeviceID`: A string device identifier for backward compatibility with existing CMIO DAL clients. The value you provide can differ from the value of `deviceID.UUIDString`.

  Set this argument to `nil` if your device has no backward-compatibility requirements.
- `source`: An extension-specific object that conforms to the [`CMIOExtensionDeviceSource`](../cmioextensiondevicesource.md) protocol.

## See Also

### Creating a Device
- [convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)](./init%28localizedname,deviceid,source%29.md)
  Creates an extension device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/init(localizedname:deviceid:legacydeviceid:source:))*