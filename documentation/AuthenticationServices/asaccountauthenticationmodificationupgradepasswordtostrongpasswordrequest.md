# ASAccountAuthenticationModificationUpgradePasswordToStrongPasswordRequest

**Framework**: Authentication Services  
**Kind**: class

A request to automatically upgrade from a weak password to a strong password.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASAccountAuthenticationModificationUpgradePasswordToStrongPasswordRequest
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Overview

Your app uses this class to initiate an upgrade from a weak password to a strong system-generated one. After creating the request, your app initiates the upgrade process by instantiating an [`ASAccountAuthenticationModificationController`](asaccountauthenticationmodificationcontroller.md) object and calling [`perform(_:)`](asaccountauthenticationmodificationcontroller/perform(_:).md) on it. The system invokes your authentication modification extension to complete the upgrade.

For details about how to enforce requirements on the password, such as minimum length or requiring both letters and numbers, see [`ASAccountAuthenticationModificationPasswordGenerationRequirements`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/ASAccountAuthenticationModificationPasswordGenerationRequirements).

## Topics

### Creating Upgrade Requests in Your App
- [init(user: String, serviceIdentifier: ASCredentialServiceIdentifier, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/init(user:serviceidentifier:userinfo:).md)
  Creates a request to upgrade from using a weak password to using a strong system-generated password.
- [var user: String](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/user.md)
  The user name of the account to upgrade.
- [var serviceIdentifier: ASCredentialServiceIdentifier](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/serviceidentifier.md)
  An identifier that represents a particular service that the user needs a credential for, like a web site.
- [var userInfo: [AnyHashable : Any]?](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest/userinfo.md)
  A dictionary that contains values to pass to your account modification extension.

## Relationships

### Inherits From
- [ASAccountAuthenticationModificationRequest](asaccountauthenticationmodificationrequest.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func perform(ASAccountAuthenticationModificationRequest)](asaccountauthenticationmodificationcontroller/perform(_:).md)
  Performs a request to upgrade the authentication credentials for an account to a strong password, or to use Sign in with Apple.
- [class ASAccountAuthenticationModificationReplacePasswordWithSignInWithAppleRequest](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest.md)
  A request to upgrade from using a password to using Sign in with Apple.
- [class ASAccountAuthenticationModificationRequest](asaccountauthenticationmodificationrequest.md)
  A request to modify an account’s authentication properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest)*