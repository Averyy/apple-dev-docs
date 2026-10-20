# CFFileDescriptorIsValid(_:)

**Framework**: Core Foundation  
**Kind**: func

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

#### Return Value

`true` if the native file descriptor for `f` is valid, otherwise `false`.

## Parameters

- `f`: A CFFileDescriptor.

## See Also

- [func CFFileDescriptorInvalidate(CFFileDescriptor!)](cffiledescriptorinvalidate(_:).md)
  Invalidates a CFFileDescriptor object.
- [func CFFileDescriptorGetNativeDescriptor(CFFileDescriptor!) -> CFFileDescriptorNativeDescriptor](cffiledescriptorgetnativedescriptor(_:).md)
  Returns the native file descriptor for a given CFFileDescriptor.
- [func CFFileDescriptorGetContext(CFFileDescriptor!, UnsafeMutablePointer<CFFileDescriptorContext>!)](cffiledescriptorgetcontext(_:_:).md)
  Gets the context for a given CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorisvalid(_:))*