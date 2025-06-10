# copyBytes(to:from:)

**Framework**: Foundation  
**Kind**: method

Copies a subset of the contents of the data to memory.

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
func copyBytes(to pointer: UnsafeMutablePointer<UInt8>, from range: Range<Data.Index>)
```

#### Discussion

> ⚠️ **Warning**:  This method does not verify that the contents at pointer have enough space to hold the required number of bytes.

## Parameters

- `pointer`: A pointer to the buffer you wish to copy the bytes into.
- `range`: The range in the   to copy.

## See Also

- [func withUnsafeBytes<ResultType, ContentType>((UnsafePointer<ContentType>) throws -> ResultType) rethrows -> ResultType](data/withunsafebytes(_:).md)
  Accesses the raw bytes in the data’s buffer.
- [func withUnsafeMutableBytes<ResultType, ContentType>((UnsafeMutablePointer<ContentType>) throws -> ResultType) rethrows -> ResultType](data/withunsafemutablebytes(_:)-7ac1g.md)
  Mutates the raw bytes in the data’s buffer.
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](data/copybytes(to:count:).md)
  Copies the contents of the data to memory.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<Data.Index>?) -> Int](data/copybytes(to:from:)-4o6zj.md)
  Copies the bytes in a range from the data into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/copybytes(to:from:)-8qk4r)*