# hash(into:)

**Framework**: Apple CryptoKit  
**Kind**: method

Hashes the essential components of the digest by feeding them into the given hash function.

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
func hash(into hasher: inout Hasher)
```

#### Discussion

This method is part of the digest’s conformance to Swift standard library’s [`Hashable`](https://developer.apple.com/documentation/Swift/Hashable) protocol, making it possible to compare digests. Don’t confuse that hashing with the cryptographically secure hashing that you use to create the digest in the first place by, for example, calling `SHA512/hash(data:)`.

## Parameters

- `hasher`: The hash function to use when combining the components of   the digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha512digest/hash(into:))*