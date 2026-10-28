# init()

**Framework**: Apple CryptoKit  
**Kind**: init  
**Role**: Initializer

Creates a SHA1 hash function.

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
init()
```

## Discussion

Initialize a new hash function by calling this method if you want to hash the data iteratively, such as when you don’t have a buffer large enough to hold all the data at once. Provide data blocks to the hash function using the `update(data:)` or [`update(bufferPointer:)`](./update%28bufferpointer%29.md) method. After providing all the data, call [`finalize()`](./finalize%28%29.md) to get the digest.

If your data fits into a single buffer, you can use the `hash(data:)` method instead, to compute the digest in a single call.

## See Also

### Computing a hash iteratively
- [func update(bufferPointer: UnsafeRawBufferPointer)](./update%28bufferpointer%29.md)
  Incrementally updates the hash function with the contents of the buffer.
- [func finalize() -> Insecure.SHA1.Digest](./finalize%28%29.md)
  Finalizes the hash function and returns the computed digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/insecure/sha1/init())*