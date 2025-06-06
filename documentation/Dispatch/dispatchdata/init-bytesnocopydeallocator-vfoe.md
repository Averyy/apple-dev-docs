# init(bytesNoCopy:deallocator:)

**Framework**: Dispatch  
**Kind**: init

Creates a new dispatch data object using the specified memory buffer and deallocator.

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
init(bytesNoCopy bytes: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator = .free)
```

## Parameters

- `bytes`: A contiguous buffer of memory containing the initial data.
- `deallocator`: The deallocator responsible for releasing the memory associated with the data object. For a list of possible options, see  .

## See Also

- [init(bytes: UnsafeRawBufferPointer)](dispatchdata/init(bytes:)-9lrd.md)
  Creates a new dispatch data object from the specified memory buffer.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](dispatchdata/withunsafebytes(body:).md)
- [DispatchData.Deallocator](dispatchdata/deallocator.md)
  Memory deallocators for dispatch data objects.
- [static let empty: DispatchData](dispatchdata/empty.md)
  A dispatch data object representing a zero-length memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytesnocopy:deallocator:)-vfoe)*