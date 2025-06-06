# CFFileDescriptorGetContext(_:_:)

**Framework**: Core Foundation  
**Kind**: func

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

## Parameters

- `f`: A CFFileDescriptor.
- `context`: Upon return, contains the context passed to   in  .

## See Also

- [func CFFileDescriptorCreate(CFAllocator!, CFFileDescriptorNativeDescriptor, Bool, CFFileDescriptorCallBack!, UnsafePointer<CFFileDescriptorContext>!) -> CFFileDescriptor!](cffiledescriptorcreate(_:_:_:_:_:).md)
  Creates a new CFFileDescriptor.
- [func CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor](cffiledescriptorgetnativedescriptor(_:).md)
  Returns the native file descriptor for a given CFFileDescriptor.
- [func CFFileDescriptorIsValid(CFFileDescriptor!) -> Bool](cffiledescriptorisvalid(_:).md)
  Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorgetcontext(_:_:))*