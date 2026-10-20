# CFFileDescriptorIsValid(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.

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
func CFFileDescriptorIsValid(_ f: CFFileDescriptor!) -> Bool
```

```c
extern Boolean CFFileDescriptorIsValid(CFFileDescriptorRef f);
```

#### Return Value

`true` if the native file descriptor for `f` is valid, otherwise `false`.

## Parameters

- `f`: A CFFileDescriptor.

## See Also

### Related Documentation
- [func CFFileDescriptorInvalidate(CFFileDescriptor!)](./cffiledescriptorinvalidate%28_%29.md)
  Invalidates a CFFileDescriptor object.
### Getting Information About a File Descriptor
- [func CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor](./cffiledescriptorgetnativedescriptor%28_%29.md)
  Returns the native file descriptor for a given CFFileDescriptor.
- [func CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>!)](./cffiledescriptorgetcontext%28_,_%29.md)
  Gets the context for a given CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorisvalid(_:))*