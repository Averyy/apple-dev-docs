# prepareInterfaceToChangePassword(for:existingCredential:newPassword:userInfo:)

**Framework**: Authentication Services  
**Kind**: method

Prepares the view controller’s interface that displays when upgrading from a weak password to a strong password.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareInterfaceToChangePassword(for serviceIdentifier: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, newPassword: String, userInfo: [AnyHashable : Any]? = nil)
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Discussion

If the extension’s `Info.plist` file includes the [`ASAccountAuthenticationModificationPasswordGenerationRequirements`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension/ASAccountAuthenticationModificationPasswordGenerationRequirements) key, the value of `newPassword` satisfies the specified requirements.

## Parameters

- `serviceIdentifier`: An identifier that represents a particular service that the user needs a credential for, like a web site.
- `existingCredential`: The current password credential for the service.
- `newPassword`: A new, automatically generated, strong password for the service to use.
- `userInfo`: A dictionary that contains app-specific values when the request to upgrade to Sign in with Apple initiates from by the parent app. If the request to upgrade to Sign in with Apple doesn’t initiate from the app, this parameter is  .

## See Also

- [func changePasswordWithoutUserInteraction(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, newPassword: String, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationviewcontroller/changepasswordwithoutuserinteraction(for:existingcredential:newpassword:userinfo:).md)
  Upgrades a user’s weak password to a strong password.
- [ASAccountAuthenticationModificationSupportsStrongPasswordChange](../BundleResources/Information-Property-List/NSExtension/ASAccountAuthenticationModificationSupportsStrongPasswordChange.md)
  A Boolean value that indicates whether the extension supports upgrading a user’s password to a strong password.
- [ASAccountAuthenticationModificationPasswordGenerationRequirements](../BundleResources/Information-Property-List/NSExtension/ASAccountAuthenticationModificationPasswordGenerationRequirements.md)
  The rules the system satisfies when generating a strong password for your extension during an automatic upgrade.
- [ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn](../BundleResources/Information-Property-List/ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn.md)
  A Boolean value that indicates the system shouldn’t show security recommendation prompts when users sign in using the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller/prepareinterfacetochangepassword(for:existingcredential:newpassword:userinfo:))*