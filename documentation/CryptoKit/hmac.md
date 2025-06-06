# HMAC

**Framework**: Apple CryptoKit  
**Kind**: struct

A hash-based message authentication algorithm.

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
struct HMAC<H> where H : HashFunction
```

#### Overview

Use hash-based message authentication to create a code with a value that’s dependent on both a block of data and a symmetric cryptographic key. Another party with access to the data and the same secret key can compute the code again and compare it to the original to detect whether the data changed. This serves a purpose similar to digital signing and verification, but depends on a shared symmetric key instead of public-key cryptography.

As with digital signing, the data isn’t hidden by this process. When you need to encrypt the data as well as authenticate it, use a cipher like [`AES`](aes.md) or [`ChaChaPoly`](chachapoly.md) to put the data into a sealed box (an instance of [`AES.GCM.SealedBox`](aes/gcm/sealedbox.md) or [`ChaChaPoly.SealedBox`](chachapoly/sealedbox.md)).

## Topics

### Getting a key
- [typealias Key](hmac/key.md)
  An alias for the symmetric key type used to compute or verify a message authentication code.
- [struct SymmetricKey](symmetrickey.md)
  A symmetric cryptographic key.
### Working with codes
- [typealias MAC](hmac/mac.md)
  An alias for a hash-based message authentication code.
- [struct HashedAuthenticationCode](hashedauthenticationcode.md)
  A hash-based message authentication code.
- [protocol MessageAuthenticationCode](messageauthenticationcode.md)
  A type that represents a message authentication code.
### Creating an authentication code with one call
- [static func authenticationCode<D>(for: D, using: SymmetricKey) -> HMAC<H>.MAC](hmac/authenticationcode(for:using:).md)
  Computes a message authentication code for the given data.
### Creating an authentication code iteratively
- [init(key: SymmetricKey)](hmac/init(key:).md)
  Creates a message authentication code generator.
- [func update<D>(data: D)](hmac/update(data:).md)
  Updates the message authentication code computation with a block of data.
- [func finalize() -> HMAC<H>.MAC](hmac/finalize.md)
  Finalizes the message authentication computation and returns the computed code.
### Checking an authentication code
- [static func isValidAuthenticationCode<D>(HMAC<H>.MAC, authenticating: D, using: SymmetricKey) -> Bool](hmac/isvalidauthenticationcode(_:authenticating:using:)-8ezmw.md)
  Returns a Boolean value indicating whether the given message authentication code is valid for a block of data.
- [static func isValidAuthenticationCode(HMAC<H>.MAC, authenticating: UnsafeRawBufferPointer, using: SymmetricKey) -> Bool](hmac/isvalidauthenticationcode(_:authenticating:using:)-5jbc8.md)
  Returns a Boolean value indicating whether the given message authentication code is valid for a block of data stored in a buffer.
- [static func isValidAuthenticationCode<C, D>(C, authenticating: D, using: SymmetricKey) -> Bool](hmac/isvalidauthenticationcode(_:authenticating:using:)-5ilt9.md)
  Returns a Boolean value indicating whether the given message authentication code represented as contiguous bytes is valid for a block of data.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SymmetricKey](symmetrickey.md)
  A symmetric cryptographic key.
- [struct SymmetricKeySize](symmetrickeysize.md)
  The sizes that a symmetric cryptographic key can take.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hmac)*