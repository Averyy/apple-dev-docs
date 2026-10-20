# ASAuthorizationPublicKeyCredentialRegistrationRequest

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface that defines properties for a credential registration request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol ASAuthorizationPublicKeyCredentialRegistrationRequest : NSCopying, NSSecureCoding, NSObjectProtocol
```

```objc
@protocol ASAuthorizationPublicKeyCredentialRegistrationRequest <NSObject, NSSecureCoding, NSCopying>
```

## Topics

### Getting the properties
- [var attestationPreference: ASAuthorizationPublicKeyCredentialAttestationKind](./asauthorizationpublickeycredentialregistrationrequest/attestationpreference.md)
  The type of attestation you’re requesting.
- [var challenge: Data](./asauthorizationpublickeycredentialregistrationrequest/challenge.md)
  Arbitrary data that the client signs as proof of a valid registration or attestation.
- [var displayName: String?](./asauthorizationpublickeycredentialregistrationrequest/displayname.md)
  A user-visible name for the credential, such as the account’s user name.
- [var name: String](./asauthorizationpublickeycredentialregistrationrequest/name.md)
  A user-visible name that identifies a credential.
- [var relyingPartyIdentifier: String](./asauthorizationpublickeycredentialregistrationrequest/relyingpartyidentifier.md)
  The domain name of the website for the credential.
- [var userID: Data](./asauthorizationpublickeycredentialregistrationrequest/userid.md)
  Data that the relying party associates with the credential.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./asauthorizationpublickeycredentialregistrationrequest/userverificationpreference.md)
  A preference for whether the authenticator attempts to verify the user at the time of sign-in.

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](./asauthorizationplatformpublickeycredentialregistrationrequest.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](./asauthorizationsecuritykeypublickeycredentialregistrationrequest.md)

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
- [class ASPasskeyCredentialRequest](./aspasskeycredentialrequest.md)
  A class that represents a request to supply a passkey credential.
- [class ASPasskeyCredentialRequestParameters](./aspasskeycredentialrequestparameters.md)
  A class that represents information about a passkey credential request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialregistrationrequest)*