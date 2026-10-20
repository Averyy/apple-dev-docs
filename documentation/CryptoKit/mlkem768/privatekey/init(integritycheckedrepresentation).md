# init(integrityCheckedRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Initializes a private key from an integrity-checked representation.

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

- `integrityCheckedRepresentation`: A representation of the private key that includes the seed value, and a hash of the corresponding public key.

## See Also

### Creating a private key
- [static func generate() throws -> MLKEM768.PrivateKey](./generate%28%29.md)
  Generates a new, random private key.
- [init() throws](./init%28%29.md)
  Initializes a random private key.
- [init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws](./init%28seedrepresentation,publickey%29.md)
  Initializes a private key from a seed representation and optional public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/init(integritycheckedrepresentation:))*