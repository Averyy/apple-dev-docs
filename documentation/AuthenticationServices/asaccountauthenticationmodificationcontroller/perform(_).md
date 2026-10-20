# perform(_:)

**Framework**: Authentication Services  
**Kind**: method

Performs a request to upgrade the authentication credentials for an account to a strong password, or to use Sign in with Apple.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func perform(_ request: ASAccountAuthenticationModificationRequest)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Discussion

Only one request can be in progress at a time. If a request is already in progress, additional requests fail immediately.

## Parameters

- `request`: The request to perform.

## See Also

- [class ASAccountAuthenticationModificationReplacePasswordWithSignInWithAppleRequest](asaccountauthenticationmodificationreplacepasswordwithsigninwithapplerequest.md)
  A request to upgrade from using a password to using Sign in with Apple.
- [class ASAccountAuthenticationModificationUpgradePasswordToStrongPasswordRequest](asaccountauthenticationmodificationupgradepasswordtostrongpasswordrequest.md)
  A request to automatically upgrade from a weak password to a strong password.
- [class ASAccountAuthenticationModificationRequest](asaccountauthenticationmodificationrequest.md)
  A request to modify an account’s authentication properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationcontroller/perform(_:))*