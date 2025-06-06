# ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor

**Framework**: Authentication Services  
**Kind**: class

An object that holds public key credential transport information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor
```

#### Overview

This class ties together a credential and its corresponding transport types (USB, NFC, Bluetooth, or all of them).

## Topics

### Creating the descriptor
- [init(credentialID: Data, transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport])](asauthorizationsecuritykeypublickeycredentialdescriptor/init(credentialid:transports:).md)
  Creates the object with the credential ID and the array of transports.
- [var transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialdescriptor/transports.md)
  The array of transport types.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialDescriptor](asauthorizationpublickeycredentialdescriptor.md)
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

## See Also

- [protocol ASPublicKeyCredential](aspublickeycredential.md)
  An interface that defines the properties of the public key.
- [class ASAuthorizationPublicKeyCredentialParameters](asauthorizationpublickeycredentialparameters.md)
  An object that provides required parameters for the credential during registration.
- [struct ASCOSEAlgorithmIdentifier](ascosealgorithmidentifier.md)
  An identifier for the algorithm that a credential’s key pair uses.
- [struct ASCOSEEllipticCurveIdentifier](ascoseellipticcurveidentifier.md)
  A structure that contains the elliptic curve identifier.
- [struct ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind.md)
  A structure that defines the types of attestations a developer can request.
- [struct ASAuthorizationPublicKeyCredentialResidentKeyPreference](asauthorizationpublickeycredentialresidentkeypreference.md)
  A structure that specifies the relying party’s preference for resident key storage.
- [struct ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialuserverificationpreference.md)
  A structure that defines the relying party’s user verification preference.
- [protocol ASAuthorizationPublicKeyCredentialDescriptor](asauthorizationpublickeycredentialdescriptor.md)
  An interface that defines the credential identifier.
- [class ASAuthorizationPlatformPublicKeyCredentialDescriptor](asauthorizationplatformpublickeycredentialdescriptor.md)
  An object that holds the credential.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.
- [static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md)
  An array of currently supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialdescriptor)*