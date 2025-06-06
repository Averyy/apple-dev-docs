# MatterAddDeviceExtensionRequestHandler.ThreadScanResult

**Framework**: MatterSupport  
**Kind**: struct

A result of a Thread-scan operation performed on the device

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct ThreadScanResult
```

#### Overview

Use one of these instances to create a [`MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation`](matteradddeviceextensionrequesthandler/threadnetworkassociation.md) as a possible Thread network for the device to join.

## Topics

### Creating the result
- [init(networkName: String, panID: UInt16, extendedPANID: UInt64, channel: UInt16, extendedAddress: Data, rssi: Int8, version: UInt8, linkQualityIndicator: UInt8)](matteradddeviceextensionrequesthandler/threadscanresult/init(networkname:panid:extendedpanid:channel:extendedaddress:rssi:version:linkqualityindicator:).md)
  Create the extension request handler.
### Getting result information
- [var channel: UInt16](matteradddeviceextensionrequesthandler/threadscanresult/channel.md)
  The Thread network radio channel.
- [var extendedAddress: Data](matteradddeviceextensionrequesthandler/threadscanresult/extendedaddress.md)
  The identifier of an active Thread network Border Agent.
- [var extendedPANID: UInt64](matteradddeviceextensionrequesthandler/threadscanresult/extendedpanid.md)
  The Thread network extended PAN identifier.
- [var linkQualityIndicator: UInt8](matteradddeviceextensionrequesthandler/threadscanresult/linkqualityindicator.md)
  A receive quality indicator, as specified by Matter specification.
- [var networkName: String](matteradddeviceextensionrequesthandler/threadscanresult/networkname.md)
  The Thread network name.
- [var panID: UInt16](matteradddeviceextensionrequesthandler/threadscanresult/panid.md)
  The Thread network PAN identifier.
- [var rssi: Int8](matteradddeviceextensionrequesthandler/threadscanresult/rssi.md)
  The observed RSSI of the network by the device.
- [var version: UInt8](matteradddeviceextensionrequesthandler/threadscanresult/version.md)
  The version field, as specified by the Matter specificaiton.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func selectThreadNetwork(from: [MatterAddDeviceExtensionRequestHandler.ThreadScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/selectthreadnetwork(from:).md)
  Provides the visible Thread networks to the device.
- [MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/threadnetworkassociation.md)
  The description of an association to a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadscanresult)*