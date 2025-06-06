# CFMessagePortContext

**Framework**: Core Foundation  
**Kind**: struct

A structure that contains program-defined data and callbacks with which you can configure a CFMessagePort object’s behavior.

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
struct CFMessagePortContext
```

## Topics

### Initializers
- [init()](cfmessageportcontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](cfmessageportcontext/init(version:info:retain:release:copydescription:).md)
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfmessageportcontext/copydescription.md)
  A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [var info: UnsafeMutableRawPointer!](cfmessageportcontext/info.md)
  An arbitrary pointer to program-defined data, which can be associated with the message port at creation time. This pointer is passed to all the callbacks defined in the context.
- [var release: ((UnsafeRawPointer?) -> Void)!](cfmessageportcontext/release.md)
  A release callback for your program-defined `info` pointer. Can be `NULL`.
- [var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfmessageportcontext/retain.md)
  A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [var version: CFIndex](cfmessageportcontext/version.md)
  Version number of the structure. Must be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfmessageportcontext)*