# send(_:toPeers:with:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Sends a message to nearby peers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func send(_ data: Data, toPeers peerIDs: [MCPeerID], with mode: MCSessionSendDataMode) throws
```

#### Discussion

This method is asynchronous (nonblocking).

On the recipient device, the session instance calls its delegate instance’s [`session(_:didReceive:fromPeer:)`](mcsessiondelegate/session(_:didreceive:frompeer:).md) method with the message after it has been fully received.

## Parameters

- `data`: An instance containing the message to send.
- `peerIDs`: An array of peer ID instances representing the peers that should receive the message.
- `mode`: The transmission mode to use (reliable or unreliable delivery).

## See Also

- [func sendResource(at: URL, withName: String, toPeer: MCPeerID, withCompletionHandler: (((any Error)?) -> Void)?) -> Progress?](mcsession/sendresource(at:withname:topeer:withcompletionhandler:).md)
  Sends the contents of a URL to a peer.
- [func startStream(withName: String, toPeer: MCPeerID) throws -> OutputStream](mcsession/startstream(withname:topeer:).md)
  Opens a byte stream to a nearby peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/send(_:topeers:with:))*