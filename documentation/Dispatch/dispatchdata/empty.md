# empty

**Framework**: Dispatch  
**Kind**: property  
**Role**: Type Property

A dispatch data object representing a zero-length memory region.

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
static let empty: DispatchData
```

## See Also

### Creating a Dispatch Data Structure
- [init(bytes: UnsafeRawBufferPointer)](./init%28bytes%29-9lrd.md)
  Creates a new dispatch data object from the specified memory buffer.
- [init(bytesNoCopy: UnsafeRawBufferPointer, deallocator: DispatchData.Deallocator)](./init%28bytesnocopy,deallocator%29-vfoe.md)
  Creates a new dispatch data object using the specified memory buffer and deallocator.
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](./withunsafebytes%28body%29.md)
- [DispatchData.Deallocator](./deallocator.md)
  Memory deallocators for dispatch data objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/empty)*