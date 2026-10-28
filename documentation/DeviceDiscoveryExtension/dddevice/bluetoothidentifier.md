# bluetoothIdentifier

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

An identifier to communicate with the device through Bluetooth wireless technology.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
var bluetoothIdentifier: UUID? { get set }
```

```objc
@property (nonatomic, strong, readwrite, nullable) NSUUID * bluetoothIdentifier;
```

## Discussion

An extension may set this property to the Bluetooth identifier of a discovered [`CBPeripheral`](../../CoreBluetooth/cbperipheral.md).

## See Also

### Indicating the protocol
- [var `protocol`: DDDevice.Protocol](./protocol-swift.property.md)
  The manner in which the system applies your app’s device discovery extension.
- [DDDevice.Protocol](./protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var protocolType: UTType](./protocoltype.md)
  A custom universal type that describes the device’s manner of communication with the extension.
- [var networkEndpoint: NWEndpoint?](./networkendpoint-3lah1.md)
  An object that describes a local-network device.
- [networkEndpoint](./networkendpoint-7excg.md)
  An object that describes a local-network device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/bluetoothidentifier)*