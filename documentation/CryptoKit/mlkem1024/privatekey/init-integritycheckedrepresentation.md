# init(integrityCheckedRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Initializes a private key from an integrity-checked representation.

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
init<D>(integrityCheckedRepresentation: D) throws where D : DataProtocol
```

## Parameters

- `integrityCheckedRepresentation`: A representation of the private key that includes the seed value, and a hash of the corresponding public key.

## See Also

- [static func generate() throws -> MLKEM1024.PrivateKey](mlkem1024/privatekey/generate.md)
  Generates a new, random private key.
- [init() throws](mlkem1024/privatekey/init.md)
  Initializes a random private key.
- [init<D>(seedRepresentation: D, publicKey: MLKEM1024.PublicKey?) throws](mlkem1024/privatekey/init(seedrepresentation:publickey:).md)
  Initializes a private key from a seed representation and optional public key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/init(integritycheckedrepresentation:))*