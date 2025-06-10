# acceptConnection(fromPeer:)

**Framework**: GameKit  
**Kind**: method

Called by the delegate to accept a connection request received from a remote peer.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func acceptConnection(fromPeer peerID: String!) throws
```

#### Discussion

When your session acts as a server, client peers can discover your session and attempt to connect to it. When a client attempts to connect to the session, the delegate’s [`session(_:didReceiveConnectionRequestFromPeer:)`](gksessiondelegate/session(_:didreceiveconnectionrequestfrompeer:).md) method is called to decide whether the peer should be connected. Your application calls this method to accept the request, or [`denyConnection(fromPeer:)`](gksession/denyconnection(frompeer:).md) to reject it.

> **Note**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `peerID`: The string identifying the peer that initiated the connection to the session.

## See Also

- [func denyConnection(fromPeer: String!)](gksession/denyconnection(frompeer:).md)
  Called by the delegate to reject a connection request received from a remote peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/acceptconnection(frompeer:))*