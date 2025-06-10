# withUnsafeBytes(_:)

**Framework**: Foundation  
**Kind**: method

Accesses the raw bytes in the data’s buffer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Swift ?+

## Declaration

```swift
func withUnsafeBytes<ResultType, ContentType>(_ body: (UnsafePointer<ContentType>) throws -> ResultType) rethrows -> ResultType
```

#### Discussion

> ⚠️ **Warning**:  The byte pointer argument should not be stored and used outside of the lifetime of the call to the closure.

## See Also

- [func withUnsafeMutableBytes<ResultType, ContentType>((UnsafeMutablePointer<ContentType>) throws -> ResultType) rethrows -> ResultType](data/withunsafemutablebytes(_:)-7ac1g.md)
  Mutates the raw bytes in the data’s buffer.
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](data/copybytes(to:count:).md)
  Copies the contents of the data to memory.
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<Data.Index>)](data/copybytes(to:from:)-8qk4r.md)
  Copies a subset of the contents of the data to memory.
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<Data.Index>?) -> Int](data/copybytes(to:from:)-4o6zj.md)
  Copies the bytes in a range from the data into a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/withunsafebytes(_:))*