# allSupported

**Framework**: Authentication Services  
**Kind**: property

An array of currently supported transport types.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport] { get }
```

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
- [class ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor](asauthorizationsecuritykeypublickeycredentialdescriptor.md)
  An object that holds public key credential transport information.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md)
  A structure that defines the security key credential transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported)*