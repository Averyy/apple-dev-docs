# ASAccountAuthenticationModificationRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A request to modify an account’s authentication properties.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASAccountAuthenticationModificationRequest
```

```objc
@interface ASAccountAuthenticationModificationRequest : NSObject
```

#### Overview

To initiate an account authentication modification request from your app, use either [`ASAccountAuthenticationModificationUpgradePasswordToStrongPasswordRequest`](./asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest.md) or [`ASAccountAuthenticationModificationReplacePasswordWithSignInWithAppleRequest`](./asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [ASAccountAuthenticationModificationReplacePasswordWithSignInWithAppleRequest](./asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest.md)
- [ASAccountAuthenticationModificationUpgradePasswordToStrongPasswordRequest](./asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Initiating Security Upgrades from Your App
- [func perform(ASAccountAuthenticationModificationRequest)](./asaccountauthenticationmodificationcontroller/perform%28_%29.md)
  Performs a request to upgrade the authentication credentials for an account to a strong password, or to use Sign in with Apple.
- [class ASAccountAuthenticationModificationReplacePasswordWithSignInWithAppleRequest](./asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest.md)
  A request to upgrade from using a password to using Sign in with Apple.
- [class ASAccountAuthenticationModificationUpgradePasswordToStrongPasswordRequest](./asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest.md)
  A request to automatically upgrade from a weak password to a strong password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationrequest)*