# bluetoothIdentifier

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

An identifier to communicate with the device through Bluetooth wireless technology.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
var bluetoothIdentifier: UUID? { get set }
```

#### Discussion

An extension may set this property to the Bluetooth identifier of a discovered [`CBPeripheral`](https://developer.apple.com/documentation/CoreBluetooth/CBPeripheral).

## See Also

- [var `protocol`: DDDevice.Protocol](dddevice/protocol-swift.property.md)
  The manner in which the system applies your app’s device discovery extension.
- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var protocolType: UTType](dddevice/protocoltype.md)
  A custom universal type that describes the device’s manner of communication with the extension.
- [var networkEndpoint: NWEndpoint?](dddevice/networkendpoint-3lah1.md)
  An object that describes a local-network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/bluetoothidentifier)*