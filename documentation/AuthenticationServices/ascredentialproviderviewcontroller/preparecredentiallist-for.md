# prepareCredentialList(for:)

**Framework**: Authentication Services  
**Kind**: method

Prepares the interface to display a list of credentials from which the user can select.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareCredentialList(for serviceIdentifiers: [ASCredentialServiceIdentifier])
```

#### Discussion

The system calls this method to tell your extension’s view controller to prepare to present a list of credentials. After calling this method, the system presents the view controller to the user.

Use the given `serviceIdentifiers` array to filter or prioritize the credentials to display. The service identifier array might be empty, but your extension should still show credentials from which the user can pick.

Items in the array with lower indices represent more specific identifiers for which a credential’s requested. For example, if the array contains identifiers `[m.example.com, example.com]`, the item `m.example.com` represents the more specific service that requires a credential.

When the user selects a credential displayed by your view controller, encapsulate the corresponding user and password strings in an [`ASPasswordCredential`](aspasswordcredential.md) instance and pass it to the extension context’s [`completeRequest(withSelectedCredential:completionHandler:)`](ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:).md) method:

```swift
let passwordCredential = ASPasswordCredential(user: user, password: password)
extensionContext.completeRequest(withSelectedCredential: passwordCredential)
```

Alternatively, if the user cancels the operation, call the [`cancelRequest(withError:)`](ascredentialproviderextensioncontext/cancelrequest(witherror:).md) method instead with an error that indicates user cancelation:

```swift
let error = NSError(domain: ASExtensionErrorDomain,
                    code: ASExtensionError.userCanceled.rawValue)
extensionContext.cancelRequest(withError: error)
```

Always provide a way for the user to cancel the operation from your view controller, for example by including a cancel button in the navigation bar.

The system dismisses your view controller automatically after you call either the completion or cancelation method.

## Parameters

- `serviceIdentifiers`: An array of service identifiers that provide a hint about the service for which the user needs credentials.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/preparecredentiallist(for:))*