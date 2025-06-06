# hash(data:)

**Framework**: Apple CryptoKit  
**Kind**: method

Computes the digest of the bytes in the given data instance and returns the computed digest.

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
static func hash<D>(data: D) -> Self.Digest where D : DataProtocol
```

#### Return Value

The computed digest of the data.

#### Discussion

Use this method if all your data fits into a single data instance. If the data you want to hash is too large, initialize a hash function and use the [`update(data:)`](hashfunction/update(data:).md) and [`finalize()`](hashfunction/finalize().md) methods to compute the digest in blocks.

## Parameters

- `data`: The data whose digest the hash function should compute. This can   be any type that conforms to   ,   like   or an   array of    instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction/hash(data:))*