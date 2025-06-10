# update(bufferPointer:)

**Framework**: Apple CryptoKit  
**Kind**: method  
**Required**: Yes

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

Call this method one or more times to provide data to the hash function in blocks. After providing the last block of data, call the [`finalize()`](hashfunction/finalize().md) method to get the computed digest. Don’t call the update method again after finalizing the hash function.

> **Note**: Typically, it’s safer to use an instance of [`Data`](https://developer.apple.com/documentation/Foundation/Data), or some other type that conforms to the [`DataProtocol`](https://developer.apple.com/documentation/Foundation/DataProtocol), to hold your data. When possible, use the [`update(data:)`](hashfunction/update(data:).md) method instead.

## Parameters

- `bufferPointer`: A pointer to the next block of data for the ongoing   digest calculation.

## See Also

- [init()](hashfunction/init.md)
  Creates a hash function.
- [func update<D>(data: D)](hashfunction/update(data:).md)
  Incrementally updates the hash function with the given data.
- [func finalize() -> Self.Digest](hashfunction/finalize.md)
  Finalizes the hash function and returns the computed digest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction/update(bufferpointer:))*