# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a Curve25519 public key from a data representation.

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
init<D>(rawRepresentation: D) throws where D : ContiguousBytes
```

## Parameters

- `rawRepresentation`: A representation of the key as contiguous   bytes from which to create the key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/signing/publickey/init(rawrepresentation:))*