# init()

**Framework**: Apple CryptoKit  
**Kind**: init

Initializes a random private key.

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
init() throws
```

## See Also

- [static func generate() throws -> MLKEM768.PrivateKey](mlkem768/privatekey/generate.md)
  Generates a new, random private key.
- [init<D>(integrityCheckedRepresentation: D) throws](mlkem768/privatekey/init(integritycheckedrepresentation:).md)
  Initializes a private key from an integrity-checked representation.
- [init<D>(seedRepresentation: D, publicKey: MLKEM768.PublicKey?) throws](mlkem768/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from a seed representation and optional public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/init())*