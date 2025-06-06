# CFSocketContext

**Framework**: Core Foundation  
**Kind**: struct

A structure that contains program-defined data and callbacks with which you can configure a CFSocket object’s behavior.

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
struct CFSocketContext
```

## Topics

### Initializers
- [init()](cfsocketcontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](cfsocketcontext/init(version:info:retain:release:copydescription:).md)
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfsocketcontext/copydescription.md)
  A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [var info: UnsafeMutableRawPointer!](cfsocketcontext/info.md)
  An arbitrary pointer to program-defined data, which can be associated with the CFSocket object at creation time. This pointer is passed to all the callbacks defined in the context.
- [var release: ((UnsafeRawPointer?) -> Void)!](cfsocketcontext/release.md)
  A release callback for your program-defined `info` pointer. Can be `NULL`.
- [var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfsocketcontext/retain.md)
  A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [var version: CFIndex](cfsocketcontext/version.md)
  Version number of the structure. Must be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [typealias CFSocketNativeHandle](cfsocketnativehandle.md)
  Type for the platform-specific native socket handle.
- [struct CFSocketSignature](cfsocketsignature.md)
  A structure that fully specifies the communication protocol and connection address of a CFSocket object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfsocketcontext)*