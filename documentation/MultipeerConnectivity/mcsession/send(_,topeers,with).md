# send(_:toPeers:with:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Sends a message to nearby peers.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
func send(_ data: Data, toPeers peerIDs: [MCPeerID], with mode: MCSessionSendDataMode) throws
```

```objc
- (BOOL) sendData:(NSData *) data toPeers:(NSArray<MCPeerID *> *) peerIDs withMode:(MCSessionSendDataMode) mode error:(NSError **) error;
```

#### Discussion

This method is asynchronous (nonblocking).

On the recipient device, the session instance calls its delegate instance’s [`session(_:didReceive:fromPeer:)`](../mcsessiondelegate/session%28_,didreceive,frompeer%29.md) method with the message after it has been fully received.

## Parameters

- `data`: An instance containing the message to send.
- `peerIDs`: An array of peer ID instances representing the peers that should receive the message.
- `mode`: The transmission mode to use (reliable or unreliable delivery).

## See Also

### Sending Data and Resources
- [func sendResource(at: URL, withName: String, toPeer: MCPeerID, withCompletionHandler: (((any Error)?) -> Void)?) -> Progress?](./sendresource%28at,withname,topeer,withcompletionhandler%29.md)
  Sends the contents of a URL to a peer.
- [func startStream(withName: String, toPeer: MCPeerID) throws -> OutputStream](./startstream%28withname,topeer%29.md)
  Opens a byte stream to a nearby peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/send(_:topeers:with:))*