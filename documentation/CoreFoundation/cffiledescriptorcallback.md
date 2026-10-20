# CFFileDescriptorCallBack

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Defines a structure for a callback for a CFFileDescriptor.

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
typealias CFFileDescriptorCallBack = (CFFileDescriptor?, CFOptionFlags, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(struct __CFFileDescriptor *, unsigned long, void *) CFFileDescriptorCallBack;
```

## See Also

### Data Types
- [typealias CFFileDescriptorNativeDescriptor](./cffiledescriptornativedescriptor.md)
  Defines a type for the native file descriptor.
- [struct CFFileDescriptorContext](./cffiledescriptorcontext.md)
  Defines a structure for the context of a CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcallback)*