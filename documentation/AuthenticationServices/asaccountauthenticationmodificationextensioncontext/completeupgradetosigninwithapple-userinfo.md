# completeUpgradeToSignInWithApple(userInfo:)

**Framework**: Authentication Services  
**Kind**: method

Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]? = nil)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Discussion

After successfully upgrading to Sign in with Apple, the system deletes the password credentials from the keychain.

To receive the `userInfo` dictionary in your app, set a delegate on the [`ASAccountAuthenticationModificationController`](asaccountauthenticationmodificationcontroller.md) when initiating the request. The delegate receives the `userInfo` dictionary as a parameter to [`accountAuthenticationModificationController(_:didSuccessfullyComplete:userInfo:)`](asaccountauthenticationmodificationcontrollerdelegate/accountauthenticationmodificationcontroller(_:didsuccessfullycomplete:userinfo:).md).

## Parameters

- `userInfo`: A dictionary that contains details to pass to the extension’s containing app if the app initiated the account modification request.

## See Also

- [func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest(updatedcredential:userinfo:).md)
  Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.
- [func getSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?, completionHandler: (ASAuthorizationAppleIDCredential?, (any Error)?) -> Void)](asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization(state:nonce:completionhandler:).md)
  Retrieves the user’s current Sign in with Apple authorization credentials.
- [func cancelRequest(withError: any Error)](asaccountauthenticationmodificationextensioncontext/cancelrequest(witherror:).md)
  Cancels a request with an error.
- [let ASExtensionLocalizedFailureReasonErrorKey: String](asextensionlocalizedfailurereasonerrorkey.md)
  A key that specifies a string value to show to the user when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple(userinfo:))*