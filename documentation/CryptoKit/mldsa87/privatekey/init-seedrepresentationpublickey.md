# init(seedRepresentation:publicKey:)

**Framework**: Apple CryptoKit  
**Kind**: init

Initializes a private key from the seed representation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

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

- [init() throws](mldsa87/privatekey/init.md)
  Initializes a new random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mldsa87/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked data representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mldsa87/privatekey/init(seedrepresentation:publickey:))*