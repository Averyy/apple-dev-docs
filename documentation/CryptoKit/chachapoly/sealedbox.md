# ChaChaPoly.SealedBox

**Framework**: Apple CryptoKit  
**Kind**: struct

A secure container for your data that you access using a cipher.

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
@frozen
struct SealedBox
```

#### Overview

Use a sealed box as a container for data that you want to transmit securely. Seal data into a box with one of the cipher algorithms, like [`seal(_:using:nonce:)`](chachapoly/seal(_:using:nonce:).md).

The box holds an encrypted version of the original data, an authentication tag, and the nonce during encryption. The encryption makes the data unintelligible to anyone without the key, while the authentication tag makes it possible for the intended receiver to be sure the data remains intact.

The receiver uses another instance of the same cipher, like the [`open(_:using:)`](chachapoly/open(_:using:).md) method, to open the box.

## Topics

### Creating the sealed box
- [init<D>(combined: D) throws](chachapoly/sealedbox/init(combined:).md)
  Creates a sealed box from the given data.
- [init<C, T>(nonce: ChaChaPoly.Nonce, ciphertext: C, tag: T) throws](chachapoly/sealedbox/init(nonce:ciphertext:tag:).md)
  Creates a sealed box from the given tag, nonce, and ciphertext.
### Retrieving the combined contents
- [let combined: Data](chachapoly/sealedbox/combined.md)
  A combined element composed of the tag, the nonce, and the ciphertext.
### Inspecting the component elements
- [var nonce: ChaChaPoly.Nonce](chachapoly/sealedbox/nonce.md)
  The nonce used to encrypt the data.
- [var ciphertext: Data](chachapoly/sealedbox/ciphertext.md)
  The encrypted data.
- [var tag: Data](chachapoly/sealedbox/tag.md)
  An authentication tag.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/chachapoly/sealedbox)*