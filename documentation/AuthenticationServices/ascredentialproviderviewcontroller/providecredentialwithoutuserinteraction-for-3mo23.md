# provideCredentialWithoutUserInteraction(for:)

**Framework**: Authentication Services  
**Kind**: method

Attempts to provide the user-requested credential with no further user interaction.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func provideCredentialWithoutUserInteraction(for credentialRequest: any ASCredentialRequest)
```

## Mentions

- [Providing one-time passcodes to AutoFill](providing-one-time-passcodes-to-autofill.md)

#### Discussion

After the person selects a credential identity, the system creates a credential request. The contents of the request depend on the type of credential requested. If the person requests a password or one-time passcode (OTP), the credential request (a [`ASPasswordCredentialRequest`](aspasswordcredentialrequest.md) or [`ASOneTimeCodeCredentialRequest`](asonetimecodecredentialrequest.md)) contains a credential identity. If the person requests a passkey, the [`ASPasskeyCredentialRequest`](aspasskeycredentialrequest.md) also contains information about the passkey assertion challenge.

The system calls [`provideCredentialWithoutUserInteraction(for:)`](ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for:)-3mo23.md) to enhance the user experience. If your credential provider extension can provide the credential without user interaction, call the relevant completion method on the extension context. For password credential requests, call [`completeRequest(withSelectedCredential:completionHandler:)`](ascredentialproviderextensioncontext/completerequest(withselectedcredential:completionhandler:).md). For passkey credential requests, call [`completeAssertionRequest(using:completionHandler:)`](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md). For OTP requests, call [`completeOneTimeCodeRequest(using:completionHandler:)`](ascredentialproviderextensioncontext/completeonetimecoderequest(using:completionhandler:).md).

If your extension requires user interaction to provide the credential, like when someone needs to unlock their credentials database, call [`cancelRequest(withError:)`](ascredentialproviderextensioncontext/cancelrequest(witherror:).md). Use the error domain [`ASExtensionErrorDomain`](asextensionerrordomain.md), and the code [`ASExtensionError.Code.userInteractionRequired`](asextensionerror/code/userinteractionrequired.md).

If an error occurs, call [`cancelRequest(withError:)`](ascredentialproviderextensioncontext/cancelrequest(witherror:).md) using the error domain [`ASExtensionErrorDomain`](asextensionerrordomain.md) and an appropriate code from [`ASExtensionError.Code`](asextensionerror/code.md).

As your view controller isn’t presented while the system calls this method, don’t show or use any user interface from this method.

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
- [func prepareInterfaceToProvideCredential(for: any ASCredentialRequest)](ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for:)-68qpo.md)
  Prepare the view controller to show user interface for providing the requested credential.
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

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for:)-3mo23)*