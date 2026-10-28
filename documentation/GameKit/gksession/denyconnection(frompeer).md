# denyConnection(fromPeer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called by the delegate to reject a connection request received from a remote peer.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
func denyConnection(fromPeer peerID: String!)
```

```objc
- (void) denyConnectionFromPeer:(NSString *) peerID;
```

## Discussion

When your session acts as a server, client peers can discover your session and attempt to connect to it. When a client attempts to connect to the session, the delegate’s [`session(_:didReceiveConnectionRequestFromPeer:)`](../gksessiondelegate/session%28_,didreceiveconnectionrequestfrompeer%29.md) method is called to decide whether the peer should be connected. Your application calls this method to reject the request or [`acceptConnection(fromPeer:)`](./acceptconnection%28frompeer%29.md) to accept it.

## Parameters

- `peerID`: The string identifying the peer that initiated the connection to the session.

## See Also

### Receiving Connections from a Remote Peer
- [func acceptConnection(fromPeer: String!) throws](./acceptconnection%28frompeer%29.md)
  Called by the delegate to accept a connection request received from a remote peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/denyconnection(frompeer:))*