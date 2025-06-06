# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a Curve25519 private key for signing from a data representation.

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
init<D>(rawRepresentation data: D) throws where D : ContiguousBytes
```

## Parameters

- `data`: A representation of the key as contiguous bytes from   which to create the key.

## See Also

- [init()](curve25519/signing/privatekey/init.md)
  Creates a random Curve25519 private key for signing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/signing/privatekey/init(rawrepresentation:))*