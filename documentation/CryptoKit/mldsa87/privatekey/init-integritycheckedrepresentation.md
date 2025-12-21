# init(integrityCheckedRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Initializes a private key from an integrity-checked data representation.

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
init<D>(integrityCheckedRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `integrityCheckedRepresentation`: The integrity-checked data representation of the private key.   The parameter needs to be 64 bytes long, and contain the seed and a hash of the public key.

## See Also

- [init() throws](mldsa87/privatekey/init.md)
  Initializes a new random private key.
- [init<D>(seedRepresentation: D, publicKey: MLDSA87.PublicKey?) throws](mldsa87/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from the seed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey/init(integritycheckedrepresentation:))*