# addDevice(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Adds a device to a provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func addDevice(_ device: CMIOExtensionDevice) throws
```

```objc
- (BOOL) addDevice:(CMIOExtensionDevice *) device error:(NSError **) outError;
```

## Parameters

- `device`: A device to add to a provider.

## See Also

### Managing Devices
- [var devices: [CMIOExtensionDevice]](./devices.md)
  An array of connected devices.
- [func removeDevice(CMIOExtensionDevice) throws](./removedevice%28_%29.md)
  Removes a device from a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/adddevice(_:))*