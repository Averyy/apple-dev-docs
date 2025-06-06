# init(buffer:)

**Framework**: Foundation  
**Kind**: init

Creates a data buffer with copied memory content using a buffer pointer.

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
init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)
```

## Parameters

- `buffer`: A buffer pointer to copy. The size is calculated from   and  .

## See Also

- [init()](data/init.md)
  Creates an empty data buffer.
- [init<S>(S)](data/init(_:).md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](data/init(buffer:)-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytes: UnsafeRawPointer, count: Int)](data/init(bytes:count:).md)
  Creates data with copied memory content.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](data/init(bytesnocopy:count:deallocator:).md)
  Creates a data buffer with memory content without copying the bytes.
- [init(capacity: Int)](data/init(capacity:).md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(buffer:)-75sng)*