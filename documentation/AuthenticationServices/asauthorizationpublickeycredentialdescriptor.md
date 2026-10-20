# ASAuthorizationPublicKeyCredentialDescriptor

**Framework**: Authentication Services  
**Kind**: protocol  
**Role**: Protocol

An interface that defines the credential identifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
protocol ASAuthorizationPublicKeyCredentialDescriptor : NSCopying, NSSecureCoding, NSObjectProtocol
```

```objc
@protocol ASAuthorizationPublicKeyCredentialDescriptor <NSObject, NSSecureCoding, NSCopying>
```

## Topics

### Getting the credential
- [var credentialID: Data](./asauthorizationpublickeycredentialdescriptor/credentialid.md)
  An identifier the authenticator generates during registration to uniquely identify a specific credential.

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
### Conforming Types
- [ASAuthorizationPlatformPublicKeyCredentialDescriptor](./asauthorizationplatformpublickeycredentialdescriptor.md)
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor](./asauthorizationsecuritykeypublickeycredentialdescriptor.md)

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
- [class ASAuthorizationPlatformPublicKeyCredentialDescriptor](./asauthorizationplatformpublickeycredentialdescriptor.md)
  An object that holds the credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor](./asauthorizationsecuritykeypublickeycredentialdescriptor.md)
  An object that holds public key credential transport information.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](./asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.
- [static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](./asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md)
  An array of currently supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialdescriptor)*