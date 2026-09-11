# ASAccountAuthenticationModificationViewController

**Framework**: Authentication Services  
**Kind**: class

A view controller that can upgrade user passwords to strong passwords, or convert accounts to use Sign in with Apple.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASAccountAuthenticationModificationViewController
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Overview

Adding an account modification extension lets your app seamlessly upgrade user passwords to strong passwords, or convert from using passwords to using Sign in with Apple. The entire process can be automatic, requiring no user interaction, or you can include interactions, such as two-factor authentication confirmation.

> **Note**:  This class ignores calls from Mac apps built with Mac Catalyst.

## Topics

### Upgrading to Sign in with Apple
- [func convertAccountToSignInWithAppleWithoutUserInteraction(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationviewcontroller/convertaccounttosigninwithapplewithoutuserinteraction(for:existingcredential:userinfo:).md)
  Converts an account’s authentication mechanism from using passwords to using Sign in with Apple.
- [func prepareInterfaceToConvertAccountToSignInWithApple(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationviewcontroller/prepareinterfacetoconvertaccounttosigninwithapple(for:existingcredential:userinfo:).md)
  Prepares the view controller’s interface that displays when converting an account that uses password authentication to use Sign in with Apple.
- [ASAccountAuthenticationModificationSupportsUpgradeToSignInWithApple](../bundleresources/information-property-list/nsextension/asaccountauthenticationmodificationsupportsupgradetosigninwithapple.md)
  A Boolean value that indicates whether the extension supports upgrading from using password authentication to using Sign in with Apple.
### Upgrading to Strong Passwords
- [func changePasswordWithoutUserInteraction(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, newPassword: String, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationviewcontroller/changepasswordwithoutuserinteraction(for:existingcredential:newpassword:userinfo:).md)
  Upgrades a user’s weak password to a strong password.
- [func prepareInterfaceToChangePassword(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, newPassword: String, userInfo: [AnyHashable : Any]?)](asaccountauthenticationmodificationviewcontroller/prepareinterfacetochangepassword(for:existingcredential:newpassword:userinfo:).md)
  Prepares the view controller’s interface that displays when upgrading from a weak password to a strong password.
- [ASAccountAuthenticationModificationSupportsStrongPasswordChange](../bundleresources/information-property-list/nsextension/asaccountauthenticationmodificationsupportsstrongpasswordchange.md)
  A Boolean value that indicates whether the extension supports upgrading a user’s password to a strong password.
- [ASAccountAuthenticationModificationPasswordGenerationRequirements](../bundleresources/information-property-list/nsextension/asaccountauthenticationmodificationpasswordgenerationrequirements.md)
  The rules the system satisfies when generating a strong password for your extension during an automatic upgrade.
- [ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn](../bundleresources/information-property-list/asaccountauthenticationmodificationoptoutofsecuritypromptsonsignin.md)
  A Boolean value that indicates the system shouldn’t show security recommendation prompts when users sign in using the app.
### Handling Modification Requests
- [func cancelRequest()](asaccountauthenticationmodificationviewcontroller/cancelrequest.md)
  Cancels a request that the user initiated.
- [protocol ASAccountAuthenticationModificationControllerDelegate](asaccountauthenticationmodificationcontrollerdelegate.md)
  An interface you implement for receiving success and failure statuses about modification of an account’s authentication properties.
- [protocol ASAccountAuthenticationModificationControllerPresentationContextProviding](asaccountauthenticationmodificationcontrollerpresentationcontextproviding.md)
  An interface you implement to coordinate presentation of the user interface when modifying an account’s authentication properties.
### Getting the Extension Context
- [var extensionContext: ASAccountAuthenticationModificationExtensionContext](asaccountauthenticationmodificationviewcontroller/extensioncontext.md)
  The context your account authentication modification extension uses to provide information to the system.

## Relationships

### Inherits From
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)
  Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.
- [class ASAccountAuthenticationModificationController](asaccountauthenticationmodificationcontroller.md)
  An object that performs a request to modify an account’s authentication properties.
- [class ASAccountAuthenticationModificationExtensionContext](asaccountauthenticationmodificationextensioncontext.md)
  An object that you interact with to change an account’s password or to upgrade to Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller)*