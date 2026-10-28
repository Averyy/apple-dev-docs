# synchronousRemoteObjectProxyWithErrorHandler(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a proxy that makes a synchronous IPC call instead of the default async behavior.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func synchronousRemoteObjectProxyWithErrorHandler(_ handler: @escaping (any Error) -> Void) -> Any
```

```objc
- (id) synchronousRemoteObjectProxyWithErrorHandler:(void (^)(NSError *error)) handler;
```

## Discussion

The error handler block and reply block will be invoked on the calling thread before the message to the proxy returns, instead of on the queue for the connection.

## See Also

### Working with proxy objects
- [func remoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](./remoteobjectproxywitherrorhandler%28_%29.md)
  Returns a proxy for the remote object (that is, the object exported from the other side of this connection) with the specified error handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/synchronousremoteobjectproxywitherrorhandler(_:))*