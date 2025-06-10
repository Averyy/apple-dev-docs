# MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation

**Framework**: MatterSupport  
**Kind**: struct

The description of an association to a Thread network.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct ThreadNetworkAssociation
```

## Topics

### Getting network information
- [static var defaultSystemNetwork: MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/threadnetworkassociation/defaultsystemnetwork.md)
  A sentinel value to represent the system’s default Thread network.
- [static func network(extendedPANID: UInt64) -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/threadnetworkassociation/network(extendedpanid:).md)
  Obtains the Thread network extended PAN identifier.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func selectThreadNetwork(from: [MatterAddDeviceExtensionRequestHandler.ThreadScanResult]) async throws -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/selectthreadnetwork(from:).md)
  Provides the visible Thread networks to the device.
- [MatterAddDeviceExtensionRequestHandler.ThreadScanResult](matteradddeviceextensionrequesthandler/threadscanresult.md)
  A result of a Thread-scan operation performed on the device


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadnetworkassociation)*