# CFRunLoopSourceContext

**Framework**: Core Foundation  
**Kind**: struct

A structure that contains program-defined data and callbacks with which you can configure a version 0 CFRunLoopSource’s behavior.

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
struct CFRunLoopSourceContext
```

## Topics

### Initializers
- [init()](cfrunloopsourcecontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash: ((UnsafeRawPointer?) -> CFHashCode)!, schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!, cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!, perform: ((UnsafeMutableRawPointer?) -> Void)!)](cfrunloopsourcecontext/init(version:info:retain:release:copydescription:equal:hash:schedule:cancel:perform:).md)
### Instance Properties
- [var cancel: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](cfrunloopsourcecontext/cancel.md)
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfrunloopsourcecontext/copydescription.md)
  A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!](cfrunloopsourcecontext/equal.md)
  An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [var hash: ((UnsafeRawPointer?) -> CFHashCode)!](cfrunloopsourcecontext/hash.md)
  A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [var info: UnsafeMutableRawPointer!](cfrunloopsourcecontext/info.md)
  An arbitrary pointer to program-defined data, which can be associated with the CFRunLoopSource at creation time. This pointer is passed to all the callbacks defined in the context.
- [var perform: ((UnsafeMutableRawPointer?) -> Void)!](cfrunloopsourcecontext/perform.md)
  A perform callback for the run loop source. This callback is called when the source has fired.
- [var release: ((UnsafeRawPointer?) -> Void)!](cfrunloopsourcecontext/release.md)
  A release callback for your program-defined `info` pointer. Can be `NULL`.
- [var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfrunloopsourcecontext/retain.md)
  A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [var schedule: ((UnsafeMutableRawPointer?, CFRunLoop?, CFRunLoopMode?) -> Void)!](cfrunloopsourcecontext/schedule.md)
  A scheduling callback for the run loop source. This callback is called when the source is added to a run loop mode. Can be `NULL`.
- [var version: CFIndex](cfrunloopsourcecontext/version.md)
  Version number of the structure. Must be 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct CFRunLoopSourceContext1](cfrunloopsourcecontext1.md)
  A structure that contains program-defined data and callbacks with which you can configure a version 1 CFRunLoopSource’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext)*