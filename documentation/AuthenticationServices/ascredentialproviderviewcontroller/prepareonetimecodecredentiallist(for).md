# prepareOneTimeCodeCredentialList(for:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Prepares the interface to display a list of one-time passcodes (OTPs) that people can select from.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func prepareOneTimeCodeCredentialList(for serviceIdentifiers: [ASCredentialServiceIdentifier])
```

```objc
- (void) prepareOneTimeCodeCredentialListForServiceIdentifiers:(NSArray<ASCredentialServiceIdentifier *> *) serviceIdentifiers;
```

## Mentions

- [Providing one-time passcodes to AutoFill](../providing-one-time-passcodes-to-autofill.md)

## Overview

## Discussion

The system calls this method to tell your extension’s view controller to prepare a list of OTPs to present. After calling this method, the system presents the view controller to the person.

Use the given `serviceIdentifiers` array to filter or prioritize the credentials to display. The service identifier array might be empty, but your extension still shows credentials that the person can select from.

Items in the array with lower indices represent more specific identifiers for which an OTP’s requested. For example, if the array contains identifiers `[m.example.com, example.com]`, the item `m.example.com` represents the more specific service that requires an OTP.

When someone selects an OTP displayed by your view controller, represent the passcode as an [`ASOneTimeCodeCredential`](../asonetimecodecredential.md) and pass it to the system by calling [`completeOneTimeCodeRequest(using:completionHandler:)`](../ascredentialproviderextensioncontext/completeonetimecoderequest%28using,completionhandler%29.md):

```swift
let credential = ASOneTimeCodeCredential(code: otpCode)
await extensionContext.completeOneTimeCodeRequest(using: credential)
```

Always provide a way for someone to cancel the operation from your view controller, for example, by including a Cancel button in the navigation bar. When someone cancels the operation, call [`cancelRequest(withError:)`](../ascredentialproviderextensioncontext/cancelrequest%28witherror%29.md), using the error domain [`ASExtensionErrorDomain`](../asextensionerrordomain.md) and code [`userCanceled`](../asextensionerror/usercanceled.md):

```swift
let error = NSError(domain: ASExtensionErrorDomain,
                    code: ASExtensionError.userCanceled.rawValue)
extensionContext.cancelRequest(withError: error)
```

The system dismisses your view controller after you call either the completion or cancellation method.

## Parameters

- `serviceIdentifiers`: An array of service identifiers that provide a hint about the service that people need an OTP for.

## See Also

### Selecting a credential
- [func prepareCredentialList(for: [ASCredentialServiceIdentifier])](./preparecredentiallist%28for%29.md)
  Prepares the interface to display a list of credentials from which the user can select.
- [func prepareCredentialList(for: [ASCredentialServiceIdentifier], requestParameters: ASPasskeyCredentialRequestParameters)](./preparecredentiallist%28for,requestparameters%29.md)
  Prepares the interface to display a list of passkey and password credentials from which the user can select.
- [func prepareInterface(forPasskeyRegistration: any ASCredentialRequest)](./prepareinterface%28forpasskeyregistration%29.md)
  Prepare the view controller to show user interface for registering a new passkey.
- [func prepareInterfaceToProvideCredential(for: any ASCredentialRequest)](./prepareinterfacetoprovidecredential%28for%29-68qpo.md)
  Prepare the view controller to show user interface for providing the requested credential.
- [func provideCredentialWithoutUserInteraction(for: any ASCredentialRequest)](./providecredentialwithoutuserinteraction%28for%29-3mo23.md)
  Attempts to provide the user-requested credential with no further user interaction.
- [func performWithoutUserInteractionIfPossible(passkeyRegistration: ASPasskeyCredentialRequest)](./performwithoutuserinteractionifpossible%28passkeyregistration%29.md)
  Perform a conditional passkey registration, if possible.
- [class ASCredentialServiceIdentifier](../ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.
- [protocol ASCredentialRequest](../ascredentialrequest.md)
  A protocol that describes a request from the user for your extension to provide a credential.
- [class ASPasswordCredentialRequest](../aspasswordcredentialrequest.md)
  A class that represents a request to supply a password credential.
- [class ASOneTimeCodeCredentialRequest](../asonetimecodecredentialrequest.md)
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](../asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASPasskeyCredentialRequest](../aspasskeycredentialrequest.md)
  A class that represents a request to supply a passkey credential.
- [class ASPasskeyCredentialRequestParameters](../aspasskeycredentialrequestparameters.md)
  A class that represents information about a passkey credential request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/prepareonetimecodecredentiallist(for:))*