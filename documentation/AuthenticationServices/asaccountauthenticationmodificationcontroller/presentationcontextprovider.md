# presentationContextProvider

**Framework**: Authentication Services  
**Kind**: property

An object that provides a presentation context for the account modification request’s user interface.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var presentationContextProvider: (any ASAccountAuthenticationModificationControllerPresentationContextProviding)? { get set }
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

## See Also

- [var delegate: (any ASAccountAuthenticationModificationControllerDelegate)?](asaccountauthenticationmodificationcontroller/delegate.md)
  An object that receives notifications about the request’s status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontroller/presentationcontextprovider)*