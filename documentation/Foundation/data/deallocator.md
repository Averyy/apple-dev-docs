# Data.Deallocator

**Framework**: Foundation  
**Kind**: enum

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
- [case custom((UnsafeMutableRawPointer, Int) -> Void)](data/deallocator/custom(_:).md)
  A custom deallocator.
- [Data.Deallocator.free](data/deallocator/free.md)
  Use `free`.
- [Data.Deallocator.none](data/deallocator/none.md)
  Do nothing upon deallocation.
- [Data.Deallocator.unmap](data/deallocator/unmap.md)
  Use `munmap`.
- [Data.Deallocator.virtualMemory](data/deallocator/virtualmemory.md)

## See Also

- [init(bytes: UnsafeRawPointer, count: Int)](data/init(bytes:count:).md)
  Creates data with copied memory content.
- [init<SourceType>(buffer: UnsafeBufferPointer<SourceType>)](data/init(buffer:)-75sng.md)
  Creates a data buffer with copied memory content using a buffer pointer.
- [init<SourceType>(buffer: UnsafeMutableBufferPointer<SourceType>)](data/init(buffer:)-6xgv4.md)
  Creates a data buffer with copied memory content using a mutable buffer pointer.
- [init(bytesNoCopy: UnsafeMutableRawPointer, count: Int, deallocator: Data.Deallocator)](data/init(bytesnocopy:count:deallocator:).md)
  Creates a data buffer with memory content without copying the bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/data/deallocator)*