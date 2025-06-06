# synchronousRemoteObjectProxyWithErrorHandler(_:)

**Framework**: Foundation  
**Kind**: method

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

## See Also

- [func remoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](nsxpcconnection/remoteobjectproxywitherrorhandler(_:).md)
  Returns a proxy for the remote object (that is, the object exported from the other side of this connection) with the specified error handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/synchronousremoteobjectproxywitherrorhandler(_:))*