# init(bytes:)

**Framework**: Dispatch  
**Kind**: init

Creates a new dispatch data object from the specified memory buffer.

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
init(bytes buffer: UnsafeRawBufferPointer)
```

## Parameters

- `buffer`: A contiguous buffer of memory containing the initial data.

## See Also

- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](dispatchdata/init(bytesnocopy:deallocator:)-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](dispatchdata/withunsafebytes(body:).md)
- [DispatchData.Deallocator](dispatchdata/deallocator.md)
  Memory deallocators for dispatch data objects.
- [static let empty: DispatchData](dispatchdata/empty.md)
  A dispatch data object representing a zero-length memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytes:)-9lrd)*