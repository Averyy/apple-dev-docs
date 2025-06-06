# CFStreamClientContext

**Framework**: Core Foundation  
**Kind**: struct

A structure that contains program-defined data and callbacks with which you can configure a stream’s client behavior.

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
struct CFStreamClientContext
```

## Topics

### Initializers
- [init()](cfstreamclientcontext/init.md)
- [init(version: CFIndex, info: UnsafeMutableRawPointer!, retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!, release: ((UnsafeMutableRawPointer?) -> Void)!, copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!)](cfstreamclientcontext/init(version:info:retain:release:copydescription:).md)
### Instance Properties
- [var copyDescription: ((UnsafeMutableRawPointer?) -> Unmanaged<CFString>?)!](cfstreamclientcontext/copydescription.md)
  A copy description callback for your program-defined `info` pointer. Can be `NULL`.
- [var info: UnsafeMutableRawPointer!](cfstreamclientcontext/info.md)
  An arbitrary pointer to program-defined data, which can be associated with the client. This pointer is passed to the callbacks defined in the context and to the client callback function [`CFReadStreamClientCallBack`](cfreadstreamclientcallback.md).
- [var release: ((UnsafeMutableRawPointer?) -> Void)!](cfstreamclientcontext/release.md)
  A release callback for your program-defined `info` pointer. Can be `NULL`.
- [var retain: ((UnsafeMutableRawPointer?) -> UnsafeMutableRawPointer?)!](cfstreamclientcontext/retain.md)
  A retain callback for your program-defined `info` pointer. Can be `NULL`.
- [var version: CFIndex](cfstreamclientcontext/version.md)
  Version number of the structure. Must be `0`.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfstreamclientcontext)*