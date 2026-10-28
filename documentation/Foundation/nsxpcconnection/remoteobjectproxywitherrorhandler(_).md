# remoteObjectProxyWithErrorHandler(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a proxy for the remote object (that is, the object exported from the other side of this connection) with the specified error handler.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func remoteObjectProxyWithErrorHandler(_ handler: @escaping (any Error) -> Void) -> Any
```

```objc
- (id) remoteObjectProxyWithErrorHandler:(void (^)(NSError *error)) handler;
```

## Discussion

See descriptions in [`NSXPCProxyCreating`](../nsxpcproxycreating.md) for more details.

## See Also

### Working with proxy objects
- [func synchronousRemoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](./synchronousremoteobjectproxywitherrorhandler%28_%29.md)
  Returns a proxy that makes a synchronous IPC call instead of the default async behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/remoteobjectproxywitherrorhandler(_:))*