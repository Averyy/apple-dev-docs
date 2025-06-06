# PKIssuerProvisioningExtensionStatus

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that indicates whether there are any payment cards available to add as Wallet passes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS ?+
- visionOS 1.0+

## Declaration

```swift
class PKIssuerProvisioningExtensionStatus
```

## Topics

### Creating an issuer extension provisioning status
- [init()](pkissuerprovisioningextensionstatus/init.md)
  Creates a new extension-handler status object.
### Reporting pass availability
- [var passEntriesAvailable: Bool](pkissuerprovisioningextensionstatus/passentriesavailable.md)
  A Boolean value that indicates whether a payment card is available to add to an iPhone.
- [var remotePassEntriesAvailable: Bool](pkissuerprovisioningextensionstatus/remotepassentriesavailable.md)
  A Boolean value that indicates whether a payment card is available to add to an Apple Watch.
### Reporting requirements for authentication
- [var requiresAuthentication: Bool](pkissuerprovisioningextensionstatus/requiresauthentication.md)
  A Boolean value that indicates whether adding a card requires an authorization-user-interface extension provided by your app.

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

- [func status(completion: (PKIssuerProvisioningExtensionStatus) -> Void)](pkissuerprovisioningextensionhandler/status(completion:).md)
  Reports the status of your Wallet extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkissuerprovisioningextensionstatus)*