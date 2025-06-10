# PKIssuerProvisioningExtensionHandler

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An abstract superclass for an app extension to add a payment card to Wallet.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class PKIssuerProvisioningExtensionHandler
```

#### Overview

The principal class of your app’s extension target must be a subclass of `PKIssuerProvisioningExtensionHandler`.

Your app must be installed and the user open the app at least once for the system to call the extension handler.

> ❗ **Important**:  Before you can add a payment card provisioning extension you need an entitlement from Apple. For more information on requesting an entitlement, contact apple-pay-inquiries@apple.com.

## Topics

### Returning extension status
- [func status(completion: (PKIssuerProvisioningExtensionStatus) -> Void)](pkissuerprovisioningextensionhandler/status(completion:).md)
  Reports the status of your Wallet extension.
- [class PKIssuerProvisioningExtensionStatus](pkissuerprovisioningextensionstatus.md)
  An object that indicates whether there are any payment cards available to add as Wallet passes.
### Returning available passes
- [func passEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](pkissuerprovisioningextensionhandler/passentries(completion:).md)
  Reports the list of passes available to add to an iPhone.
- [func remotePassEntries(completion: ([PKIssuerProvisioningExtensionPassEntry]) -> Void)](pkissuerprovisioningextensionhandler/remotepassentries(completion:).md)
  Reports the list of passes available to add to an Apple Watch.
- [class PKIssuerProvisioningExtensionPassEntry](pkissuerprovisioningextensionpassentry.md)
  An object that represents an item available to add to as a Wallet pass.
- [class PKIssuerProvisioningExtensionPaymentPassEntry](pkissuerprovisioningextensionpaymentpassentry.md)
  An object that represents a payment card available to add as a payment pass.
### Returning information for adding a pass
- [func generateAddPaymentPassRequestForPassEntryWithIdentifier(String, configuration: PKAddPaymentPassRequestConfiguration, certificateChain: [Data], nonce: Data, nonceSignature: Data, completionHandler: (PKAddPaymentPassRequest?) -> Void)](pkissuerprovisioningextensionhandler/generateaddpaymentpassrequestforpassentrywithidentifier(_:configuration:certificatechain:nonce:noncesignature:completionhandler:).md)
  Creates an object with the data the system needs to add a card to Apple Pay.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Implementing Wallet Extensions](implementing-wallet-extensions.md)
  Support adding an issued card to Apple Pay from directly within Apple Wallet using Wallet Extensions.
- [protocol PKIssuerProvisioningExtensionAuthorizationProviding](pkissuerprovisioningextensionauthorizationproviding.md)
  A protocol for a UI app extension to authorize a user to add a payment card to Wallet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionhandler)*