# integrityCheckedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property

An integrity-checked representation of the private key.

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
var integrityCheckedRepresentation: Data { get }
```

#### Discussion

This representation includes the seed value, and a hash of the corresponding public key.

## See Also

- [var publicKey: MLKEM768.PublicKey](mlkem768/privatekey/publickey.md)
  The corresponding public key.
- [var seedRepresentation: Data](mlkem768/privatekey/seedrepresentation.md)
  The private key’s seed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem768/privatekey/integritycheckedrepresentation)*