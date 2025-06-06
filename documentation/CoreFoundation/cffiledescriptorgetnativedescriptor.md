# CFFileDescriptorGetNativeDescriptor(_:)

**Framework**: Core Foundation  
**Kind**: func

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

#### Return Value

The native file descriptor for `f`.

## Parameters

- `f`: A CFFileDescriptor.

## See Also

- [func CFFileDescriptorInvalidate(CFFileDescriptor!)](cffiledescriptorinvalidate(_:).md)
  Invalidates a CFFileDescriptor object.
- [func CFFileDescriptorIsValid(CFFileDescriptor!) -> Bool](cffiledescriptorisvalid(_:).md)
  Returns a Boolean value that indicates whether the native file descriptor for a given CFFileDescriptor is valid.
- [func CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>!)](cffiledescriptorgetcontext(_:_:).md)
  Gets the context for a given CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorgetnativedescriptor(_:))*