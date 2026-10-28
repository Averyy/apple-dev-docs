# acceptConnection(fromPeer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called by the delegate to accept a connection request received from a remote peer.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
func acceptConnection(fromPeer peerID: String!) throws
```

```objc
- (BOOL) acceptConnectionFromPeer:(NSString *) peerID error:(NSError **) error;
```

## Discussion

When your session acts as a server, client peers can discover your session and attempt to connect to it. When a client attempts to connect to the session, the delegate’s [`session(_:didReceiveConnectionRequestFromPeer:)`](../gksessiondelegate/session%28_,didreceiveconnectionrequestfrompeer%29.md) method is called to decide whether the peer should be connected. Your application calls this method to accept the request, or [`denyConnection(fromPeer:)`](./denyconnection%28frompeer%29.md) to reject it.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `peerID`: The string identifying the peer that initiated the connection to the session.

## See Also

### Receiving Connections from a Remote Peer
- [func denyConnection(fromPeer: String!)](./denyconnection%28frompeer%29.md)
  Called by the delegate to reject a connection request received from a remote peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/acceptconnection(frompeer:))*