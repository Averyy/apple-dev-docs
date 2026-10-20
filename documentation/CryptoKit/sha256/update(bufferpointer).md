# update(bufferPointer:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Instance Method

Incrementally updates the hash function with the contents of the buffer.

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
mutating func update(bufferPointer: UnsafeRawBufferPointer)
```

#### Discussion

Call this method one or more times to provide data to the hash function in blocks. After providing the last block of data, call the [`finalize()`](./finalize%28%29.md) method to get the computed digest. Don’t call the update method again after finalizing the hash function.

> **Note**: Typically, it’s safer to use an instance of [`Data`](../../Foundation/data.md), or some other type that conforms to the [`DataProtocol`](../../Foundation/dataprotocol.md), to hold your data. When possible, use the `update(data:)` method instead.

## Parameters

- `bufferPointer`: A pointer to the next block of data for the ongoing digest calculation.

## See Also

### Computing a hash iteratively
- [init()](./init%28%29.md)
  Creates a SHA256 hash function.
- [func finalize() -> SHA256.Digest](./finalize%28%29.md)
  Finalizes the hash function and returns the computed digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha256/update(bufferpointer:))*