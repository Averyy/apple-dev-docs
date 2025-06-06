# seal(_:using:nonce:)

**Framework**: Apple CryptoKit  
**Kind**: method

Secures the given plaintext message with encryption and an authentication tag.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func seal<Plaintext>(_ message: Plaintext, using key: SymmetricKey, nonce: ChaChaPoly.Nonce? = nil) throws -> ChaChaPoly.SealedBox where Plaintext : DataProtocol
```

#### Return Value

The sealed message.

## Parameters

- `message`: The plaintext data to seal.
- `key`: A cryptographic key used to seal the message.
- `nonce`: The nonce the sealing process requires. If you don’t provide a nonce, the method generates a random one by invoking  .

## See Also

- [static func seal<Plaintext, AuthenticatedData>(Plaintext, using: SymmetricKey, nonce: ChaChaPoly.Nonce?, authenticating: AuthenticatedData) throws -> ChaChaPoly.SealedBox](chachapoly/seal(_:using:nonce:authenticating:).md)
  Secures the given plaintext message with encryption and an authentication tag that covers both the encrypted data and additional data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/seal(_:using:nonce:))*