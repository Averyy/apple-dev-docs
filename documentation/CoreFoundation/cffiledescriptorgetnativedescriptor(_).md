# CFFileDescriptorGetNativeDescriptor(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns the native file descriptor for a given CFFileDescriptor.

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
func CFFileDescriptorGetNativeDescriptor(_ f: CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor
```

```c
extern CFFileDescriptorNativeDescriptor CFFileDescriptorGetNativeDescriptor(CFFileDescriptorRef f);
```

## Return Value

The native file descriptor for `f`.

## Parameters

- `f`: A CFFileDescriptor.

## See Also

### Related Documentation
- [func CFFileDescriptorInvalidate(CFFileDescriptor!)](./cffiledescriptorinvalidate%28_%29.md)
  Invalidates a CFFileDescriptor object.
### Getting Information About a File Descriptor
- [func CFFileDescriptorIsValid(CFFileDescriptor!) -> Bool](./cffiledescriptorisvalid%28_%29.md)
  Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.
- [func CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>!)](./cffiledescriptorgetcontext%28_,_%29.md)
  Gets the context for a given CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorgetnativedescriptor(_:))*