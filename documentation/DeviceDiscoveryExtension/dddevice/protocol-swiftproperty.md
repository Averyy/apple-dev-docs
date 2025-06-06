# protocol

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

The manner in which the system applies your app’s device discovery extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var `protocol`: DDDevice.Protocol { get set }
```

#### Discussion

The value is [`DDDevice.Protocol.dial`](dddevice/protocol-swift.enum/dial.md) for the discovery of third-party media receivers.

## See Also

- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var protocolType: UTType](dddevice/protocoltype.md)
  A custom universal type that describes the device’s manner of communication with the extension.
- [var bluetoothIdentifier: UUID?](dddevice/bluetoothidentifier.md)
  An identifier to communicate with the device through Bluetooth wireless technology.
- [var networkEndpoint: NWEndpoint?](dddevice/networkendpoint-3lah1.md)
  An object that describes a local-network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/protocol-swift.property)*