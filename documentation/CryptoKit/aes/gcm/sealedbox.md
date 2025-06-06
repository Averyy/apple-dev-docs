# AES.GCM.SealedBox

**Framework**: Apple CryptoKit  
**Kind**: struct

A secure container for your data that you can access using a cipher.

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
struct SealedBox
```

#### Overview

Use a sealed box as a container for data that you want to transmit securely. Seal data into a box with one of the cipher algorithms, like [`seal(_:using:nonce:)`](aes/gcm/seal(_:using:nonce:).md).

The box holds an encrypted version of the original data, an authentication tag, and the nonce during encryption. The encryption makes the data unintelligible to anyone without the key, while the authentication tag makes it possible for the intended receiver to be sure the data remains intact.

The receiver uses another instance of the same cipher, like the [`open(_:using:)`](aes/gcm/open(_:using:).md) method, to open the box.

## Topics

### Creating the sealed box
- [init<C, T>(nonce: AES.GCM.Nonce, ciphertext: C, tag: T) throws](aes/gcm/sealedbox/init(nonce:ciphertext:tag:).md)
  Creates a sealed box from the given tag, nonce, and ciphertext.
- [init<D>(combined: D) throws](aes/gcm/sealedbox/init(combined:).md)
  Creates a sealed box from the combined bytes of an authentication tag, nonce, and encrypted data.
### Retrieving the combined contents
- [var combined: Data?](aes/gcm/sealedbox/combined.md)
  A combined element composed of the nonce, encrypted data, and authentication tag.
### Inspecting the component elements
- [var nonce: AES.GCM.Nonce](aes/gcm/sealedbox/nonce.md)
  The nonce used to encrypt the data.
- [var ciphertext: Data](aes/gcm/sealedbox/ciphertext.md)
  The encrypted data.
- [var tag: Data](aes/gcm/sealedbox/tag.md)
  An authentication tag.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox)*