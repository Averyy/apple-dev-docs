# replaceSubrange(_:with:)

**Framework**: Foundation  
**Kind**: method

Replaces a region of bytes in the data with new bytes from a collection.

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
mutating func replaceSubrange<ByteCollection>(_ subrange: Range<Data.Index>, with newElements: ByteCollection) where ByteCollection : Collection, ByteCollection.Element == UInt8
```

#### Discussion

This will resize the data if required, to fit the entire contents of `newElements`.

Precondition: The bounds of `subrange` must be valid indices of the collection.

## Parameters

- `subrange`: The range in the data to replace.
- `newElements`: The replacement bytes.

## See Also

- [func replaceSubrange(Range<Data.Index>, with: Data)](data/replacesubrange(_:with:)-3jcfi.md)
  Replaces a region of bytes in the data with new data.
- [func replaceSubrange<SourceType>(Range<Data.Index>, with: UnsafeBufferPointer<SourceType>)](data/replacesubrange(_:with:)-9nzh.md)
  Replaces a region of bytes in the data with new bytes from a buffer.
- [func replaceSubrange(Range<Data.Index>, with: UnsafeRawPointer, count: Int)](data/replacesubrange(_:with:count:).md)
  Replaces a region of bytes in the data with bytes from memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/replacesubrange(_:with:)-9u7ry)*