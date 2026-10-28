# network(extendedPANID:)

**Framework**: MatterSupport  
**Kind**: method  
**Role**: Type Method

Obtains the Thread network extended PAN identifier.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
static func network(extendedPANID: UInt64) -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation
```

## Return Value

The Thread network extended PAN identifier.

## Discussion

The system retrieves the network parameters from [`retrieveCredentials(forExtendedPANID:completion:)`](../../../ThreadNetwork/thclient/retrievecredentials%28forextendedpanid,completion%29.md) using the provided parameter. The credentials must be present in the store or else association and pairing fails.

## See Also

### Getting network information
- [static var defaultSystemNetwork: MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](./defaultsystemnetwork.md)
  A sentinel value to represent the system’s default Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadnetworkassociation/network(extendedpanid:))*