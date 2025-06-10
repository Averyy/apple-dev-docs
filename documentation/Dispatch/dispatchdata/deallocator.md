# DispatchData.Deallocator

**Framework**: Dispatch  
**Kind**: enum

Memory deallocators for dispatch data objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum Deallocator
```

## Topics

### Deallocators
- [DispatchData.Deallocator.free](dispatchdata/deallocator/free.md)
  Use `free` to deallocate memory.
- [DispatchData.Deallocator.unmap](dispatchdata/deallocator/unmap.md)
  Use `munmap` to deallocate memory.
- [case custom(DispatchQueue?, () -> Void)](dispatchdata/deallocator/custom(_:_:).md)
  Use a custom deallocator.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(bytes: UnsafeRawBufferPointer)](dispatchdata/init(bytes:)-9lrd.md)
  Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](dispatchdata/init(bytesnocopy:deallocator:)-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](dispatchdata/withunsafebytes(body:).md)
- [static let empty: DispatchData](dispatchdata/empty.md)
  A dispatch data object representing a zero-length memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/deallocator)*