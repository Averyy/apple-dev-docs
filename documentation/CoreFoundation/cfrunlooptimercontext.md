# CFRunLoopTimerContext

**Framework**: Core Foundation  
**Kind**: struct

A structure that contains program-defined data and callbacks with which you can configure a CFRunLoopTimer’s behavior.

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
struct CFRunLoopTimerContext
```

## Topics

### Initializers
- [init()](cfrunlooptimercontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!)](cfrunlooptimercontext/init(version:info:retain:release:copydescription:).md)
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfrunlooptimercontext/copydescription.md)
  A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [var info: UnsafeMutableRawPointer!](cfrunlooptimercontext/info.md)
  An arbitrary pointer to program-defined data, which can be associated with the run loop timer at creation time. This pointer is passed to all the callbacks defined in the context.
- [var release: ((UnsafeRawPointer?) -> Void)!](cfrunlooptimercontext/release.md)
  A release callback for your program-defined `info` pointer. Can be `NULL`.
- [var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfrunlooptimercontext/retain.md)
  A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [var version: CFIndex](cfrunlooptimercontext/version.md)
  Version number of the structure. Must be 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunlooptimercontext)*