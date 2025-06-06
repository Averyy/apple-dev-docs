# protocolType

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

A custom universal type that describes the device’s manner of communication with the extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var protocolType: UTType { get set }
```

## See Also

- [var `protocol`: DDDevice.Protocol](dddevice/protocol-swift.property.md)
  The manner in which the system applies your app’s device discovery extension.
- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var bluetoothIdentifier: UUID?](dddevice/bluetoothidentifier.md)
  An identifier to communicate with the device through Bluetooth wireless technology.
- [var networkEndpoint: NWEndpoint?](dddevice/networkendpoint-3lah1.md)
  An object that describes a local-network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/protocoltype)*