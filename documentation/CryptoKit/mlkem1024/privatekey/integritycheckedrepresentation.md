# integrityCheckedRepresentation

**Framework**: Apple CryptoKit  
**Kind**: property  
**Role**: Instance Property

An integrity-checked representation of the private key.

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
var integrityCheckedRepresentation: Data { get }
```

#### Discussion

This representation includes the seed value, and a hash of the corresponding public key.

## See Also

### Inspecting a private key’s properties
- [var publicKey: MLKEM1024.PublicKey](./publickey.md)
  The corresponding public key.
- [var seedRepresentation: Data](./seedrepresentation.md)
  The private key’s seed representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/mlkem1024/privatekey/integritycheckedrepresentation)*