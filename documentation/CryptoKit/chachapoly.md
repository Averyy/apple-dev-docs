# ChaChaPoly

**Framework**: Apple CryptoKit  
**Kind**: enum  
**Role**: Enumeration

An implementation of the ChaCha20-Poly1305 cipher.

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
enum ChaChaPoly
```

## Topics

### Storing the output
- [ChaChaPoly.SealedBox](./chachapoly/sealedbox.md)
  A secure container for your data that you access using a cipher.
### Getting a nonce
- [ChaChaPoly.Nonce](./chachapoly/nonce.md)
  A value used once during a cryptographic operation and then discarded.
### Securing the plaintext message
- [static func seal<Plaintext>(Plaintext, using: SymmetricKey, nonce: ChaChaPoly.Nonce?) throws -> ChaChaPoly.SealedBox](./chachapoly/seal%28_,using,nonce%29.md)
  Secures the given plaintext message with encryption and an authentication tag.
- [static func seal<Plaintext, AuthenticatedData>(Plaintext, using: SymmetricKey, nonce: ChaChaPoly.Nonce?, authenticating: AuthenticatedData) throws -> ChaChaPoly.SealedBox](./chachapoly/seal%28_,using,nonce,authenticating%29.md)
  Secures the given plaintext message with encryption and an authentication tag that covers both the encrypted data and additional data.
### Decrypting and verifying the message
- [static func open(ChaChaPoly.SealedBox, using: SymmetricKey) throws -> Data](./chachapoly/open%28_,using%29.md)
  Decrypts the message and verifies its authenticity.
- [static func open<AuthenticatedData>(ChaChaPoly.SealedBox, using: SymmetricKey, authenticating: AuthenticatedData) throws -> Data](./chachapoly/open%28_,using,authenticating%29.md)
  Decrypts the message and verifies the authenticity of both the encrypted message and additional data.
### Type Methods
- [static func open(inPlace: inout MutableRawSpan, using: SymmetricKey, nonce: ChaChaPoly.Nonce, authenticating: RawSpan?, tag: RawSpan) throws](./chachapoly/open%28inplace,using,nonce,authenticating,tag%29.md)
  Decrypts the message and verifies the authenticity of both the encrypted message and additional data.
- [static func seal(inPlace: inout MutableRawSpan, using: SymmetricKey, nonce: ChaChaPoly.Nonce, authenticating: RawSpan?, tag: inout OutputRawSpan) throws](./chachapoly/seal%28inplace,using,nonce,authenticating,tag%29.md)
  Secures the given plaintext message in place with encryption and an authentication tag.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Ciphers
- [enum AES](./aes.md)
  A container for Advanced Encryption Standard (AES) ciphers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly)*