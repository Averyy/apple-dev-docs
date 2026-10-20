# ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

```objc
@interface ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor : NSObject
```

#### Overview

This class ties together a credential and its corresponding transport types (USB, NFC, Bluetooth, or all of them).

## Topics

### Creating the descriptor
- [init(credentialID: Data, transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport])](./asauthorizationsecuritykeypublickeycredentialdescriptor/init%28credentialid,transports%29.md)
  Creates the object with the credential ID and the array of transports.
- [var transports: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](./asauthorizationsecuritykeypublickeycredentialdescriptor/transports.md)
  The array of transport types.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](./asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.
### Initializers
- [init?(coder: NSCoder)](./asauthorizationsecuritykeypublickeycredentialdescriptor/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [ASAuthorizationPublicKeyCredentialDescriptor](./asauthorizationpublickeycredentialdescriptor.md)
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

### Request configuration
- [protocol ASPublicKeyCredential](./aspublickeycredential.md)
  An interface that defines the properties of the public key.
- [class ASAuthorizationPublicKeyCredentialParameters](./asauthorizationpublickeycredentialparameters.md)
  An object that provides required parameters for the credential during registration.
- [struct ASCOSEAlgorithmIdentifier](./ascosealgorithmidentifier.md)
  An identifier for the algorithm that a credential’s key pair uses.
- [struct ASCOSEEllipticCurveIdentifier](./ascoseellipticcurveidentifier.md)
  A structure that contains the elliptic curve identifier.
- [struct ASAuthorizationPublicKeyCredentialAttestationKind](./asauthorizationpublickeycredentialattestationkind.md)
  A structure that defines the types of attestations a developer can request.
- [struct ASAuthorizationPublicKeyCredentialResidentKeyPreference](./asauthorizationpublickeycredentialresidentkeypreference.md)
  A structure that specifies the relying party’s preference for resident key storage.
- [struct ASAuthorizationPublicKeyCredentialUserVerificationPreference](./asauthorizationpublickeycredentialuserverificationpreference.md)
  A structure that defines the relying party’s user verification preference.
- [protocol ASAuthorizationPublicKeyCredentialDescriptor](./asauthorizationpublickeycredentialdescriptor.md)
  An interface that defines the credential identifier.
- [class ASAuthorizationPlatformPublicKeyCredentialDescriptor](./asauthorizationplatformpublickeycredentialdescriptor.md)
  An object that holds the credential.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](./asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.
- [static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](./asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md)
  An array of currently supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialdescriptor)*