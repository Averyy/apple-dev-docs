# SCEPCredential

**Framework**: Device Management  
**Kind**: dictionary

A SCEP identity that the device generates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+
- watchOS 10.0+

## Declaration

```swift
object SCEPCredential
```

## Topics

### Objects
- [object SCEPCredentialSubjectAltNameObject](scepcredentialsubjectaltnameobject.md)
  The subject’s alternative name for the certificate.

## Properties

- `CAFingerprint` (string): The fingerprint of the Certificate Authority certificate.
- `Challenge` (string): A preshared secret.
- `Key Type` (string): The key type, which always has the value `RSA`.
- `Key Usage` (integer): A bitmask that specifies the use of the key: `1` is signing, `4` is encryption, and `5` is both signing and encryption. Some certificate authorities, such as Windows CA, support only encryption or signing, but not both at the same time.
- `Keysize` (integer): The key size in bits, either `1024`, `2048`, or `4096`.
- `Name` (string): Any string that the SCEP server recognizes. For example, it could be a domain name such as `example.org`. If a certificate authority has multiple CA certificates, you can use this field to specify the required certificate.
- `Retries` (integer): The number of times the device should retry if the server sends a `PENDING` response.
- `RetryDelay` (integer): The number of seconds to wait between subsequent retries. The system makes the first retry without this delay.
- `Subject` ([[[string]]]): The representation of an X.500 name is an array of OID and value. For example, `/C=US/O=Apple Inc./CN=foo/1.2.5.3=bar` corresponds to: `[ [ ["C", "US"] ], [ ["O", "Apple Inc."] ], [ [ "CN", "foo"] ], [ [ "1.2.5.3", "bar" ] ] ]` You can represent OIDs as dotted numbers or use shortcuts for country (`C`), locality (`L`), state (`ST`), organization (`O`), organizational unit (`OU`), and common name (`CN`).
- `SubjectAltName` (SCEPCredentialSubjectAltNameObject): The subject’s alternative name for the certificate.
- `URL` (string) *(required)*: The SCEP URL.

## See Also

- [object ACMECredential](acmecredential.md)
  An ACME identity that the device generates.
- [object IdentityCredential](identitycredential.md)
  The data for a PKCS #12 password-protected identity.
- [object UserNameAndPasswordCredential](usernameandpasswordcredential.md)
  Data that describes a credential that represents a user name and password.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/scepcredential)*