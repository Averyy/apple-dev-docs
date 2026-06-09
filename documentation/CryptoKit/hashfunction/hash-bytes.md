# hash(bytes:)

**Framework**: Apple CryptoKit  
**Kind**: method

Computes a digest of a span of bytes.

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
@export(implementation)
static func hash(bytes: RawSpan) -> Self.Digest
```

#### Return Value

The computed digest.

## Parameters

- `bytes`: The bytes to be hashed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction/hash(bytes:))*