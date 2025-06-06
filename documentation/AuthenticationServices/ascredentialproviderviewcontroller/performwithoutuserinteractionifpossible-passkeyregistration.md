# performWithoutUserInteractionIfPossible(passkeyRegistration:)

**Framework**: Authentication Services  
**Kind**: method

Perform a conditional passkey registration, if possible.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func performWithoutUserInteractionIfPossible(passkeyRegistration registrationRequest: ASPasskeyCredentialRequest)
```

#### Discussion

This method will be called for handling conditional passkey registration requests. A conditional passkey registration request allows your extension to opportunistically register passkeys in the background, if and only if you believe the user is in a good state to do so. Your extension decides can decide what conditions make sense for whether to fulfill or reject this request. For example, an extension may decide to register a passkey only if all of the following conditions are met:

- The user’s vault is currently unlocked.
- The user name for the registration request matches that for an existing saved password.
- The matching saved password was filled recently.
- The user does not already have a passkey for this account.

Fulfilling this request should not remove a user’s saved password for this account, but it may mean that the passkey will be preferred over the password in future AutoFill invocations, if both are supported.

Your extension should complete this request by calling `-[ASCredentialProviderExtensionContext completeRegistrationRequestWithSelectedPasskeyCredential:completionHandler:]` or`-[ASCredentialProviderExtensionContext cancelRequestWithError:]`, like for standard registration requests. However, this request is not allowed to show UI and `ASExtensionErrorCodeUserInteractionRequired` will be treated like any other error. The intent of this API is to provide a method of performing a background registration only where easy and convenient, so no blocking UI or error should ever be shown.

To indicate support for this feature, add `SupportsConditionalPasskeyRegistration` under the `ASCredentialProviderExtensionCapabilities` dictionary.

```None
Info.plist
├─ NSExtension
    ├─ NSExtensionAttributes
        ├─ ASCredentialProviderExtensionCapabilities
            ├─ SupportsConditionalPasskeyRegistration => true
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible(passkeyregistration:))*