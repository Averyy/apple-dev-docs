# init(rawRepresentation:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a Curve25519 private key for key agreement from a collection of bytes.

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

- `rawRepresentation`: A raw representation of the key as a   collection of contiguous bytes.

## See Also

- [init()](curve25519/keyagreement/privatekey/init.md)
  Creates a random Curve25519 private key for key agreement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/curve25519/keyagreement/privatekey/init(rawrepresentation:))*