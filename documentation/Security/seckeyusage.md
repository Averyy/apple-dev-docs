# SecKeyUsage

**Framework**: Security  
**Kind**: struct

The flags that indicate key usage in the `KeyUsage` extension of a certificate.

**Availability**:
- macOS 10.0+

## Declaration

```swift
struct SecKeyUsage
```

## Topics

### Initializers
- [init(rawValue: UInt32)](seckeyusage/init(rawvalue:).md)
  Initializes a key usage structure.
### Flags
- [static var crlSign: SecKeyUsage](seckeyusage/crlsign.md)
  The `CRLSign` bit is set in KeyUsage extension.
- [static var contentCommitment: SecKeyUsage](seckeyusage/contentcommitment.md)
  The `ContentCommitment` bit is set in KeyUsage extension.
- [static var critical: SecKeyUsage](seckeyusage/critical.md)
  The KeyUsage extension is marked critical.
- [static var dataEncipherment: SecKeyUsage](seckeyusage/dataencipherment.md)
  The `DataEncipherment` bit is set in KeyUsage extension.
- [static var decipherOnly: SecKeyUsage](seckeyusage/decipheronly.md)
  The `DecipherOnly` bit is set in KeyUsage extension.
- [static var digitalSignature: SecKeyUsage](seckeyusage/digitalsignature.md)
  The `DigitalSignature` bit is set in KeyUsage extension.
- [static var encipherOnly: SecKeyUsage](seckeyusage/encipheronly.md)
  The `EncipherOnly` bit is set in KeyUsage extension.
- [static var keyAgreement: SecKeyUsage](seckeyusage/keyagreement.md)
  The `KeyAgreement` bit is set in KeyUsage extension.
- [static var keyCertSign: SecKeyUsage](seckeyusage/keycertsign.md)
  The `KeyCertSign` bit is set in KeyUsage extension.
- [static var keyEncipherment: SecKeyUsage](seckeyusage/keyencipherment.md)
  The `KeyEncipherment` bit is set in KeyUsage extension.
- [static var nonRepudiation: SecKeyUsage](seckeyusage/nonrepudiation.md)
  The `NonRepudiation` bit is set in KeyUsage extension.
- [static var all: SecKeyUsage](seckeyusage/all.md)
  All flags set.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyusage)*