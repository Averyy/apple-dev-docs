# DispatchData.Deallocator

**Framework**: Dispatch  
**Kind**: enum  
**Role**: Enumeration

Memory deallocators for dispatch data objects.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum Deallocator
```

## Topics

### Deallocators
- [DispatchData.Deallocator.free](./deallocator/free.md)
  Use `free` to deallocate memory.
- [DispatchData.Deallocator.unmap](./deallocator/unmap.md)
  Use `munmap` to deallocate memory.
- [case custom(DispatchQueue?, () -> Void)](./deallocator/custom%28_,_%29.md)
  Use a custom deallocator.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Dispatch Data Structure
- [init(bytes: UnsafeRawBufferPointer)](./init%28bytes%29-9lrd.md)
  Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](./init%28bytesnocopy,deallocator%29-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](./withunsafebytes%28body%29.md)
- [static let empty: DispatchData](./empty.md)
  A dispatch data object representing a zero-length memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/deallocator)*