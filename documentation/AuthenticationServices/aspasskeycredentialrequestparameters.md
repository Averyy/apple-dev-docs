# ASPasskeyCredentialRequestParameters

**Framework**: Authentication Services  
**Kind**: class

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

#### Overview

The system creates instances of this class to handle active passkey requests, and passes them to your extension by calling [`prepareCredentialList(for:requestParameters:)`](ascredentialproviderviewcontroller/preparecredentiallist(for:requestparameters:).md). Use the properties of the given request parameters object, along with the passkey credential that the person chooses, to construct a passkey credential response that you return to the system using [`completeAssertionRequest(using:completionHandler:)`](ascredentialproviderextensioncontext/completeassertionrequest(using:completionhandler:).md).

## Topics

### Viewing credential request parameters
- [var allowedCredentials: [Data]](aspasskeycredentialrequestparameters/allowedcredentials.md)
  A list of passkey credentials that the relying party accepts for this challenge.
- [var clientDataHash: Data](aspasskeycredentialrequestparameters/clientdatahash.md)
  The client data that you sign as part of the response.
- [var relyingPartyIdentifier: String](aspasskeycredentialrequestparameters/relyingpartyidentifier.md)
  The relying party that issues the challenge.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](aspasskeycredentialrequestparameters/userverificationpreference.md)
  The relying party’s preference for user verification.
### Instance Properties
- [var extensionInput: ASPasskeyAssertionCredentialExtensionInput?](aspasskeycredentialrequestparameters/extensioninput-2edlv.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequestparameters)*