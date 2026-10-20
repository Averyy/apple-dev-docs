# init(localizedName:deviceID:source:)

**Framework**: Core Media I/O  
**Kind**: init  
**Role**: Initializer

Creates an extension device.

**Availability**:
- Mac Catalyst 15.4+
- macOS 10.7+

## Declaration

```swift
convenience init(localizedName: String, deviceID: UUID, source: any CMIOExtensionDeviceSource)
```

```objc
- (instancetype) initWithLocalizedName:(NSString *) localizedName deviceID:(NSUUID *) deviceID source:(id<CMIOExtensionDeviceSource>) source;
```

## Parameters

- `localizedName`: A localized name for the device.
- `deviceID`: A universally unique device identifier value.
- `source`: An extension-specific object that conforms to the [`CMIOExtensionDeviceSource`](../cmioextensiondevicesource.md) protocol.

## See Also

### Creating a Device
- [init(localizedName: String, deviceID: UUID, legacyDeviceID: String?, source: any CMIOExtensionDeviceSource)](./init%28localizedname,deviceid,legacydeviceid,source%29.md)
  Creates an extension device with an optional legacy device identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensiondevice/init(localizedname:deviceid:source:))*