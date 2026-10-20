# CFFileDescriptorGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Gets the context for a given CFFileDescriptor.

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
func CFFileDescriptorGetContext(_ f: CFFileDescriptor!, _ context: UnsafeMutablePointer<CFFileDescriptorContext>!)
```

```c
extern void CFFileDescriptorGetContext(CFFileDescriptorRef f, CFFileDescriptorContext *context);
```

## Parameters

- `f`: A CFFileDescriptor.
- `context`: Upon return, contains the context passed to `f` in [`CFFileDescriptorCreate(_:_:_:_:_:)`](./cffiledescriptorcreate%28_,_,_,_,_%29.md).

## See Also

### Related Documentation
- [func CFFileDescriptorCreate(CFAllocator!, CFFileDescriptorNativeDescriptor, Bool, CFFileDescriptorCallBack!, UnsafePointer<CFFileDescriptorContext>!) -> CFFileDescriptor!](./cffiledescriptorcreate%28_,_,_,_,_%29.md)
  Creates a new CFFileDescriptor.
### Getting Information About a File Descriptor
- [func CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor](./cffiledescriptorgetnativedescriptor%28_%29.md)
  Returns the native file descriptor for a given CFFileDescriptor.
- [func CFFileDescriptorIsValid(CFFileDescriptor!) -> Bool](./cffiledescriptorisvalid%28_%29.md)
  Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorgetcontext(_:_:))*