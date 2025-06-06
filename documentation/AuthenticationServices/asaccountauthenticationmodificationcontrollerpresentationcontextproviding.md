# ASAccountAuthenticationModificationControllerPresentationContextProviding

**Framework**: Authentication Services  
**Kind**: protocol

An interface you implement to coordinate presentation of the user interface when modifying an account’s authentication properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol ASAccountAuthenticationModificationControllerPresentationContextProviding : NSObjectProtocol
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Topics

### Presenting the Account Modification Interface
- [func presentationAnchor(for: ASAccountAuthenticationModificationController) -> ASPresentationAnchor](asaccountauthenticationmodificationcontrollerpresentationcontextproviding/presentationanchor(for:).md)
  Returns the most appropriate window for presenting the authentication modification interface.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func cancelRequest()](asaccountauthenticationmodificationviewcontroller/cancelrequest.md)
  Cancels a request that the user initiated.
- [protocol ASAccountAuthenticationModificationControllerDelegate](asaccountauthenticationmodificationcontrollerdelegate.md)
  An interface you implement for receiving success and failure statuses about modification of an account’s authentication properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontrollerpresentationcontextproviding)*