# init(data:)

**Framework**: Apple CryptoKit  
**Kind**: init

Creates a nonce from the given data.

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
init<D>(data: D) throws where D : DataProtocol
```

#### Discussion

Unless your use case calls for a nonce with a specific value, use the [`init()`](aes/gcm/nonce/init().md) method to instead create a random nonce.

## Parameters

- `data`: A data representation of the nonce.   The initializer throws an error if the data has a length smaller than 12 bytes.

## See Also

- [init()](aes/gcm/nonce/init.md)
  Creates a new random nonce.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/aes/gcm/nonce/init(data:))*