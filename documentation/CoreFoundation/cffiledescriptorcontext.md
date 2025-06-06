# CFFileDescriptorContext

**Framework**: Core Foundation  
**Kind**: struct

Defines a structure for the context of a CFFileDescriptor.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFFileDescriptorContext
```

## Topics

### Initializers
- [init()](cffiledescriptorcontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release: ((UnsafeMutableRawPointer?) -> Void)!, copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!)](cffiledescriptorcontext/init(version:info:retain:release:copydescription:).md)
### Instance Properties
- [var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!](cffiledescriptorcontext/copydescription.md)
  The callback used to create a descriptive string representation of the CFFileDescriptor.
- [var info: UnsafeMutableRawPointer!](cffiledescriptorcontext/info.md)
- [var release: ((UnsafeMutableRawPointer?) -> Void)!](cffiledescriptorcontext/release.md)
  The release callback used by the CFFileDescriptor.
- [var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!](cffiledescriptorcontext/retain.md)
  The retain callback used by the CFFileDescriptor.
- [var version: CFIndex](cffiledescriptorcontext/version.md)
  The version number of this structure. If not one of the defined version numbers for this opaque type, the behavior is undefined. The current version of this structure is 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias CFFileDescriptorNativeDescriptor](cffiledescriptornativedescriptor.md)
  Defines a type for the native file descriptor.
- [typealias CFFileDescriptorCallBack](cffiledescriptorcallback.md)
  Defines a structure for a callback for a CFFileDescriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cffiledescriptorcontext)*