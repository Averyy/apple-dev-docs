# removeDevice(_:)

**Framework**: Core Media I/O  
**Kind**: method

Removes a device from a provider.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func removeDevice(_ device: CMIOExtensionDevice) throws
```

## Parameters

- `device`: A device to remove from a provider.

## See Also

- [var devices: [CMIOExtensionDevice]](cmioextensionprovider/devices.md)
  An array of connected devices.
- [func addDevice(CMIOExtensionDevice) throws](cmioextensionprovider/adddevice(_:).md)
  Adds a device to a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/removedevice(_:))*