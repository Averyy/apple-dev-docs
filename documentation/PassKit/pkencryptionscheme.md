# PKEncryptionScheme

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

Encryption schemes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct PKEncryptionScheme
```

## Topics

### Creating an encryption scheme
- [init(rawValue: String)](pkencryptionscheme/init(rawvalue:).md)
  Initialize an encryption scheme using a string.
### Encryption schemes
- [static let ECC_V2: PKEncryptionScheme](pkencryptionscheme/ecc_v2.md)
  The elliptic curve cryptography (ECC) scheme.
- [static let RSA_V2: PKEncryptionScheme](pkencryptionscheme/rsa_v2.md)
  The RSA v2 scheme.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(encryptionScheme: PKEncryptionScheme)](pkaddpaymentpassrequestconfiguration/init(encryptionscheme:).md)
  Instantiates a new request configuration with the given encryption scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkencryptionscheme)*