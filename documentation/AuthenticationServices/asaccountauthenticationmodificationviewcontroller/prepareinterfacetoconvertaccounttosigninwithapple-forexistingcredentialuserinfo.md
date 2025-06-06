# prepareInterfaceToConvertAccountToSignInWithApple(for:existingCredential:userInfo:)

**Framework**: Authentication Services  
**Kind**: method

Prepares the view controller’s interface that displays when converting an account that uses password authentication to use Sign in with Apple.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareInterfaceToConvertAccountToSignInWithApple(for serviceIdentifier: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]? = nil)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Parameters

- `serviceIdentifier`: An identifier that represents a particular service that the user needs a credential for, like a web site.
- `existingCredential`: The current password credential for the service.
- `userInfo`: A dictionary that contains app-specific values when the request to upgrade to Sign in with Apple initiates from by the parent app. If the request to upgrade to Sign in with Apple doesn’t initiate from the app, this parameter is  .

## See Also

- [func convertAccountToSignInWithAppleWithoutUserInteraction(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationviewcontroller/convertaccounttosigninwithapplewithoutuserinteraction(for:existingcredential:userinfo:).md)
  Converts an account’s authentication mechanism from using passwords to using Sign in with Apple.
- [ASAccountAuthenticationModificationSupportsUpgradeToSignInWithApple](../BundleResources/Information-Property-List/NSExtension/ASAccountAuthenticationModificationSupportsUpgradeToSignInWithApple.md)
  A Boolean value that indicates whether the extension supports upgrading from using password authentication to using Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller/prepareinterfacetoconvertaccounttosigninwithapple(for:existingcredential:userinfo:))*