# update(data:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Instance Method

Incrementally updates the hash function with the given data.

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
mutating func update<D>(data: D) where D : DataProtocol
```

## Discussion

Call this method one or more times to provide data to the hash function in blocks. After providing the last block of data, call the [`finalize()`](./finalize%28%29.md) method to get the computed digest. Don’t call the update method again after finalizing the hash function.

## Parameters

- `data`: The next block of data for the ongoing digest calculation. You can provide this as any type that conforms to [`DataProtocol`](../../Foundation/dataprotocol.md), like [`Data`](../../Foundation/data.md) or an array of [`UInt8`](../../Swift/uint8.md) instances.

## See Also

### Computing a hash iteratively
- [init()](./init%28%29.md)
  Creates a hash function.
- [func update(bufferPointer: UnsafeRawBufferPointer)](./update%28bufferpointer%29.md)
  Incrementally updates the hash function with the contents of the buffer.
- [func finalize() -> Self.Digest](./finalize%28%29.md)
  Finalizes the hash function and returns the computed digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction/update(data:))*