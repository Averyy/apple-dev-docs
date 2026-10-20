# Data.Deallocator

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

A deallocator you use to customize how the backing store is deallocated for data created with the no-copy initializer.

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
enum Deallocator
```

## Topics

### Enumeration Cases
- [case custom((UnsafeMutableRawPointer, Int) -> Void)](./deallocator/custom%28_%29.md)
  A custom deallocator.
- [Data.Deallocator.free](./deallocator/free.md)
  Use `free`.
- [Data.Deallocator.none](./deallocator/none.md)
  Do nothing upon deallocation.
- [Data.Deallocator.unmap](./deallocator/unmap.md)
  Use `munmap`.
- [Data.Deallocator.virtualMemory](./deallocator/virtualmemory.md)

## See Also

### Creating Data from Raw Memory
- [init(bytes: UnsafeRawPointer, count: Int)](./init%28bytes,count%29.md)
  Creates data with copied memory content.
- [init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)](./init%28buffer%29-75sng.md)
  Creates a data buffer with copied memory content using a buffer pointer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](./init%28buffer%29-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](./init%28bytesnocopy,count,deallocator%29.md)
  Creates a data buffer with memory content without copying the bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/deallocator)*