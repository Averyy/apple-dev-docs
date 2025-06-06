# replaceSubrange(_:with:count:)

**Framework**: Foundation  
**Kind**: method

Replaces a region of bytes in the data with bytes from memory.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
mutating func replaceSubrange(_ subrange: Range<Data.Index>, with bytes: UnsafeRawPointer, count cnt: Int)
```

## See Also

- [func replaceSubrange(Range<Data.Index>, with: Data)](data/replacesubrange(_:with:)-3jcfi.md)
  Replaces a region of bytes in the data with new data.
- [func replaceSubrange<ByteCollection>(Range<Data.Index>, with: ByteCollection)](data/replacesubrange(_:with:)-9u7ry.md)
  Replaces a region of bytes in the data with new bytes from a collection.
- [func replaceSubrange<SourceType>(Range<Data.Index>, with: UnsafeBufferPointer<SourceType>)](data/replacesubrange(_:with:)-9nzh.md)
  Replaces a region of bytes in the data with new bytes from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/replacesubrange(_:with:count:))*