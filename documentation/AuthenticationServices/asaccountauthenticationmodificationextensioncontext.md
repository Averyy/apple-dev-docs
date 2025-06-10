# ASAccountAuthenticationModificationExtensionContext

**Framework**: Authentication Services  
**Kind**: class

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

#### Overview

> **Note**:  This class ignores calls from Mac apps built with Mac Catalyst.

## Topics

### Handling Requests
- [func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple(userinfo:).md)
  Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.
- [func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest(updatedcredential:userinfo:).md)
  Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.
- [func getSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?, completionHandler: (ASAuthorizationAppleIDCredential?, (any Error)?) -> Void)](asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization(state:nonce:completionhandler:).md)
  Retrieves the user’s current Sign in with Apple authorization credentials.
- [func cancelRequest(withError: any Error)](asaccountauthenticationmodificationextensioncontext/cancelrequest(witherror:).md)
  Cancels a request with an error.
- [let ASExtensionLocalizedFailureReasonErrorKey: String](asextensionlocalizedfailurereasonerrorkey.md)
  A key that specifies a string value to show to the user when a request fails.

## Relationships

### Inherits From
- [NSExtensionContext](../Foundation/NSExtensionContext.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)
  Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.
- [class ASAccountAuthenticationModificationController](asaccountauthenticationmodificationcontroller.md)
  An object that performs a request to modify an account’s authentication properties.
- [class ASAccountAuthenticationModificationViewController](asaccountauthenticationmodificationviewcontroller.md)
  A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext)*