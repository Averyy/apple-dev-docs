# PKIssuerProvisioningExtensionPaymentPassEntry

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents a payment card available to add as a payment pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class PKIssuerProvisioningExtensionPaymentPassEntry
```

## Topics

### Creating a payment pass entry
- [init?(identifier: String, title: String, art: CGImage, addRequestConfiguration: PKAddPaymentPassRequestConfiguration)](pkissuerprovisioningextensionpaymentpassentry/init(identifier:title:art:addrequestconfiguration:).md)
  Creates a new entry for a payment pass that a user adds to Wallet.
### Getting the pass entry configuration
- [var addRequestConfiguration: PKAddPaymentPassRequestConfiguration](pkissuerprovisioningextensionpaymentpassentry/addrequestconfiguration.md)
  The configuration that the system uses to add a payment pass.

## Relationships

### Inherits From
- [PKIssuerProvisioningExtensionPassEntry](pkissuerprovisioningextensionpassentry.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func passEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](pkissuerprovisioningextensionhandler/passentries(completion:).md)
  Reports the list of passes available to add to an iPhone.
- [func remotePassEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](pkissuerprovisioningextensionhandler/remotepassentries(completion:).md)
  Reports the list of passes available to add to an Apple Watch.
- [class PKIssuerProvisioningExtensionPassEntry](pkissuerprovisioningextensionpassentry.md)
  An object that represents an item available to add to as a Wallet pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionpaymentpassentry)*