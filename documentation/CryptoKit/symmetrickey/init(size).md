# init(size:)

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Generates a new random key of the given size.

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
init(size: SymmetricKeySize)
```

## Parameters

- `size`: The size of the key to generate. You can use one of the standard sizes, like [`bits256`](../symmetrickeysize/bits256.md), or you can create a key of custom length by initializing a [`SymmetricKeySize`](../symmetrickeysize.md) instance with a non-standard value.

## See Also

### Creating a key
- [init<D>(data: D)](./init%28data%29.md)
  Creates a key from the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/symmetrickey/init(size:))*