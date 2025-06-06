# init(bitCount:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a new key size of the given length.

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
init(bitCount: Int)
```

#### Discussion

In most cases, you can use one of the standard key sizes, like bits256. If instead you need a key with a non-standard size, use the [`init(bitCount:)`](symmetrickeysize/init(bitcount:).md) initializer to create a custom key size.

## Parameters

- `bitCount`: The number of bits in the key size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/symmetrickeysize/init(bitcount:))*