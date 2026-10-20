# MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation

**Framework**: MatterSupport  
**Kind**: struct  
**Role**: Structure

The description of an association to a Thread network.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct ThreadNetworkAssociation
```

## Topics

### Getting network information
- [static var defaultSystemNetwork: MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](./threadnetworkassociation/defaultsystemnetwork.md)
  A sentinel value to represent the system’s default Thread network.
- [static func network(extendedPANID: UInt64) -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](./threadnetworkassociation/network%28extendedpanid%29.md)
  Obtains the Thread network extended PAN identifier.

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
- [MatterAddDeviceExtensionRequestHandler.ThreadScanResult](./threadscanresult.md)
  A result of a Thread-scan operation performed on the device


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadnetworkassociation)*