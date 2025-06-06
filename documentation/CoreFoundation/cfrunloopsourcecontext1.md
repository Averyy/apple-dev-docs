# CFRunLoopSourceContext1

**Framework**: Core Foundation  
**Kind**: struct

A structure that contains program-defined data and callbacks with which you can configure a version 1 CFRunLoopSource’s behavior.

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
struct CFRunLoopSourceContext1
```

## Topics

### Initializers
- [init()](cfrunloopsourcecontext1/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!, release: ((UnsafeRawPointer?) -> Void)!, copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!, equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!, hash: ((UnsafeRawPointer?) -> CFHashCode)!, getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!, perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!)](cfrunloopsourcecontext1/init(version:info:retain:release:copydescription:equal:hash:getport:perform:).md)
### Instance Properties
- [var copyDescription: ((UnsafeRawPointer?) -> Unmanaged<CFString>?)!](cfrunloopsourcecontext1/copydescription.md)
  A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [var equal: ((UnsafeRawPointer?, UnsafeRawPointer?) -> DarwinBoolean)!](cfrunloopsourcecontext1/equal.md)
  An equality test callback for your program-defined `info` pointer. Can be `NULL`.
- [var getPort: ((UnsafeMutableRawPointer?) -> mach_port_t)!](cfrunloopsourcecontext1/getport.md)
  A callback to retrieve the native Mach port represented by the source. This callback is called when the source is either added to or removed from a run loop mode.
- [var hash: ((UnsafeRawPointer?) -> CFHashCode)!](cfrunloopsourcecontext1/hash.md)
  A hash calculation callback for your program-defined `info` pointer. Can be `NULL`.
- [var info: UnsafeMutableRawPointer!](cfrunloopsourcecontext1/info.md)
  An arbitrary pointer to program-defined data, which can be associated with the run loop source at creation time. This pointer is passed to all the callbacks defined in the context.
- [var perform: ((UnsafeMutableRawPointer?, CFIndex, CFAllocator?, UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!](cfrunloopsourcecontext1/perform.md)
  A perform callback for the run loop source. This callback is called when the source has fired.
- [var release: ((UnsafeRawPointer?) -> Void)!](cfrunloopsourcecontext1/release.md)
  A release callback for your program-defined `info` pointer. Can be `NULL`.
- [var retain: ((UnsafeRawPointer?) -> UnsafeRawPointer?)!](cfrunloopsourcecontext1/retain.md)
  A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [var version: CFIndex](cfrunloopsourcecontext1/version.md)
  Version number of the structure. Must be 1.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct CFRunLoopSourceContext](cfrunloopsourcecontext.md)
  A structure that contains program-defined data and callbacks with which you can configure a version 0 CFRunLoopSource’s behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfrunloopsourcecontext1)*