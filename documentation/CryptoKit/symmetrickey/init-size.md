# init(size:)

**Framework**: Apple CryptoKit  
**Kind**: init

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

- `size`: The size of the key to generate. You can use one of the standard   sizes, like  , or you can create a key of   custom length by initializing a   instance with a   non-standard value.

## See Also

- [init<D>(data: D)](symmetrickey/init(data:).md)
  Creates a key from the given data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/symmetrickey/init(size:))*