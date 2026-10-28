# CFFileDescriptorCreate(_:_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

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

```c
extern CFFileDescriptorRefCFFileDescriptorCreate(CFAllocatorRef allocator, CFFileDescriptorNativeDescriptor fd, Boolean closeOnInvalidate, CFFileDescriptorCallBack callout, const CFFileDescriptorContext *context);
```

## Return Value

A new CFFileDescriptor or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Parameters

- `allocator`: The allocator to use to allocate memory for the new file descriptor object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.
- `fd`: The file descriptor for the new CFFileDescriptor.
- `closeOnInvalidate`: `true` if the new CFFileDescriptor should close `fd` when it is invalidated, otherwise `false`.
- `callout`: The CFFileDescriptorCallBack for the new CFFileDescriptor.
- `context`: Contextual information for the new CFFileDescriptor.

## See Also

### Related Documentation
- [func CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>!)](./cffiledescriptorgetcontext%28_,_%29.md)
  Gets the context for a given CFFileDescriptor.
- [func CFFileDescriptorInvalidate(CFFileDescriptor!)](./cffiledescriptorinvalidate%28_%29.md)
  Invalidates a CFFileDescriptor object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcreate(_:_:_:_:_:))*