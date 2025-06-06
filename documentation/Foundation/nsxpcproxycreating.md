# NSXPCProxyCreating

**Framework**: Foundation  
**Kind**: protocol

Methods for creating new proxy objects.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol NSXPCProxyCreating
```

#### Overview

[`NSXPCConnection`](nsxpcconnection.md) implements this protocol. All objects returned from the methods in this protocol also implement the protocol. This allows creation of new proxies from other proxies.

## Topics

### Instance Methods
- [func remoteObjectProxy() -> Any](nsxpcproxycreating/remoteobjectproxy.md)
  Returns a proxy object with no error handling block.
- [func remoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](nsxpcproxycreating/remoteobjectproxywitherrorhandler(_:).md)
  Returns a proxy object that invokes the error handling block if an error occurs on the connection.
- [func synchronousRemoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](nsxpcproxycreating/synchronousremoteobjectproxywitherrorhandler(_:).md)

## Relationships

### Conforming Types
- [NSXPCConnection](nsxpcconnection.md)

## See Also

- [class NSXPCConnection](nsxpcconnection.md)
  A bidirectional communication channel between two processes.
- [class NSXPCInterface](nsxpcinterface.md)
  An interface that may be sent to an exported object or remote object proxy.
- [class NSXPCCoder](nsxpccoder.md)
  A coder that encodes and decodes objects that your app sends over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcproxycreating)*