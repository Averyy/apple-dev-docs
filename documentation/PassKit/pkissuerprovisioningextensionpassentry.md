# PKIssuerProvisioningExtensionPassEntry

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that represents an item available to add to as a Wallet pass.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class PKIssuerProvisioningExtensionPassEntry
```

## Topics

### Information for displaying an addable card
- [var art: CGImage](pkissuerprovisioningextensionpassentry/art.md)
  An image to that the system displays to the user when they add or select the card.
- [var title: String](pkissuerprovisioningextensionpassentry/title.md)
  A name for the pass that the system displays to the user when they add or select the card.
- [var identifier: String](pkissuerprovisioningextensionpassentry/identifier.md)
  A developer-defined value you use to identify the card.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [PKIssuerProvisioningExtensionPaymentPassEntry](pkissuerprovisioningextensionpaymentpassentry.md)
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
- [class PKIssuerProvisioningExtensionPaymentPassEntry](pkissuerprovisioningextensionpaymentpassentry.md)
  An object that represents a payment card available to add as a payment pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionpassentry)*