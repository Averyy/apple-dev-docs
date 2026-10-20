# init(bytes:)

**Framework**: Dispatch  
**Kind**: init  
**Role**: Initializer

Creates a new dispatch data object from the specified memory buffer.

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
init(bytes buffer: UnsafeRawBufferPointer)
```

## Parameters

- `buffer`: A contiguous buffer of memory containing the initial data.

## See Also

### Creating a Dispatch Data Structure
- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](./init%28bytesnocopy,deallocator%29-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](./withunsafebytes%28body%29.md)
- [DispatchData.Deallocator](./deallocator.md)
  Memory deallocators for dispatch data objects.
- [static let empty: DispatchData](./empty.md)
  A dispatch data object representing a zero-length memory region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/init(bytes:)-9lrd)*