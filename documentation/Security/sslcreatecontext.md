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

A new context. In Objective-C, use [`CFRelease`](https://developer.apple.com/documentation/corefoundation/cfrelease) to release this object’s memory when you are done with it.

## Parameters

- `alloc`: The allocator to use. Pass `NULL` or [`kCFAllocatorDefault`](https://developer.apple.com/documentation/corefoundation/kcfallocatordefault) to use the default allocator.
- `protocolSide`: Either [`SSLProtocolSide.serverSide`](sslprotocolside/serverside.md) or [`SSLProtocolSide.clientSide`](sslprotocolside/clientside.md).
- `connectionType`: Either [`SSLConnectionType.streamType`](sslconnectiontype/streamtype.md) or [`SSLConnectionType.datagramType`](sslconnectiontype/datagramtype.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/sslcreatecontext(_:_:_:))*