# remoteObjectProxyWithErrorHandler(_:)

**Framework**: Foundation  
**Kind**: method

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

#### Discussion

See descriptions in [`NSXPCProxyCreating`](nsxpcproxycreating.md) for more details.

## See Also

- [func synchronousRemoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](nsxpcconnection/synchronousremoteobjectproxywitherrorhandler(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/remoteobjectproxywitherrorhandler(_:))*