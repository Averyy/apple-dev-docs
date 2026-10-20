# convertAccountToSignInWithAppleWithoutUserInteraction(for:existingCredential:userInfo:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Converts an account’s authentication mechanism from using passwords to using Sign in with Apple.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
func convertAccountToSignInWithAppleWithoutUserInteraction(for serviceIdentifier: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]? = nil)
```

```objc
- (void) convertAccountToSignInWithAppleWithoutUserInteractionForServiceIdentifier:(ASCredentialServiceIdentifier *) serviceIdentifier existingCredential:(ASPasswordCredential *) existingCredential userInfo:(NSDictionary *) userInfo;
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](../upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Parameters

- `serviceIdentifier`: An identifier that represents a particular service that the user needs a credential for, like a web site.
- `existingCredential`: The current password credential for the service.
- `userInfo`: A dictionary that contains app-specific values when the request to upgrade to Sign in with Apple initiates from the parent app. If the request to upgrade to Sign in with Apple doesn’t initiate from the app, this parameter is `nil`.

## See Also

### Upgrading to Sign in with Apple
- [func prepareInterfaceToConvertAccountToSignInWithApple(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](./prepareinterfacetoconvertaccounttosigninwithapple%28for,existingcredential,userinfo%29.md)
  Prepares the view controller’s interface that displays when converting an account that uses password authentication to use Sign in with Apple.
- [ASAccountAuthenticationModificationSupportsUpgradeToSignInWithApple](../../BundleResources/information-property-list/nsextension/asaccountauthenticationmodificationsupportsupgradetosigninwithapple.md)
  A Boolean value that indicates whether the extension supports upgrading from using password authentication to using Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller/convertaccounttosigninwithapplewithoutuserinteraction(for:existingcredential:userinfo:))*