# ACMECredential

**Framework**: Device Management  
**Kind**: dictionary

An ACME identity that the device generates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object ACMECredential
```

#### Discussion

##### Acme Attestation Hardware Support

The following table indicates which System on Chips (SoCs) support ACME attestation. If the Attest key is ignored, the ACME server does not receive an attestation.

| Attest key support | iPhone, iPad | Mac | Apple TV | Apple Watch | Vision Pro |
| --- | --- | --- | --- | --- | --- |
| Ignored | A10x Fusion and earlier | Intel | A10x Fusion and earlier | S3 and earlier | none |
| Supported | A11 Bionic and laterAll M series | Apple Silicon | A12 Bionic and later | S4 and later | All |

## Topics

### Objects
- [object ACMECredentialSubjectAltNameObject](acmecredentialsubjectaltnameobject.md)
  Specifies the subject’s alternative name that the device requests for the certificate that the ACME server issues.

## See Also

- [object IdentityCredential](identitycredential.md)
  The data for a PKCS #12 password-protected identity.
- [object SCEPCredential](scepcredential.md)
  An SCEP identity that the device generates.
- [object UserNameAndPasswordCredential](usernameandpasswordcredential.md)
  Data that describes a credential that represents a user name and password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/acmecredential)*