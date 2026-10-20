# ASExtensionLocalizedFailureReasonErrorKey

**Framework**: Authentication Services  
**Kind**: var  
**Role**: Global Variable

A key that specifies a string value to show to the user when a request fails.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
let ASExtensionLocalizedFailureReasonErrorKey: String
```

```c
extern NSErrorUserInfoKey const ASExtensionLocalizedFailureReasonErrorKey;
```

#### Discussion

When canceling a request, your extension calls [`cancelRequest(withError:)`](./asaccountauthenticationmodificationextensioncontext/cancelrequest%28witherror%29.md). The system informs the user that the request failed. To show additional information regarding the failure, use this key to set a string value in the error’s `userInfo` dictionary.

## See Also

### Handling Requests
- [func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple%28userinfo%29.md)
  Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.
- [func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest%28updatedcredential,userinfo%29.md)
  Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.
- [func getSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?, completionHandler: (ASAuthorizationAppleIDCredential?, (any Error)?) -> Void)](./asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization%28state,nonce,completionhandler%29.md)
  Retrieves the user’s current Sign in with Apple authorization credentials.
- [func cancelRequest(withError: any Error)](./asaccountauthenticationmodificationextensioncontext/cancelrequest%28witherror%29.md)
  Cancels a request with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asextensionlocalizedfailurereasonerrorkey)*