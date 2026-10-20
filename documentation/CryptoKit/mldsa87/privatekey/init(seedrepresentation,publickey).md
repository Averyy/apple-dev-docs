# init(seedRepresentation:publicKey:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Initializes a private key from the seed representation.

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
init<D>(seedRepresentation: D, publicKey: MLDSA87.PublicKey?) throws where D : DataProtocol
```

#### Discussion

This initializer implements the `ML-DSA.KeyGen_internal` algorithm (Algorithm 16) of FIPS 204.

If a public key is provided, a consistency check is performed between it and the derived public key.

## Parameters

- `seedRepresentation`: The seed representation of the private key. This parameter needs to be 32 bytes long.
- `publicKey`: The public key associated with the secret key.

## See Also

### Creating a private key
- [init() throws](./init%28%29.md)
  Creates a random MLDSA87 private key.
- [init<D>(integrityCheckedRepresentation: D) throws](./init%28integritycheckedrepresentation%29.md)
  Initializes a private key from an integrity-checked data representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey/init(seedrepresentation:publickey:))*