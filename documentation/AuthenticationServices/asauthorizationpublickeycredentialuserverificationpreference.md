# ASAuthorizationPublicKeyCredentialUserVerificationPreference

**Framework**: Authentication Services  
**Kind**: struct

A structure that defines the relying party’s user verification preference.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialUserVerificationPreference
```

## Topics

### Creating the preference
- [init(String)](asauthorizationpublickeycredentialuserverificationpreference/init(_:).md)
  Creates the object with a preference.
- [init(rawValue: String)](asauthorizationpublickeycredentialuserverificationpreference/init(rawvalue:).md)
  Creates the object with a preference.
### Getting preferences
- [static let discouraged: ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialuserverificationpreference/discouraged.md)
  The relying party discourages user verification.
- [static let preferred: ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialuserverificationpreference/preferred.md)
  The relying party prefers user verification.
- [static let required: ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialuserverificationpreference/required.md)
  The relying party requires user verification.

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
- [struct ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind.md)
  A structure that defines the types of attestations a developer can request.
- [struct ASAuthorizationPublicKeyCredentialResidentKeyPreference](asauthorizationpublickeycredentialresidentkeypreference.md)
  A structure that specifies the relying party’s preference for resident key storage.
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

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialuserverificationpreference)*