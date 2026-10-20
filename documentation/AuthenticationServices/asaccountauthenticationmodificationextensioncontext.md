# ASAccountAuthenticationModificationExtensionContext

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

An object that you interact with to change an account’s password or to upgrade to Sign in with Apple.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASAccountAuthenticationModificationExtensionContext
```

```objc
@interface ASAccountAuthenticationModificationExtensionContext : NSExtensionContext
```

#### Overview

> **Note**:  This class ignores calls from Mac apps built with Mac Catalyst.

## Topics

### Handling Requests
- [func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple%28userinfo%29.md)
  Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.
- [func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest%28updatedcredential,userinfo%29.md)
  Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.
- [func getSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?, completionHandler: (ASAuthorizationAppleIDCredential?, (any Error)?) -> Void)](./asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization%28state,nonce,completionhandler%29.md)
  Retrieves the user’s current Sign in with Apple authorization credentials.
- [func cancelRequest(withError: any Error)](./asaccountauthenticationmodificationextensioncontext/cancelrequest%28witherror%29.md)
  Cancels a request with an error.
- [let ASExtensionLocalizedFailureReasonErrorKey: String](./asextensionlocalizedfailurereasonerrorkey.md)
  A key that specifies a string value to show to the user when a request fails.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/nsextensioncontext.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Automatic security upgrades
- [Upgrading Account Security With an Account Authentication Modification Extension](./upgrading-account-security-with-an-account-authentication-modification-extension.md)
  Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.
- [class ASAccountAuthenticationModificationController](./asaccountauthenticationmodificationcontroller.md)
  An object that performs a request to modify an account’s authentication properties.
- [class ASAccountAuthenticationModificationViewController](./asaccountauthenticationmodificationviewcontroller.md)
  A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext)*