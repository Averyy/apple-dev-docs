# init(bytes:count:)

**Framework**: Foundation  
**Kind**: init

Creates data with copied memory content.

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
init(bytes: UnsafeRawPointer, count: Int)
```

## Parameters

- `bytes`: A pointer to the memory to copy.
- `count`: The number of bytes to copy.

## See Also

- [init()](data/init.md)
  Creates an empty data buffer.
- [init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)](data/init(buffer:)-75sng.md)
  Creates a data buffer with copied memory content using a buffer pointer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](data/init(buffer:)-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](data/init(bytesnocopy:count:deallocator:).md)
  Creates a data buffer with memory content without copying the bytes.
- [init(capacity: Int)](data/init(capacity:).md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](data/init(count:).md)
  Creates a new data buffer with the specified count of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(bytes:count:))*