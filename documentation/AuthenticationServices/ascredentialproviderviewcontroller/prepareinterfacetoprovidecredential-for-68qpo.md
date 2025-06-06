# prepareInterfaceToProvideCredential(for:)

**Framework**: Authentication Services  
**Kind**: method

Prepare the view controller to show user interface for providing the requested credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func prepareInterfaceToProvideCredential(for credentialRequest: any ASCredentialRequest)
```

## Mentions

- [Providing one-time passcodes to AutoFill](providing-one-time-passcodes-to-autofill.md)

#### Discussion

The system calls this method when your extension can’t supply the requested credential without user interaction. Limit user interaction to operations required for providing the requested credential, like showing an authentication UI to unlock the person’s passwords database.

Call the appropriate completion method on the extension context to provide the credential. For password credentials, call [`completeRequest(withSelectedCredential:completionHandler:)`](ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:).md). For passkey credentials, call [`completeAssertionRequest(using:completionHandler:)`](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md). For one-time passcodes, call [`completeOneTimeCodeRequest(using:completionHandler:)`](ascredentialproviderextensioncontext/completeonetimecoderequest(using:completionhandler:).md).

Alternatively, if an error occurs, call [`cancelRequest(withError:)`](ascredentialproviderextensioncontext/cancelrequest(witherror:).md) instead and pass an error with domain [`ASExtensionErrorDomain`](asextensionerrordomain.md) and an appropriate error code from [`ASExtensionError.Code`](asextensionerror/code.md). For example, if your app can’t find the credential identity in the database, pass an error with code [`ASExtensionError.Code.credentialIdentityNotFound`](asextensionerror/code/credentialidentitynotfound.md).

## Parameters

- `credentialRequest`: The credential request.

## See Also

- [func prepareCredentialList(for: [ASCredentialServiceIdentifier])](ascredentialproviderviewcontroller/preparecredentiallist(for:).md)
  Prepares the interface to display a list of credentials from which the user can select.
- [func prepareCredentialList(for: [ASCredentialServiceIdentifier], requestParameters: ASPasskeyCredentialRequestParameters)](ascredentialproviderviewcontroller/preparecredentiallist(for:requestparameters:).md)
  Prepares the interface to display a list of passkey and password credentials from which the user can select.
- [func prepareOneTimeCodeCredentialList(for: [ASCredentialServiceIdentifier])](ascredentialproviderviewcontroller/prepareonetimecodecredentiallist(for:).md)
  Prepares the interface to display a list of one-time passcodes (OTPs) that people can select from.
- [func prepareInterface(forPasskeyRegistration: any ASCredentialRequest)](ascredentialproviderviewcontroller/prepareinterface(forpasskeyregistration:).md)
  Prepare the view controller to show user interface for registering a new passkey.
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

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for:)-68qpo)*