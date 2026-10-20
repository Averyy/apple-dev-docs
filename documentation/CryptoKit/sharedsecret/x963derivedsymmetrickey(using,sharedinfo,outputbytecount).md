# x963DerivedSymmetricKey(using:sharedInfo:outputByteCount:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Instance Method

Derives a symmetric encryption key from the secret using x9.63 key derivation.

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
func x963DerivedSymmetricKey<H, SI>(using hashFunction: H.Type, sharedInfo: SI, outputByteCount: Int) -> SymmetricKey where H : HashFunction, SI : DataProtocol
```

#### Return Value

The derived symmetric key.

## Parameters

- `hashFunction`: The hash function to use for key derivation.
- `sharedInfo`: The shared information to use for key derivation.
- `outputByteCount`: The length in bytes of resulting symmetric key.

## See Also

### Deriving keys
- [func hkdfDerivedSymmetricKey<H, Salt, SI>(using: H.Type, salt: Salt, sharedInfo: SI, outputByteCount: Int) -> SymmetricKey](./hkdfderivedsymmetrickey%28using,salt,sharedinfo,outputbytecount%29.md)
  Derives a symmetric encryption key from the secret using HKDF key derivation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sharedsecret/x963derivedsymmetrickey(using:sharedinfo:outputbytecount:))*