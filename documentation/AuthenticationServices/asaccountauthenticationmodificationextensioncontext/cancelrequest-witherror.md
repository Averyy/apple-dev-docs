# cancelRequest(withError:)

**Framework**: Authentication Services  
**Kind**: method

Cancels a request with an error.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func cancelRequest(withError error: any Error)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Discussion

If the user cancels the request, use the [`ASExtensionError.Code.userCanceled`](asextensionerror/code/usercanceled.md) error code in the `error`. If the request requires user interaction, use [`ASExtensionError.Code.userInteractionRequired`](asextensionerror/code/userinteractionrequired.md) instead.

To include additional information regarding the failure, use [`ASExtensionLocalizedFailureReasonErrorKey`](asextensionlocalizedfailurereasonerrorkey.md) to set a string value in the error’s `userInfo` dictionary. The system displays this string value to the user.

## Parameters

- `error`: An error that indicates the reason for the canceled request.

## See Also

- [func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple(userinfo:).md)
  Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.
- [func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest(updatedcredential:userinfo:).md)
  Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.
- [func getSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?, completionHandler: (ASAuthorizationAppleIDCredential?, (any Error)?) -> Void)](asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization(state:nonce:completionhandler:).md)
  Retrieves the user’s current Sign in with Apple authorization credentials.
- [let ASExtensionLocalizedFailureReasonErrorKey: String](asextensionlocalizedfailurereasonerrorkey.md)
  A key that specifies a string value to show to the user when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext/cancelrequest(witherror:))*