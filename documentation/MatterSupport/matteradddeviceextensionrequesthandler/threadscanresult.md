# MatterAddDeviceExtensionRequestHandler.ThreadScanResult

**Framework**: MatterSupport  
**Kind**: struct  
**Role**: Structure

A result of a Thread-scan operation performed on the device

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct ThreadScanResult
```

## Overview

Use one of these instances to create a [`MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation`](./threadnetworkassociation.md) as a possible Thread network for the device to join.

## Topics

### Creating the result
- [init(networkName: String, panID: UInt16, extendedPANID: UInt64, channel: UInt16, extendedAddress: Data, rssi: Int8, version: UInt8, linkQualityIndicator: UInt8)](./threadscanresult/init%28networkname,panid,extendedpanid,channel,extendedaddress,rssi,version,linkqualityindicator%29.md)
  Create the extension request handler.
### Getting result information
- [var channel: UInt16](./threadscanresult/channel.md)
  The Thread network radio channel.
- [var extendedAddress: Data](./threadscanresult/extendedaddress.md)
  The identifier of an active Thread network Border Agent.
- [var extendedPANID: UInt64](./threadscanresult/extendedpanid.md)
  The Thread network extended PAN identifier.
- [var linkQualityIndicator: UInt8](./threadscanresult/linkqualityindicator.md)
  A receive quality indicator, as specified by Matter specification.
- [var networkName: String](./threadscanresult/networkname.md)
  The Thread network name.
- [var panID: UInt16](./threadscanresult/panid.md)
  The Thread network PAN identifier.
- [var rssi: Int8](./threadscanresult/rssi.md)
  The observed RSSI of the network by the device.
- [var version: UInt8](./threadscanresult/version.md)
  The version field, as specified by the Matter specification.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Selecting the Thread network
- [func selectThreadNetwork(from: [MatterAddDeviceExtensionRequestHandler.ThreadScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](./selectthreadnetwork%28from%29.md)
  Provides the visible Thread networks to the device.
- [MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](./threadnetworkassociation.md)
  The description of an association to a Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadscanresult)*