# completeChangePasswordRequest(updatedCredential:userInfo:)

**Framework**: Authentication Services  
**Kind**: method

Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]? = nil)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Discussion

To receive the `userInfo` dictionary in your app, set a delegate on the [`ASAccountAuthenticationModificationController`](asaccountauthenticationmodificationcontroller.md) when initiating the request. The delegate receives the `userInfo` dictionary as a parameter to [`accountAuthenticationModificationController(_:didSuccessfullyComplete:userInfo:)`](asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller(_:didsuccessfullycomplete:userinfo:).md).

## Parameters

- `updatedCredential`: The new credentials to store in the user’s keychain.
- `userInfo`: A dictionary that contains details to pass to the extension’s containing app if the app initiated the account modification request.

## See Also

- [func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple(userinfo:).md)
  Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.
- [func getSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?, completionHandler: (ASAuthorizationAppleIDCredential?, (any Error)?) -> Void)](asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization(state:nonce:completionhandler:).md)
  Retrieves the user’s current Sign in with Apple authorization credentials.
- [func cancelRequest(withError: any Error)](asaccountauthenticationmodificationextensioncontext/cancelrequest(witherror:).md)
  Cancels a request with an error.
- [let ASExtensionLocalizedFailureReasonErrorKey: String](asextensionlocalizedfailurereasonerrorkey.md)
  A key that specifies a string value to show to the user when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest(updatedcredential:userinfo:))*