# ASAccountAuthenticationModificationViewController

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface ASAccountAuthenticationModificationViewController : UIViewController
```

*macOS*

```objc
@interface ASAccountAuthenticationModificationViewController : NSViewController
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](./upgrading-account-security-with-an-account-authentication-modification-extension.md)

#### Overview

Adding an account modification extension lets your app seamlessly upgrade user passwords to strong passwords, or convert from using passwords to using Sign in with Apple. The entire process can be automatic, requiring no user interaction, or you can include interactions, such as two-factor authentication confirmation.

> **Note**:  This class ignores calls from Mac apps built with Mac Catalyst.

## Topics

### Upgrading to Sign in with Apple
- [func convertAccountToSignInWithAppleWithoutUserInteraction(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationviewcontroller/convertaccounttosigninwithapplewithoutuserinteraction%28for,existingcredential,userinfo%29.md)
  Converts an account’s authentication mechanism from using passwords to using Sign in with Apple.
- [func prepareInterfaceToConvertAccountToSignInWithApple(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationviewcontroller/prepareinterfacetoconvertaccounttosigninwithapple%28for,existingcredential,userinfo%29.md)
  Prepares the view controller’s interface that displays when converting an account that uses password authentication to use Sign in with Apple.
- [ASAccountAuthenticationModificationSupportsUpgradeToSignInWithApple](../BundleResources/information-property-list/nsextension/asaccountauthenticationmodificationsupportsupgradetosigninwithapple.md)
  A Boolean value that indicates whether the extension supports upgrading from using password authentication to using Sign in with Apple.
### Upgrading to Strong Passwords
- [func changePasswordWithoutUserInteraction(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, newPassword: String, userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationviewcontroller/changepasswordwithoutuserinteraction%28for,existingcredential,newpassword,userinfo%29.md)
  Upgrades a user’s weak password to a strong password.
- [func prepareInterfaceToChangePassword(for: ASCredentialServiceIdentifier, existingCredential: ASPasswordCredential, newPassword: String, userInfo: [AnyHashable : Any]?)](./asaccountauthenticationmodificationviewcontroller/prepareinterfacetochangepassword%28for,existingcredential,newpassword,userinfo%29.md)
  Prepares the view controller’s interface that displays when upgrading from a weak password to a strong password.
- [ASAccountAuthenticationModificationSupportsStrongPasswordChange](../BundleResources/information-property-list/nsextension/asaccountauthenticationmodificationsupportsstrongpasswordchange.md)
  A Boolean value that indicates whether the extension supports upgrading a user’s password to a strong password.
- [ASAccountAuthenticationModificationPasswordGenerationRequirements](../BundleResources/information-property-list/nsextension/asaccountauthenticationmodificationpasswordgenerationrequirements.md)
  The rules the system satisfies when generating a strong password for your extension during an automatic upgrade.
- [ASAccountAuthenticationModificationOptOutOfSecurityPromptsOnSignIn](../BundleResources/information-property-list/asaccountauthenticationmodificationoptoutofsecuritypromptsonsignin.md)
  A Boolean value that indicates the system shouldn’t show security recommendation prompts when users sign in using the app.
### Handling Modification Requests
- [func cancelRequest()](./asaccountauthenticationmodificationviewcontroller/cancelrequest%28%29.md)
  Cancels a request that the user initiated.
- [protocol ASAccountAuthenticationModificationControllerDelegate](./asaccountauthenticationmodificationcontrollerdelegate.md)
  An interface you implement for receiving success and failure statuses about modification of an account’s authentication properties.
- [protocol ASAccountAuthenticationModificationControllerPresentationContextProviding](./asaccountauthenticationmodificationcontrollerpresentationcontextproviding.md)
  An interface you implement to coordinate presentation of the user interface when modifying an account’s authentication properties.
### Getting the Extension Context
- [var extensionContext: ASAccountAuthenticationModificationExtensionContext](./asaccountauthenticationmodificationviewcontroller/extensioncontext.md)
  The context your account authentication modification extension uses to provide information to the system.

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
- [NSViewController](../AppKit/nsviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Automatic security upgrades
- [Upgrading Account Security With an Account Authentication Modification Extension](./upgrading-account-security-with-an-account-authentication-modification-extension.md)
  Automatically and transparently convert accounts to Sign in with Apple or to use strong passwords for improved security.
- [class ASAccountAuthenticationModificationController](./asaccountauthenticationmodificationcontroller.md)
  An object that performs a request to modify an account’s authentication properties.
- [class ASAccountAuthenticationModificationExtensionContext](./asaccountauthenticationmodificationextensioncontext.md)
  An object that you interact with to change an account’s password or to upgrade to Sign in with Apple.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asaccountauthenticationmodificationviewcontroller)*