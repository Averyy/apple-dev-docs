# init()

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a random MLDSA87 private key.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init() throws
```

#### Discussion

This initializer is marked `throws` to support use in generic contexts, but key generation itself doesn’t produce errors.

When you call this initializer directly on a concrete type, rather than through a generic type parameter, you can safely call `try!` to create the key:

```swift
let privateKey = try! MLDSA87.PrivateKey()
```

## See Also

- [init<D>(integrityCheckedRepresentation: D) throws](mldsa87/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked data representation.
- [init<D>(seedRepresentation: D, publicKey: MLDSA87.PublicKey?) throws](mldsa87/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from the seed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey/init())*