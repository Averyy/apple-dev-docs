# init()

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Initializes a random private key.

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

## See Also

### Creating a private key
- [static func generate() throws -> MLKEM768.PrivateKey](./generate%28%29.md)
  Generates a new, random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](./init%28integritycheckedrepresentation%29.md)
  Initializes a private key from an integrity-checked representation.
- [init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws](./init%28seedrepresentation,publickey%29.md)
  Initializes a private key from a seed representation and optional public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/init())*