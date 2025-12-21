# ASCredentialProviderViewController

**Framework**: Authentication Services  
**Kind**: class

A view controller that a credential manager app uses to extend AutoFill.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class ASCredentialProviderViewController
```

#### Overview

To integrate a password, passkey, or one-time passcode manager app with AutoFill:

1. Add a Credential Provider Extension target to your project that subclasses [`ASCredentialProviderViewController`](ascredentialproviderviewcontroller.md). Add the [`AutoFill Credential Provider Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.authentication-services.autofill-credential-provider) to both the extension and its containing app.
2. Override the view controller’s [`prepareCredentialList(for:)`](ascredentialproviderviewcontroller/preparecredentiallist(for:).md) method to prepare a view with a list of credentials that the person can choose from after opening your extension from the AutoFill suggestions list.
3. Optionally add [`ASPasswordCredentialIdentity`](aspasswordcredentialidentity.md) and [`ASPasskeyCredentialIdentity`](aspasskeycredentialidentity.md) instances to the shared [`ASCredentialIdentityStore`](ascredentialidentitystore.md) to make identities available directly in the AutoFill suggestions list. Then override the [`provideCredentialWithoutUserInteraction(for:)`](ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for:)-3mo23.md) method to provide the associated credentials when the person taps a suggestion.
4. Optionally, override the [`prepareInterfaceForExtensionConfiguration()`](ascredentialproviderviewcontroller/prepareinterfaceforextensionconfiguration().md) method to specify a configuration interface that you can show when people first enable your credentials manager in Settings.

##### Receiving Credential Updates

Apps and websites that allow sign-ins can signal updates to the operating system with the [`ASCredentialUpdater`](ascredentialupdater.md) class. The various “report” methods of [`ASCredentialUpdater`](ascredentialupdater.md) work like the “signal” methods of `PublicKeyCredential` when using WebAuthn on the web. For example, a website or app can notify credential manager apps that it updated a user name or email for a given account, allowing the manager to stay consistent with the website.

Your credential manager manager receives these updates in the “report” methods of `ASCredentialProviderViewController`. Use these calls to update your manager’s stored credential data or behavior. For example, a call to [`reportUnusedPasswordCredential(forDomain:userName:)`](ascredentialproviderviewcontroller/reportunusedpasswordcredential(fordomain:username:).md) can indicate that someone using a passkey will no longer use a password to sign in to a given domain, or that they deleted their account. In this case, the manager should stop showing the user name and password for that domain.

> **Note**:  This class ignores calls from Mac apps built with Mac Catalyst.

## Topics

### Getting the extension context
- [var extensionContext: ASCredentialProviderExtensionContext](ascredentialproviderviewcontroller/extensioncontext.md)
  The context your credential provider extension uses to provide information to the system.
- [class ASCredentialProviderExtensionContext](ascredentialproviderextensioncontext.md)
  A mechanism that credential provider extensions use to communicate with the system.
### Configuring the credential provider extension
- [func prepareInterfaceForExtensionConfiguration()](ascredentialproviderviewcontroller/prepareinterfaceforextensionconfiguration.md)
  Prepares the interface to enable the user to configure the extension.
- [class ASCredentialIdentityStore](ascredentialidentitystore.md)
  A container that your extension fills to provide credentials through the QuickType bar.
### Selecting a credential
- [func prepareCredentialList(for: [ASCredentialServiceIdentifier])](ascredentialproviderviewcontroller/preparecredentiallist(for:).md)
  Prepares the interface to display a list of credentials from which the user can select.
- [func prepareCredentialList(for: [ASCredentialServiceIdentifier], requestParameters: ASPasskeyCredentialRequestParameters)](ascredentialproviderviewcontroller/preparecredentiallist(for:requestparameters:).md)
  Prepares the interface to display a list of passkey and password credentials from which the user can select.
- [func prepareOneTimeCodeCredentialList(for: [ASCredentialServiceIdentifier])](ascredentialproviderviewcontroller/prepareonetimecodecredentiallist(for:).md)
  Prepares the interface to display a list of one-time passcodes (OTPs) that people can select from.
- [func prepareInterface(forPasskeyRegistration: any ASCredentialRequest)](ascredentialproviderviewcontroller/prepareinterface(forpasskeyregistration:).md)
  Prepare the view controller to show user interface for registering a new passkey.
- [func prepareInterfaceToProvideCredential(for: any ASCredentialRequest)](ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for:)-68qpo.md)
  Prepare the view controller to show user interface for providing the requested credential.
- [func provideCredentialWithoutUserInteraction(for: any ASCredentialRequest)](ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for:)-3mo23.md)
  Attempts to provide the user-requested credential with no further user interaction.
