# SecTrustSettingsKeyUsage

**Framework**: Security  
**Kind**: struct

Allowed uses for the encryption key in a certificate.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
struct SecTrustSettingsKeyUsage
```

## Topics

### Initializers
- [init(rawValue: UInt32)](sectrustsettingskeyusage/init(rawvalue:).md)
  Initializes a trust settings key usage structure.
### Constants
- [static var useSignature: SecTrustSettingsKeyUsage](sectrustsettingskeyusage/usesignature.md)
  The key can be used to sign data or verify a signature.
- [static var useEnDecryptData: SecTrustSettingsKeyUsage](sectrustsettingskeyusage/useendecryptdata.md)
  The key can be used to encrypt or decrypt data.
- [static var useEnDecryptKey: SecTrustSettingsKeyUsage](sectrustsettingskeyusage/useendecryptkey.md)
  The key can be used to encrypt or decrypt (wrap or unwrap) a key.
- [static var useSignCert: SecTrustSettingsKeyUsage](sectrustsettingskeyusage/usesigncert.md)
  The key can be used to sign a certificate or verify a signature.
- [static var useSignRevocation: SecTrustSettingsKeyUsage](sectrustsettingskeyusage/usesignrevocation.md)
  The key can be used to sign an OCSP (online certificate status protocol) message or CRL (certificate verification list), or to verify a signature.
- [static var useKeyExchange: SecTrustSettingsKeyUsage](sectrustsettingskeyusage/usekeyexchange.md)
  The key is a private key that has been shared using a key exchange protocol, such as Diffie-Hellman key exchange.
- [static var useAny: SecTrustSettingsKeyUsage](sectrustsettingskeyusage/useany.md)
  The key can be used for any purpose.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sectrustsettingskeyusage)*