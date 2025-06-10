# ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport

**Framework**: Authentication Services  
**Kind**: struct

A structure that defines the security key credential transport type.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
struct Transport
```

## Topics

### Creating the transport type
- [init(String)](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/init(_:).md)
  Creates the object with a transport type.
- [init(rawValue: String)](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/init(rawvalue:).md)
  Creates the object with a preference.
### Getting the properties
- [static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md)
  An array of currently supported transport types.
- [static let bluetooth: ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/bluetooth.md)
  The Bluetooth transport type.
- [static let nfc: ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/nfc.md)
  The Near Field Communication transport type.
- [static let usb: ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/usb.md)
  The USB transport type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [static var allSupported: [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor.Transport]](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md)
  An array of currently supported transport types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationsecuritykeypublickeycredentialdescriptor/transport)*