- [func performWithoutUserInteractionIfPossible(passkeyRegistration: ASPasskeyCredentialRequest)](ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible(passkeyregistration:).md)
  Perform a conditional passkey registration, if possible.
- [class ASCredentialServiceIdentifier](ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.
- [protocol ASCredentialRequest](ascredentialrequest.md)
  A protocol that describes a request from the user for your extension to provide a credential.
- [class ASPasswordCredentialRequest](aspasswordcredentialrequest.md)
  A class that represents a request to supply a password credential.
- [class ASOneTimeCodeCredentialRequest](asonetimecodecredentialrequest.md)
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASPasskeyCredentialRequest](aspasskeycredentialrequest.md)
  A class that represents a request to supply a passkey credential.
- [class ASPasskeyCredentialRequestParameters](aspasskeycredentialrequestparameters.md)
  A class that represents information about a passkey credential request.
### Providing text to AutoFill
- [func prepareInterfaceForUserChoosingTextToInsert()](ascredentialproviderviewcontroller/prepareinterfaceforuserchoosingtexttoinsert.md)
  Prepare the view controller to show a list of all insertable text with user selectable fields.
### Recognizing errors
- [struct ASExtensionError](asextensionerror.md)
  A credential provider extension error.
- [let ASExtensionErrorDomain: String](asextensionerrordomain.md)
  The domain for a credential provider extension error.
- [ASExtensionError.Code](asextensionerror/code.md)
  The codes for a credential provider extension error.
### Accessing settings
- [class ASSettingsHelper](assettingshelper.md)
  A class that opens Settings and navigates to the settings for configuring credential providers.
### Receiving credential updates
- [func reportAllAcceptedPublicKeyCredentials(forRelyingParty: String, userHandle: Data, acceptedCredentialIDs: [Data])](ascredentialproviderviewcontroller/reportallacceptedpublickeycredentials(forrelyingparty:userhandle:acceptedcredentialids:).md)
  Receives a report from the system that a relying party sent a snapshot of all accepted credentials for an account.
- [func reportPublicKeyCredentialUpdate(forRelyingParty: String, userHandle: Data, newName: String)](ascredentialproviderviewcontroller/reportpublickeycredentialupdate(forrelyingparty:userhandle:newname:).md)
  Receives a report from the system that a relying party indicated that a passkey’s user name updated.
- [func reportUnknownPublicKeyCredential(forRelyingParty: String, credentialID: Data)](ascredentialproviderviewcontroller/reportunknownpublickeycredential(forrelyingparty:credentialid:).md)
  Receives a report from the system that a relying party indicated a passkey credential is invalid.
- [func reportUnusedPasswordCredential(forDomain: String, userName: String)](ascredentialproviderviewcontroller/reportunusedpasswordcredential(fordomain:username:).md)
  Receives a report from the system that a relying party indicatd that a password credential isn’t needed anymore for a given user name.
### Deprecated methods
- [func provideCredentialWithoutUserInteraction(for: ASPasswordCredentialIdentity)](ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for:)-7jlg0.md)
  Attempts to provide the user-requested credential with no further user interaction.
- [func prepareInterfaceToProvideCredential(for: ASPasswordCredentialIdentity)](ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for:)-18ukb.md)
  Prepares the interface for a user interaction, like a database login, that enables it to access and return the credential for the given identity.
### Instance Methods
- [func performWithoutUserInteraction(generatePasswordsRequest: ASGeneratePasswordsRequest)](ascredentialproviderviewcontroller/performwithoutuserinteraction(generatepasswordsrequest:).md)
  Attempt to generate passwords based on developer-specified rules.
- [func performWithoutUserInteractionIfPossible(savePasswordRequest: ASSavePasswordRequest)](ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible(savepasswordrequest:).md)
  Attempt to save a password credential.
- [func prepareInterface(for: ASSavePasswordRequest)](ascredentialproviderviewcontroller/prepareinterface(for:)-69elg.md)
  Prepares the interface to display a prompt to save a password credential.
- [func prepareInterface(for: ASGeneratePasswordsRequest)](ascredentialproviderviewcontroller/prepareinterface(for:)-7ideq.md)
  Prepares the interface to display a prompt to generate passwords based on developer-specified rules.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Providing one-time passcodes to AutoFill](providing-one-time-passcodes-to-autofill.md)
  Help people efficiently perform multifactor authentication.
- [AutoFill Credential Provider Entitlement](../BundleResources/Entitlements/com.apple.developer.authentication-services.autofill-credential-provider.md)
  A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller)*