# ASCredentialServiceIdentifier

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASCredentialServiceIdentifier : NSObject
```

## Mentions

- [Upgrading Account Security With an Account Authentication Modification Extension](./upgrading-account-security-with-an-account-authentication-modification-extension.md)

## Topics

### Creating a credential service identifier
- [init(identifier: String, type: ASCredentialServiceIdentifier.IdentifierType)](./ascredentialserviceidentifier/init%28identifier,type%29.md)
  Initializes a credential service identifier instance.
### Identifying the credential service
- [var identifier: String](./ascredentialserviceidentifier/identifier.md)
  A string that names the identified service.
- [var type: ASCredentialServiceIdentifier.IdentifierType](./ascredentialserviceidentifier/type.md)
  The kind of services that the identifier represents.
- [ASCredentialServiceIdentifier.IdentifierType](./ascredentialserviceidentifier/identifiertype.md)
  Possible values for the service identifier type.
### Initializers
- [init?(coder: NSCoder)](./ascredentialserviceidentifier/init%28coder%29.md)
- [init(identifier: String, type: ASCredentialServiceIdentifier.IdentifierType, displayName: String)](./ascredentialserviceidentifier/init%28identifier,type,displayname%29.md)
  Initializes an ASCredentialServiceIdentifier object.
### Instance Properties
- [var displayName: String?](./ascredentialserviceidentifier/displayname.md)
  A user visible name for the identifier. For `app` types it will contain the localized name of the app. For `URL` types it will contain the host name of the URL if it contains a valid host. For `URL` type identifiers that do not contain a valid host and for `domain` type identifiers, this will be equal to `identifier`. This property is meant only as a best effort suggestion for display purposes. It is not used by the system to identify the service or suggest a credential for AutoFill.

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
- [protocol ASCredentialRequest](./ascredentialrequest.md)
  A protocol that describes a request from the user for your extension to provide a credential.
- [class ASPasswordCredentialRequest](./aspasswordcredentialrequest.md)
  A class that represents a request to supply a password credential.
- [class ASOneTimeCodeCredentialRequest](./asonetimecodecredentialrequest.md)
- [protocol ASAuthorizationPublicKeyCredentialRegistrationRequest](./asauthorizationpublickeycredentialregistrationrequest.md)
  An interface that defines properties for a credential registration request.
- [class ASPasskeyCredentialRequest](./aspasskeycredentialrequest.md)
  A class that represents a request to supply a passkey credential.
- [class ASPasskeyCredentialRequestParameters](./aspasskeycredentialrequestparameters.md)
  A class that represents information about a passkey credential request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialserviceidentifier)*