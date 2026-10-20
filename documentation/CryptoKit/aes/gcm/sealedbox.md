# AES.GCM.SealedBox

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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

Use a sealed box as a container for data that you want to transmit securely. Seal data into a box with one of the cipher algorithms, like [`seal(_:using:nonce:)`](./seal%28_,using,nonce%29.md).

The box holds an encrypted version of the original data, an authentication tag, and the nonce during encryption. The encryption makes the data unintelligible to anyone without the key, while the authentication tag makes it possible for the intended receiver to be sure the data remains intact.

The receiver uses another instance of the same cipher, like the [`open(_:using:)`](./open%28_,using%29.md) method, to open the box.

## Topics

### Creating the sealed box
- [init<C, T>(nonce: AES.GCM.Nonce, ciphertext: C, tag: T) throws](./sealedbox/init%28nonce,ciphertext,tag%29.md)
  Creates a sealed box from the given tag, nonce, and ciphertext.
- [init<D>(combined: D) throws](./sealedbox/init%28combined%29.md)
  Creates a sealed box from the combined bytes of an authentication tag, nonce, and encrypted data.
### Retrieving the combined contents
- [var combined: Data?](./sealedbox/combined.md)
  A combined element composed of the nonce, encrypted data, and authentication tag.
### Inspecting the component elements
- [var nonce: AES.GCM.Nonce](./sealedbox/nonce.md)
  The nonce used to encrypt the data.
- [var ciphertext: Data](./sealedbox/ciphertext.md)
  The encrypted data.
- [var tag: Data](./sealedbox/tag.md)
  An authentication tag.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox)*