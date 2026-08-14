# update(data:)

**Framework**: Apple CryptoKit  
**Kind**: method

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

#### Discussion

Call this method one or more times to provide data to the hash function in blocks. After providing the last block of data, call the [`finalize()`](hashfunction/finalize().md) method to get the computed digest. Don’t call the update method again after finalizing the hash function.

## Parameters

- `data`: The next block of data for the ongoing digest calculation. You can provide this as any type that conforms to [`DataProtocol`](https://developer.apple.com/documentation/foundation/dataprotocol), like [`Data`](https://developer.apple.com/documentation/foundation/data) or an array of [`UInt8`](https://developer.apple.com/documentation/swift/uint8) instances.

## See Also

- [init()](hashfunction/init.md)
  Creates a hash function.
- [func update(bufferPointer: UnsafeRawBufferPointer)](hashfunction/update(bufferpointer:).md)
  Incrementally updates the hash function with the contents of the buffer.
- [func finalize() -> Self.Digest](hashfunction/finalize.md)
  Finalizes the hash function and returns the computed digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction/update(data:))*