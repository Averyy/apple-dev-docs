# hkdfDerivedSymmetricKey(using:salt:sharedInfo:outputByteCount:)

**Framework**: Apple CryptoKit  
**Kind**: method

Derives a symmetric encryption key from the secret using HKDF key derivation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func hkdfDerivedSymmetricKey<H, Salt, SI>(using hashFunction: H.Type, salt: Salt, sharedInfo: SI, outputByteCount: Int) -> SymmetricKey where H : HashFunction, Salt : DataProtocol, SI : DataProtocol
```

#### Return Value

The derived symmetric key.

## Parameters

- `hashFunction`: The hash function to use for key derivation.
- `salt`: The salt to use for key derivation.
- `sharedInfo`: The shared information to use for key derivation.
- `outputByteCount`: The length in bytes of resulting symmetric key.

## See Also

- [func x963DerivedSymmetricKey<H, SI>(using: H.Type, sharedInfo: SI, outputByteCount: Int) -> SymmetricKey](sharedsecret/x963derivedsymmetrickey(using:sharedinfo:outputbytecount:).md)
  Derives a symmetric encryption key from the secret using x9.63 key derivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sharedsecret/hkdfderivedsymmetrickey(using:salt:sharedinfo:outputbytecount:))*