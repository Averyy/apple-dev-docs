# init(buffer:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

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

- `buffer`: A buffer pointer to copy. The size is calculated from `SourceType` and `buffer.count`.

## See Also

### Creating Populated Data
- [init()](./init%28%29.md)
  Creates an empty data buffer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](./init%28buffer%29-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytes: UnsafeRawPointer, count: Int)](./init%28bytes,count%29.md)
  Creates data with copied memory content.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](./init%28bytesnocopy,count,deallocator%29.md)
  Creates a data buffer with memory content without copying the bytes.
- [init(capacity: Int)](./init%28capacity%29.md)
  Creates an empty data buffer of a specified size.
- [init(count: Int)](./init%28count%29.md)
  Creates a new data buffer with the specified count of zeroed bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/init(buffer:)-75sng)*