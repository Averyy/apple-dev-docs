# finalize()

**Framework**: Apple CryptoKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Finalizes the hash function and returns the computed digest.

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
func finalize() -> Self.Digest
```

## Return Value

The computed digest of the data.

## Discussion

Call this method after you provide the hash function with all the data to hash using one or more calls to the [`update(data:)`](./update%28data%29.md) or [`update(bufferPointer:)`](./update%28bufferpointer%29.md) method. After finalizing the hash function, discard it. To compute a new digest, create a new hash function with a call to the [`init()`](./init%28%29.md) method.

## See Also

### Computing a hash iteratively
- [init()](./init%28%29.md)
  Creates a hash function.
- [func update<D>(data: D)](./update%28data%29.md)
  Incrementally updates the hash function with the given data.
- [func update(bufferPointer: UnsafeRawBufferPointer)](./update%28bufferpointer%29.md)
  Incrementally updates the hash function with the contents of the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hashfunction/finalize())*