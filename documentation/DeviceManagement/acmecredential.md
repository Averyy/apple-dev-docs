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

This schema specifies how the device requests a client certificate from an Automated Certificate Management Environment (ACME) server. Use this to create a JSON document that the device downloads when resolving an asset.

When the device resolves the asset, first it generates an asymmetric key pair based upon the `KeyType`, `KeySize`, and `HardwareBound` fields. Then the device communicates with the ACME server. It requests a new order using the `ClientIdentifier` as the `permanent-identifier`. The ACME server responds with a challenge type of `device-attest-01`. If `Attest` is `true` the device requests an attestation of the key and device properties. Then it replies to the challenge with a WebAuthn attestation statement, and this contains the attestation if the device obtained one. The device submits a certificate signing request matching the key and containing the `ClientIdentifier`, `Subject`, `SubjectAltName`, `UsageFlags`, and `ExtendedKeyUsage` fields. The ACME server issues a certificate, and the device stores the resulting identity.

For details on the content of the attestation provided to the ACME server, see the documentation of the `DevicePropertiesAttestation` key in the [`DeviceInformationResponse.QueryResponses`](deviceinformationresponse/queryresponses-data.dictionary.md) response. In the attestation certificate the value of the freshness code OID is the SHA-256 hash of the `token` from the `device-attest-01` challenge.

##### Acme Attestation Hardware Support

The following table indicates which System on Chips (SoCs) support ACME attestation. If the Attest key is ignored, the ACME server does not receive an attestation.

| Attest key support | iPhone, iPad | Mac | Apple TV | Apple Watch | Vision Pro |
| --- | --- | --- | --- | --- | --- |
| Ignored | A10x Fusion and earlier | Intel | A10x Fusion and earlier | S3 and earlier | none |
| Supported | A11 Bionic and laterAll M series | Apple Silicon | A12 Bionic and later | S4 and later | All |

##### Credential Example

```json
{
    "DirectoryURL": "https://example.com/acme/dir",
    "ClientIdentifier": "This is a ClientIdentifier",
    "KeySize": 384,
    "KeyType": "ECSECPrimeRandom",
    "HardwareBound": true,
    "Subject": [[["C", "US"]], [["O", "Example Inc."]], [["1.2.840.113635.100.6.99999.99999", "test custom OID value"]]],
    "SubjectAltName": {
        "dNSName": "site.example.com",
        "rfc822Name": "rfc822",
        "uniformResourceIdentifier": "https://www.example.com/",
        "ntPrincipalName": "Principal Example"
    },
    "UsageFlags": 5,
    "ExtendedKeyUsage": [
        "1.3.6.1.5.5.7.3.2"
    ],
    "Attest": true
}
```

## Topics

### Objects
- [object ACMECredentialSubjectAltNameObject](acmecredentialsubjectaltnameobject.md)
  Specifies the subject’s alternative name that the device requests for the certificate that the ACME server issues.

## See Also

- [object IdentityCredential](identitycredential.md)
  The data for a PKCS #12 password-protected identity.
- [object SCEPCredential](scepcredential.md)
  A SCEP identity that the device generates.
- [object UserNameAndPasswordCredential](usernameandpasswordcredential.md)
  Data that describes a credential that represents a user name and password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/acmecredential)*