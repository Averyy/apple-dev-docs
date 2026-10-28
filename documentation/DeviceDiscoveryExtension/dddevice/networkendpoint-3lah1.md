# networkEndpoint

**Framework**: DeviceDiscoveryExtension  
**Kind**: property  
**Role**: Instance Property

An object that describes a local-network device.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst
- macOS 13.0+
- visionOS

## Declaration

```swift
var networkEndpoint: NWEndpoint? { get set }
```

## Discussion

For the discovery of local-network devices, the extension sets the value of this property to the [`endpoint`](../../Network/nwbrowser/result/endpoint.md) of an [`NWBrowser.Result`](../../Network/nwbrowser/result.md). When a search over the local network succeeds, the browser passes the newly discovered device into your extension’s [`browseResultsChangedHandler`](../../Network/nwbrowser/browseresultschangedhandler.md).

## See Also

### Indicating the protocol
- [var `protocol`: DDDevice.Protocol](./protocol-swift.property.md)
  The manner in which the system applies your app’s device discovery extension.
- [DDDevice.Protocol](./protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var protocolType: UTType](./protocoltype.md)
  A custom universal type that describes the device’s manner of communication with the extension.
- [var bluetoothIdentifier: UUID?](./bluetoothidentifier.md)
  An identifier to communicate with the device through Bluetooth wireless technology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/networkendpoint-3lah1)*