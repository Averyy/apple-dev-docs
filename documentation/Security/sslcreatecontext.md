# SSLCreateContext(_:_:_:)

**Framework**: Security  
**Kind**: func

Allocates and returns a new context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+

## Declaration

```swift
func SSLCreateContext(_ alloc: CFAllocator?, _ protocolSide: SSLProtocolSide, _ connectionType: SSLConnectionType) -> SSLContext?
```

## Mentions

- [Using the Secure Socket Layer for Network Communication](using-the-secure-socket-layer-for-network-communication.md)

#### Return Value

A new context. In Objective-C, use [`CFRelease`](https://developer.apple.com/documentation/corefoundation/1521153-cfrelease) to release this object’s memory when you are done with it.

## Parameters

- `alloc`: The allocator to use. Pass   or   to use the default allocator.
- `protocolSide`: Either   or  .
- `connectionType`: Either   or  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcreatecontext(_:_:_:))*