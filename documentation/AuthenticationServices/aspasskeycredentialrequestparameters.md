# ASPasskeyCredentialRequestParameters

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A class that represents information about a passkey credential request.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASPasskeyCredentialRequestParameters
```

```objc
@interface ASPasskeyCredentialRequestParameters : NSObject
```

#### Overview

The system creates instances of this class to handle active passkey requests, and passes them to your extension by calling [`prepareCredentialList(for:requestParameters:)`](./ascredentialproviderviewcontroller/preparecredentiallist%28for,requestparameters%29.md). Use the properties of the given request parameters object, along with the passkey credential that the person chooses, to construct a passkey credential response that you return to the system using [`completeAssertionRequest(using:completionHandler:)`](./ascredentialproviderextensioncontext/completeassertionrequest%28using,completionhandler%29.md).

## Topics

### Viewing credential request parameters
- [var allowedCredentials: [Data]](./aspasskeycredentialrequestparameters/allowedcredentials.md)
  A list of passkey credentials that the relying party accepts for this challenge.
- [var clientDataHash: Data](./aspasskeycredentialrequestparameters/clientdatahash.md)
  The client data that you sign as part of the response.
- [var relyingPartyIdentifier: String](./aspasskeycredentialrequestparameters/relyingpartyidentifier.md)
  The relying party that issues the challenge.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./aspasskeycredentialrequestparameters/userverificationpreference.md)
  The relying party’s preference for user verification.
### Working with WebAuthn extensions
- [var extensionInput: ASPasskeyAssertionCredentialExtensionInput?](./aspasskeycredentialrequestparameters/extensioninput-2edlv.md)
  An input for WebAuthn extensions.
- [struct ASPasskeyAssertionCredentialExtensionInput](./aspasskeyassertioncredentialextensioninput-swift.struct.md)
  A type that encapsulates input for various WebAuthn extensions during passkey assertion.
### Initializers
- [init?(coder: NSCoder)](./aspasskeycredentialrequestparameters/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Selecting a credential
- [func prepareCredentialList(for: [ASCredentialServiceIdentifier])](./ascredentialproviderviewcontroller/preparecredentiallist%28for%29.md)
  Prepares the interface to display a list of credentials from which the user can select.
- [func prepareCredentialList(for: [ASCredentialServiceIdentifier], requestParameters: ASPasskeyCredentialRequestParameters)](./ascredentialproviderviewcontroller/preparecredentiallist%28for,requestparameters%29.md)
  Prepares the interface to display a list of passkey and password credentials from which the user can select.
- [func prepareOneTimeCodeCredentialList(for: [ASCredentialServiceIdentifier])](./ascredentialproviderviewcontroller/prepareonetimecodecredentiallist%28for%29.md)
  Prepares the interface to display a list of one-time passcodes (OTPs) that people can select from.
- [func prepareInterface(forPasskeyRegistration: any ASCredentialRequest)](./ascredentialproviderviewcontroller/prepareinterface%28forpasskeyregistration%29.md)
  Prepare the view controller to show user interface for registering a new passkey.
- [func prepareInterfaceToProvideCredential(for: any ASCredentialRequest)](./ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential%28for%29-68qpo.md)
  Prepare the view controller to show user interface for providing the requested credential.
- [func provideCredentialWithoutUserInteraction(for: any ASCredentialRequest)](./ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction%28for%29-3mo23.md)
  Attempts to provide the user-requested credential with no further user interaction.
- [func performWithoutUserInteractionIfPossible(passkeyRegistration: ASPasskeyCredentialRequest)](./ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible%28passkeyregistration%29.md)
  Perform a conditional passkey registration, if possible.
- [class ASCredentialServiceIdentifier](./ascredentialserviceidentifier.md)
  An identifier representing a particular service for which the user needs a credential, like a web site.
- [protocol ASCredentialRequest](./ascredentialrequest.md)
  A protocol that describes a request from the user for your extension to provide a credential.
- [class ASPasswordCredentialRequest](./aspasswordcredentialrequest.md)
  A class that represents a request to supply a password credential.
- [class ASOneTimeCodeCredentialRequest](./asonetimecodecredentialrequest.md)
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](./asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASPasskeyCredentialRequest](./aspasskeycredentialrequest.md)
  A class that represents a request to supply a passkey credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequestparameters)*