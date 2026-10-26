# ASPasskeyCredentialRequest

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A class that represents a request to supply a passkey credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class ASPasskeyCredentialRequest
```

```objc
@interface ASPasskeyCredentialRequest : NSObject
```

## Topics

### Creating passkey credential requests
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [NSNumber])](./aspasskeycredentialrequest/init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms%29-1jihy.md)
  Initializes a passkey credential request, identifying supported algorithms by number.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier])](./aspasskeycredentialrequest/init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms%29-52txr.md)
  Initializes a passkey credential request, identifying supported algorithms with constants.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyAssertionCredentialExtensionInput?)](./aspasskeycredentialrequest/init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms,extensioninput%29-9hsyv.md)
  Initializes a passkey credential request, providing additional passkey assertion data.
- [convenience init(credentialIdentity: ASPasskeyCredentialIdentity, clientDataHash: Data, userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference, supportedAlgorithms: [ASCOSEAlgorithmIdentifier], extensionInput: ASPasskeyRegistrationCredentialExtensionInput?)](./aspasskeycredentialrequest/init%28credentialidentity,clientdatahash,userverificationpreference,supportedalgorithms,extensioninput%29-1258o.md)
  Initializes a passkey credential request, providing additional passkey registration data.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:](./aspasskeycredentialrequest/initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_.md)
  Initializes a passkey credential request.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:assertionExtensionInput:](./aspasskeycredentialrequest/initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_assertionextensioninput_.md)
  Initializes a passkey credential request, providing additional passkey registration data.
- [- initWithCredentialIdentity:clientDataHash:userVerificationPreference:supportedAlgorithms:registrationExtensionInput:](./aspasskeycredentialrequest/initwithcredentialidentity_clientdatahash_userverificationpreference_supportedalgorithms_registrationextensioninput_.md)
  Initializes a passkey credential request, providing additional passkey registration data.
### Viewing passkey challenge information
- [var clientDataHash: Data](./aspasskeycredentialrequest/clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./aspasskeycredentialrequest/userverificationpreference.md)
  The relying party’s user verification preference.
- [var supportedAlgorithms: [ASCOSEAlgorithmIdentifier]](./aspasskeycredentialrequest/supportedalgorithms-74mad.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [var extensionInput: ASPasskeyCredentialExtensionInput](./aspasskeycredentialrequest/extensioninput.md)
  An input for WebAuthn extensions.
- [enum ASPasskeyCredentialExtensionInput](./aspasskeycredentialextensioninput.md)
  A type for WebAuthn extension inputs.
- [supportedAlgorithms](./aspasskeycredentialrequest/supportedalgorithms-27z68.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [assertionExtensionInput](./aspasskeycredentialrequest/assertionextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyAssertionCredentialExtensionInput](./aspasskeyassertioncredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey assertion.
- [registrationExtensionInput](./aspasskeycredentialrequest/registrationextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyRegistrationCredentialExtensionInput](./aspasskeyregistrationcredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey registration.
### Initializers
- [init?(coder: NSCoder)](./aspasskeycredentialrequest/init%28coder%29.md)
### Instance Properties
- [var excludedCredentials: [ASAuthorizationPlatformPublicKeyCredentialDescriptor]?](./aspasskeycredentialrequest/excludedcredentials.md)
  A list of IDs that represent existing passkeys for the account, to prevent creation of duplicate passkeys.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASCredentialRequest](./ascredentialrequest.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

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
- [class ASPasskeyCredentialRequestParameters](./aspasskeycredentialrequestparameters.md)
  A class that represents information about a passkey credential request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest)*