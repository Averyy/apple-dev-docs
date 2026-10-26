# protocolType

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

A custom universal type that describes the device’s manner of communication with the extension.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
var protocolType: UTType { get set }
```

```objc
@property (nonatomic, strong, readwrite) UTType * protocolType;
```

## See Also

### Indicating the protocol
- [var `protocol`: DDDevice.Protocol](./protocol-swift.property.md)
  The manner in which the system applies your app’s device discovery extension.
- [DDDevice.Protocol](./protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var bluetoothIdentifier: UUID?](./bluetoothidentifier.md)
  An identifier to communicate with the device through Bluetooth wireless technology.
- [var networkEndpoint: NWEndpoint?](./networkendpoint-3lah1.md)
  An object that describes a local-network device.
- [networkEndpoint](./networkendpoint-7excg.md)
  An object that describes a local-network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/protocoltype)*