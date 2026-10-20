# removeDevice(_:)

**Framework**: Core Media I/O  
**Kind**: method  
**Role**: Instance Method

Removes a device from a provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func removeDevice(_ device: CMIOExtensionDevice) throws
```

```objc
- (BOOL) removeDevice:(CMIOExtensionDevice *) device error:(NSError **) outError;
```

## Parameters

- `device`: A device to remove from a provider.

## See Also

### Managing Devices
- [var devices: [CMIOExtensionDevice]](./devices.md)
  An array of connected devices.
- [func addDevice(CMIOExtensionDevice) throws](./adddevice%28_%29.md)
  Adds a device to a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/removedevice(_:))*