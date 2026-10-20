# PKEncryptionScheme

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct  
**Role**: Structure

Encryption schemes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS
- watchOS

## Declaration

```swift
struct PKEncryptionScheme
```

```c
typedef NSString * PKEncryptionScheme;
```

## Topics

### Creating an encryption scheme
- [init(rawValue: String)](./pkencryptionscheme/init%28rawvalue%29.md)
  Initialize an encryption scheme using a string.
### Encryption schemes
- [static let ECC_V2: PKEncryptionScheme](./pkencryptionscheme/ecc_v2.md)
  The elliptic curve cryptography (ECC) scheme.
- [static let RSA_V2: PKEncryptionScheme](./pkencryptionscheme/rsa_v2.md)
  The RSA v2 scheme.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a request configuration
- [init?(encryptionScheme: PKEncryptionScheme)](./pkaddpaymentpassrequestconfiguration/init%28encryptionscheme%29.md)
  Instantiates a new request configuration with the given encryption scheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkencryptionscheme)*