# empty

**Framework**: Dispatch  
**Kind**: property

A dispatch data object representing a zero-length memory region.

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
static let empty: DispatchData
```

## See Also

- [init(bytes: UnsafeRawBufferPointer)](dispatchdata/init(bytes:)-9lrd.md)
  Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](dispatchdata/init(bytesnocopy:deallocator:)-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](dispatchdata/withunsafebytes(body:).md)
- [DispatchData.Deallocator](dispatchdata/deallocator.md)
  Memory deallocators for dispatch data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/empty)*