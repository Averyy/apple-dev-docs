# AES.GCM

**Framework**: Apple CryptoKit  
**Kind**: enum  
**Role**: Enumeration

The Advanced Encryption Standard (AES) Galois Counter Mode (GCM) cipher suite.

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
enum GCM
```

## Topics

### Storing the output
- [AES.GCM.SealedBox](./gcm/sealedbox.md)
  A secure container for your data that you can access using a cipher.
### Getting a nonce
- [AES.GCM.Nonce](./gcm/nonce.md)
  A value used once during a cryptographic operation and then discarded.
### Securing the plaintext message
- [static func seal<Plaintext>(Plaintext, using: SymmetricKey, nonce: AES.GCM.Nonce?) throws -> AES.GCM.SealedBox](./gcm/seal%28_,using,nonce%29.md)
  Secures the given plaintext message with encryption and an authentication tag.
- [static func seal<Plaintext, AuthenticatedData>(Plaintext, using: SymmetricKey, nonce: AES.GCM.Nonce?, authenticating: AuthenticatedData) throws -> AES.GCM.SealedBox](./gcm/seal%28_,using,nonce,authenticating%29.md)
  Secures the given plaintext message with encryption and an authentication tag that covers both the encrypted data and additional data.
### Decrypting and verifying the message
- [static func open(AES.GCM.SealedBox, using: SymmetricKey) throws -> Data](./gcm/open%28_,using%29.md)
  Decrypts the message and verifies its authenticity.
- [static func open<AuthenticatedData>(AES.GCM.SealedBox, using: SymmetricKey, authenticating: AuthenticatedData) throws -> Data](./gcm/open%28_,using,authenticating%29.md)
  Decrypts the message and verifies the authenticity of both the encrypted message and additional data.
### Type Methods
- [static func open(inPlace: inout MutableRawSpan, using: SymmetricKey, nonce: AES.GCM.Nonce, authenticating: RawSpan?, tag: RawSpan) throws](./gcm/open%28inplace,using,nonce,authenticating,tag%29.md)
  Decrypts the message and verifies its authenticity.
- [static func seal(inPlace: inout MutableRawSpan, using: SymmetricKey, nonce: AES.GCM.Nonce, authenticating: RawSpan?, tag: inout OutputRawSpan) throws](./gcm/seal%28inplace,using,nonce,authenticating,tag%29.md)
  Secures the given plaintext message with encryption and an optional authentication tag.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm)*