# CFFileDescriptorCreate(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Creates a new CFFileDescriptor.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFFileDescriptorCreate(_ allocator: CFAllocator!, _ fd: CFFileDescriptorNativeDescriptor, _ closeOnInvalidate: Bool, _ callout: CFFileDescriptorCallBack!, _ context: UnsafePointer<CFFileDescriptorContext>!) -> CFFileDescriptor!
```

#### Return Value

A new CFFileDescriptor or `NULL` if there was a problem creating the object. Ownership follows the [`The Create Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new file descriptor object. Pass   or kCFAllocatorDefault to use the current default allocator.
- `fd`: The file descriptor for the new CFFileDescriptor.
- `closeOnInvalidate`:   if the new CFFileDescriptor should close   when it is invalidated, otherwise  .
- `callout`: The CFFileDescriptorCallBack for the new CFFileDescriptor.
- `context`: Contextual information for the new CFFileDescriptor.

## See Also

- [func CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>!)](cffiledescriptorgetcontext(_:_:).md)
  Gets the context for a given CFFileDescriptor.
- [func CFFileDescriptorInvalidate(CFFileDescriptor!)](cffiledescriptorinvalidate(_:).md)
  Invalidates a CFFileDescriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcreate(_:_:_:_:_:))*