# AES.GCM.Nonce

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

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

## Overview

Don’t reuse the same nonce for multiple calls to encryption APIs. It’s critical that nonces are unique per call to encryption APIs in order to protect the integrity of the encryption.

## Topics

### Creating a nonce
- [init()](./nonce/init%28%29.md)
  Creates a new random nonce.
- [init<D>(data: D) throws](./nonce/init%28data%29.md)
  Creates a nonce from the given data.
### Iterating over a nonce’s bytes
- [func makeIterator() -> Array<UInt8>.Iterator](./nonce/makeiterator%28%29.md)
  Returns an iterator over the elements of the nonce.
### Initializers
- [init(copying: RawSpan) throws](./nonce/init%28copying%29.md)
  Creates a nonce from the given data.
### Instance Properties
- [var bytes: RawSpan](./nonce/bytes.md)
  The bytes stored in the nonce.
- [var count: Int](./nonce/count.md)
  The number of bytes stored in the nonce.

## Relationships

### Conforms To
- [ContiguousBytes](../../../Foundation/contiguousbytes.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)
- [Sequence](../../../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/nonce)*