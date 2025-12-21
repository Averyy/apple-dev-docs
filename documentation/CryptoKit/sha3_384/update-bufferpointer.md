# update(bufferPointer:)

**Framework**: Apple CryptoKit  
**Kind**: method

Incrementally updates the hash function with the contents of the buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 2.0+
- watchOS 26.0+

## Declaration

```swift
mutating func update(bufferPointer: UnsafeRawBufferPointer)
```

#### Discussion

Call this method one or more times to provide data to the hash function in blocks. After providing the last block of data, call the [`finalize()`](sha3_384/finalize().md) method to get the computed digest. Don’t call the update method again after finalizing the hash function.

> **Note**: Typically, it’s safer to use an instance of [`Data`](https://developer.apple.com/documentation/Foundation/Data), or some other type that conforms to the [`DataProtocol`](https://developer.apple.com/documentation/Foundation/DataProtocol), to hold your data. When possible, use the `update(data:)` method instead.

## Parameters

- `bufferPointer`: A pointer to the next block of data for the ongoing   digest calculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha3_384/update(bufferpointer:))*