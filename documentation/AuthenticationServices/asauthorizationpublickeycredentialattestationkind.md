# ASAuthorizationPublicKeyCredentialAttestationKind

**Framework**: Authentication Services  
**Kind**: struct

A structure that defines the types of attestations a developer can request.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialAttestationKind
```

## Topics

### Creating the attestation type
- [init(String)](asauthorizationpublickeycredentialattestationkind/init(_:).md)
  Creates the object with an attestation type.
- [init(rawValue: String)](asauthorizationpublickeycredentialattestationkind/init(rawvalue:).md)
  Creates the object with an attestation type.
### Getting attestation types
- [static let none: ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind/none.md)
  An attestation kind of none.
- [static let direct: ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind/direct.md)
  An attestation kind of direct.
- [static let enterprise: ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind/enterprise.md)
  An attestation kind of enterprise.
- [static let indirect: ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind/indirect.md)
  An attestation kind of indirect.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
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
- [struct ASAuthorizationPublicKeyCredentialResidentKeyPreference](asauthorizationpublickeycredentialresidentkeypreference.md)
  A structure that specifies the relying party’s preference for resident key storage.
- [struct ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialuserverificationpreference.md)
  A structure that defines the relying party’s user verification preference.
- [protocol ASAuthorizationPublicKeyCredentialDescriptor](asauthorizationpublickeycredentialdescriptor.md)
  An interface that defines the credential identifier.
- [class ASAuthorizationPlatformPublicKeyCredentialDescriptor](asauthorizationplatformpublickeycredentialdescriptor.md)
  An object that holds the credential.
- [class ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor](asauthorizationsecuritykeypublickeycredentialdescriptor.md)
  An object that holds public key credential transport information.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.
- [static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md)
  An array of currently supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialattestationkind)*