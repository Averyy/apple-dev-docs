# ASCredentialServiceIdentifier

**Framework**: Authentication Services  
**Kind**: class

An identifier representing a particular service for which the user needs a credential, like a web site.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class ASCredentialServiceIdentifier
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Topics

### Creating a credential service identifier
- [init(identifier: String, type: ASCredentialServiceIdentifier.IdentifierType)](ascredentialserviceidentifier/init(identifier:type:).md)
  Initializes a credential service identifier instance.
### Identifying the credential service
- [var identifier: String](ascredentialserviceidentifier/identifier.md)
  A string that names the identified service.
- [var type: ASCredentialServiceIdentifier.IdentifierType](ascredentialserviceidentifier/type.md)
  The kind of services that the identifier represents.
- [ASCredentialServiceIdentifier.IdentifierType](ascredentialserviceidentifier/identifiertype.md)
  Possible values for the service identifier type.
### Initializers
- [init(identifier: String, type: ASCredentialServiceIdentifier.IdentifierType, displayName: String)](ascredentialserviceidentifier/init(identifier:type:displayname:).md)
  Initializes an ASCredentialServiceIdentifier object.
### Instance Properties
- [var displayName: String?](ascredentialserviceidentifier/displayname.md)
  A user visible name for the identifier. For `app` types it will contain the localized name of the app. For `URL` types it will contain the host name of the URL if it contains a valid host. For `URL` type identifiers that do not contain a valid host and for `domain` type identifiers, this will be equal to `identifier`. This property is meant only as a best effort suggestion for display purposes. It is not used by the system to identify the service or suggest a credential for AutoFill.

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

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialserviceidentifier)*