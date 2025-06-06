# ASExtensionLocalizedFailureReasonErrorKey

**Framework**: Authentication Services  
**Kind**: var

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

#### Discussion

When canceling a request, your extension calls [`cancelRequest(withError:)`](asaccountauthenticationmodificationextensioncontext/cancelrequest(witherror:).md). The system informs the user that the request failed. To show additional information regarding the failure, use this key to set a string value in the error’s `userInfo` dictionary.

## See Also

- [func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple(userinfo:).md)
  Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.
- [func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest(updatedcredential:userinfo:).md)
  Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.
- [func getSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?, completionHandler: (ASAuthorizationAppleIDCredential?, (any Error)?) -> Void)](asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization(state:nonce:completionhandler:).md)
  Retrieves the user’s current Sign in with Apple authorization credentials.
- [func cancelRequest(withError: any Error)](asaccountauthenticationmodificationextensioncontext/cancelrequest(witherror:).md)
  Cancels a request with an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asextensionlocalizedfailurereasonerrorkey)*