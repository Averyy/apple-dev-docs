# copyBytes(to:from:)

**Framework**: Foundation  
**Kind**: method

Copies the bytes in a range from the data into a buffer.

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
func copyBytes<DestinationType>(to buffer: UnsafeMutableBufferPointer<DestinationType>, from range: Range<Data.Index>? = nil) -> Int
```

#### Return Value

Number of bytes copied into the destination buffer.

#### Discussion

If the count of the range is greater than `MemoryLayout<DestinationType>.stride * buffer.count` then only the first `N` bytes will be copied into the buffer.Precondition: The range must be within the bounds of the data. Otherwise `fatalError` is called.

## Parameters

- `buffer`: A buffer to copy the data into.
- `range`: A range in the data to copy into the buffer. If the range is empty, this function will return 0 without copying anything. If the range is nil, as much data as will fit into   is copied.

## See Also

- [func withUnsafeBytes<ResultType, ContentType>((UnsafePointer<ContentType>) throws -> ResultType) rethrows -> ResultType](data/withunsafebytes(_:).md)
  Accesses the raw bytes in the data’s buffer.
- [func withUnsafeMutableBytes<ResultType, ContentType>((UnsafeMutablePointer<ContentType>) throws -> ResultType) rethrows -> ResultType](data/withunsafemutablebytes(_:)-7ac1g.md)
  Mutates the raw bytes in the data’s buffer.
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](data/copybytes(to:count:).md)
  Copies the contents of the data to memory.
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<Data.Index>)](data/copybytes(to:from:)-8qk4r.md)
  Copies a subset of the contents of the data to memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/copybytes(to:from:)-4o6zj)*