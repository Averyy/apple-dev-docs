# AES.GCM.Nonce

**Framework**: Apple CryptoKit  
**Kind**: struct

A value used once during a cryptographic operation and then discarded.

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
struct Nonce
```

#### Overview

Don’t reuse the same nonce for multiple calls to encryption APIs. It’s critical that nonces are unique per call to encryption APIs in order to protect the integrity of the encryption.

## Topics

### Creating a nonce
- [init()](aes/gcm/nonce/init.md)
  Creates a new random nonce.
- [init<D>(data: D) throws](aes/gcm/nonce/init(data:).md)
  Creates a nonce from the given data.
### Iterating over a nonce’s bytes
- [func makeIterator() -> Array<UInt8>.Iterator](aes/gcm/nonce/makeiterator.md)
  Returns an iterator over the elements of the nonce.

## Relationships

### Conforms To
- [ContiguousBytes](../Foundation/ContiguousBytes.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/nonce)*