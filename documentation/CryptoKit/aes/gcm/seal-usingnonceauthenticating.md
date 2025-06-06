# seal(_:using:nonce:authenticating:)

**Framework**: Apple CryptoKit  
**Kind**: method

Secures the given plaintext message with encryption and an authentication tag that covers both the encrypted data and additional data.

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
static func seal<Plaintext, AuthenticatedData>(_ message: Plaintext, using key: SymmetricKey, nonce: AES.GCM.Nonce? = nil, authenticating authenticatedData: AuthenticatedData) throws -> AES.GCM.SealedBox where Plaintext : DataProtocol, AuthenticatedData : DataProtocol
```

#### Return Value

The sealed message.

## Parameters

- `message`: The plaintext data to seal.
- `key`: A cryptographic key used to seal the message.
- `nonce`: The nonce the sealing process requires. If you don’t provide a nonce, the method generates a random one by invoking  .
- `authenticatedData`: Additional data to be authenticated.

## See Also

- [static func seal<Plaintext>(Plaintext, using: SymmetricKey, nonce: AES.GCM.Nonce?) throws -> AES.GCM.SealedBox](aes/gcm/seal(_:using:nonce:).md)
  Secures the given plaintext message with encryption and an authentication tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/seal(_:using:nonce:authenticating:))*