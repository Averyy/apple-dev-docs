# ASAccountAuthenticationModificationController

**Framework**: Authentication Services  
**Kind**: class

An object that performs a request to modify an account’s authentication properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASAccountAuthenticationModificationController
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Overview

> **Note**:  This class ignores calls from Mac apps built with Mac Catalyst.

 This class ignores calls from Mac apps built with Mac Catalyst.

## Topics

### Initiating Security Upgrades from Your App
- [func perform(ASAccountAuthenticationModificationRequest)](asaccountauthenticationmodificationcontroller/perform(_:).md)
  Performs a request to upgrade the authentication credentials for an account to a strong password, or to use Sign in with Apple.
- [class ASAccountAuthenticationModificationReplacePasswordWithSignInWithAppleRequest](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest.md)
  A request to upgrade from using a password to using Sign in with Apple.
- [class ASAccountAuthenticationModificationUpgradePasswordToStrongPasswordRequest](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest.md)
  A request to automatically upgrade from a weak password to a strong password.
- [class ASAccountAuthenticationModificationRequest](asaccountauthenticationmodificationrequest.md)
  A request to modify an account’s authentication properties.
### Configuring Requests
- [var presentationContextProvider: (any ASAccountAuthenticationModificationControllerPresentationContextProviding)?](asaccountauthenticationmodificationcontroller/presentationcontextprovider.md)
  An object that provides a presentation context for the account modification request’s user interface.
- [var delegate: (any ASAccountAuthenticationModificationControllerDelegate)?](asaccountauthenticationmodificationcontroller/delegate.md)
  An object that receives notifications about the request’s status.

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

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)
  Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.
- [class ASAccountAuthenticationModificationViewController](asaccountauthenticationmodificationviewcontroller.md)
  A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.
- [class ASAccountAuthenticationModificationExtensionContext](asaccountauthenticationmodificationextensioncontext.md)
  An object that you interact with to change an account’s password or to upgrade to Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontroller)*