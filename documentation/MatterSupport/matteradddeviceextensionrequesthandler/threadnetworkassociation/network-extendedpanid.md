# network(extendedPANID:)

**Framework**: MatterSupport  
**Kind**: method

Obtains the Thread network extended PAN identifier.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
static func network(extendedPANID: UInt64) -> MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation
```

#### Return Value

The Thread network extended PAN identifier.

#### Discussion

The system retrieves the network parameters from [`retrieveCredentials(forExtendedPANID:completion:)`](https://developer.apple.com/documentation/ThreadNetwork/THClient/retrieveCredentials(forExtendedPANID:completion:)) using the provided parameter. The credentials must be present in the store or else association and pairing fails.

## See Also

- [static var defaultSystemNetwork: MatterAddDeviceExtensionRequestHandler.ThreadNetworkAssociation](matteradddeviceextensionrequesthandler/threadnetworkassociation/defaultsystemnetwork.md)
  A sentinel value to represent the system’s default Thread network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/threadnetworkassociation/network(extendedpanid:))*