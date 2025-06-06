# init(data:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a key from the given data.

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
init<D>(data: D) where D : ContiguousBytes
```

## Parameters

- `data`: The contiguous bytes from which to create the key.

## See Also

- [init(size: SymmetricKeySize)](symmetrickey/init(size:).md)
  Generates a new random key of the given size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/symmetrickey/init(data:))*