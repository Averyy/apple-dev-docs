# networkEndpoint

**Framework**: DeviceDiscoveryExtension  
**Kind**: property

An object that describes a local-network device.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
var networkEndpoint: NWEndpoint? { get set }
```

#### Discussion

For the discovery of local-network devices, the extension sets the value of this property to the [`endpoint`](https://developer.apple.com/documentation/Network/NWBrowser/Result/endpoint) of an [`NWBrowser.Result`](https://developer.apple.com/documentation/Network/NWBrowser/Result). When a search over the local network succeeds, the browser passes the newly discovered device into your extension’s [`browseResultsChangedHandler`](https://developer.apple.com/documentation/Network/NWBrowser/browseResultsChangedHandler).

## See Also

- [var `protocol`: DDDevice.Protocol](dddevice/protocol-swift.property.md)
  The manner in which the system applies your app’s device discovery extension.
- [DDDevice.Protocol](dddevice/protocol-swift.enum.md)
  An identifier for the manner in which an app interacts with a device.
- [var protocolType: UTType](dddevice/protocoltype.md)
  A custom universal type that describes the device’s manner of communication with the extension.
- [var bluetoothIdentifier: UUID?](dddevice/bluetoothidentifier.md)
  An identifier to communicate with the device through Bluetooth wireless technology.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicediscoveryextension/dddevice/networkendpoint-3lah1)*