# devices

**Framework**: Core Media I/O  
**Kind**: property  
**Role**: Instance Property

An array of connected devices.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
var devices: [CMIOExtensionDevice] { get }
```

```objc
@property (atomic, copy, readonly) NSArray<CMIOExtensionDevice *> * devices;
```

#### Discussion

This property isn’t key-value observable.

## See Also

### Managing Devices
- [func addDevice(CMIOExtensionDevice) throws](./adddevice%28_%29.md)
  Adds a device to a provider.
- [func removeDevice(CMIOExtensionDevice) throws](./removedevice%28_%29.md)
  Removes a device from a provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionprovider/devices)*