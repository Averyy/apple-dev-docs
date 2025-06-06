# getSignInWithAppleUpgradeAuthorization(state:nonce:completionHandler:)

**Framework**: Authentication Services  
**Kind**: method

Retrieves the user’s current Sign in with Apple authorization credentials.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func requestSignInWithAppleUpgradeAuthorization(state: String?, nonce: String?) async throws -> ASAuthorizationAppleIDCredential
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Discussion

Calling this method causes the system to present the Sign in with Apple upgrade interface, dismissing any currently presented interface.

For more information about the `state` and `nonce` parameters, see doc://com.apple.documentation/documentation/sign_in_with_apple/sign_in_with_apple_rest_api/authenticating_users_with_sign_in_with_apple and [`Get the most out of Sign in with Apple`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10173/).

## Parameters

- `state`: A string that contains a random value for verifying the Sign in with Apple credentials.
- `nonce`: A string that contains a random value for verifying the Sign in with Apple credentials.
- `completionHandler`: A closure that takes a parameter for the user’s current Sign in with Apple credentials, and an error if one occurs while retrieving them.

## See Also

- [func completeUpgradeToSignInWithApple(userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completeupgradetosigninwithapple(userinfo:).md)
  Completes the process of upgrading an account’s authentication credentials from using passwords to using Sign in with Apple.
- [func completeChangePasswordRequest(updatedCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationextensioncontext/completechangepasswordrequest(updatedcredential:userinfo:).md)
  Completes a request to update an account’s authentication credentials from using a weak password to using a strong password.
- [func cancelRequest(withError: any Error)](asaccountauthenticationmodificationextensioncontext/cancelrequest(witherror:).md)
  Cancels a request with an error.
- [let ASExtensionLocalizedFailureReasonErrorKey: String](asextensionlocalizedfailurereasonerrorkey.md)
  A key that specifies a string value to show to the user when a request fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationextensioncontext/getsigninwithappleupgradeauthorization(state:nonce:completionhandler:))*