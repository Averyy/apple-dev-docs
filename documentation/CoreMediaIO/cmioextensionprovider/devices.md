# devices

**Framework**: Core Media I/O  
**Kind**: property

An array of connected devices.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var devices: [CMIOExtensionDevice] { get }
```

#### Discussion

This property isn’t key-value observable.

## See Also

- [func addDevice(CMIOExtensionDevice) throws](cmioextensionprovider/adddevice(_:).md)
  Adds a device to a provider.
- [func removeDevice(CMIOExtensionDevice) throws](cmioextensionprovider/removedevice(_:).md)
  Removes a device from a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/devices)*