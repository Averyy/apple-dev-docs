# SymmetricKey

**Framework**: Apple CryptoKit  
**Kind**: struct

A symmetric cryptographic key.

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
struct SymmetricKey
```

#### Overview

You typically derive a symmetric key from an instance of a shared secret ([`SharedSecret`](sharedsecret.md)) that you obtain through key agreement. You use a symmetric key to compute a message authentication code like [`HMAC`](hmac.md), or to open and close a sealed box ([`ChaChaPoly.SealedBox`](chachapoly/sealedbox.md) or [`AES.GCM.SealedBox`](aes/gcm/sealedbox.md)) using a cipher like [`ChaChaPoly`](chachapoly.md) or [`AES`](aes.md).

## Topics

### Creating a key
- [init<D>(data: D)](symmetrickey/init(data:).md)
  Creates a key from the given data.
- [init(size: SymmetricKeySize)](symmetrickey/init(size:).md)
  Generates a new random key of the given size.
### Getting the key length
- [var bitCount: Int](symmetrickey/bitcount.md)
  The number of bits in the key.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct HMAC](hmac.md)
  A hash-based message authentication algorithm.
- [struct SymmetricKeySize](symmetrickeysize.md)
  The sizes that a symmetric cryptographic key can take.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/symmetrickey)*