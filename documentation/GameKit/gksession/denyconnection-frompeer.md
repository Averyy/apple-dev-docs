# denyConnection(fromPeer:)

**Framework**: GameKit  
**Kind**: method

Called by the delegate to reject a connection request received from a remote peer.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func denyConnection(fromPeer peerID: String!)
```

#### Discussion

When your session acts as a server, client peers can discover your session and attempt to connect to it. When a client attempts to connect to the session, the delegate’s [`session(_:didReceiveConnectionRequestFromPeer:)`](gksessiondelegate/session(_:didreceiveconnectionrequestfrompeer:).md) method is called to decide whether the peer should be connected. Your application calls this method to reject the request or [`acceptConnection(fromPeer:)`](gksession/acceptconnection(frompeer:).md) to accept it.

## Parameters

- `peerID`: The string identifying the peer that initiated the connection to the session.

## See Also

- [func acceptConnection(fromPeer: String!) throws](gksession/acceptconnection(frompeer:).md)
  Called by the delegate to accept a connection request received from a remote peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/denyconnection(frompeer:))*