# finalize()

**Framework**: Apple CryptoKit  
**Kind**: method

Finalizes the hash function and returns the computed digest.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 2.0+
- watchOS 26.0+ (Beta)

## Declaration

```swift
func finalize() -> SHA3_384.Digest
```

#### Return Value

The computed digest of the data.

#### Discussion

Call this method after you provide the hash function with all the data to hash by making one or more calls to the `update(data:)` or [`update(bufferPointer:)`](sha3_384/update(bufferpointer:).md) method. After finalizing the hash function, discard it. To compute a new digest, create a new hash function with a call to the [`init()`](sha3_384/init().md) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/sha3_384/finalize())*