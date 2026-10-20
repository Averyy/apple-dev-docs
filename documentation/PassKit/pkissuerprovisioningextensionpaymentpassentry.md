# PKIssuerProvisioningExtensionPaymentPassEntry

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that represents a payment card available to add as a payment pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
class PKIssuerProvisioningExtensionPaymentPassEntry
```

```objc
@interface PKIssuerProvisioningExtensionPaymentPassEntry : PKIssuerProvisioningExtensionPassEntry
```

## Topics

### Creating a payment pass entry
- [init?(identifier: String, title: String, art: CGImage, addRequestConfiguration: PKAddPaymentPassRequestConfiguration)](./pkissuerprovisioningextensionpaymentpassentry/init%28identifier,title,art,addrequestconfiguration%29.md)
  Creates a new entry for a payment pass that a user adds to Wallet.
### Getting the pass entry configuration
- [var addRequestConfiguration: PKAddPaymentPassRequestConfiguration](./pkissuerprovisioningextensionpaymentpassentry/addrequestconfiguration.md)
  The configuration that the system uses to add a payment pass.

## Relationships

### Inherits From
- [PKIssuerProvisioningExtensionPassEntry](./pkissuerprovisioningextensionpassentry.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Returning available passes
- [func passEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](./pkissuerprovisioningextensionhandler/passentries%28completion%29.md)
  Reports the list of passes available to add to an iPhone.
- [func remotePassEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](./pkissuerprovisioningextensionhandler/remotepassentries%28completion%29.md)
  Reports the list of passes available to add to an Apple Watch.
- [class PKIssuerProvisioningExtensionPassEntry](./pkissuerprovisioningextensionpassentry.md)
  An object that represents an item available to add to as a Wallet pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionpaymentpassentry)*