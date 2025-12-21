# init(seedRepresentation:publicKey:)

**Framework**: Apple CryptoKit  
**Kind**: init

Initializes a private key from a seed representation and optional public key.

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
init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws where D : DataProtocol
```

## Parameters

- `seedRepresentation`: The seed representation  , as specified in the   algorithm (Algorithm 16) of FIPS 203.
- `publicKey`: An optional public key. Pass this to check that the initialized private key is consistent with the public key. The initializer throws if the public key doesn’t match the expected value.

## See Also

- [static func generate() throws -> MLKEM768.PrivateKey](mlkem768/privatekey/generate.md)
  Generates a new, random private key.
- [init() throws](mlkem768/privatekey/init.md)
  Initializes a random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mlkem768/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/init(seedrepresentation:publickey:))*