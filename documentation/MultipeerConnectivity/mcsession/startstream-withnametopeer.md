# startStream(withName:toPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Opens a byte stream to a nearby peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func startStream(withName streamName: String, toPeer peerID: MCPeerID) throws -> OutputStream
```

#### Return Value

In Swift, an output stream instance. In Objective-C, an output stream object upon success or `nil` if a stream could not be established.

#### Discussion

This method is nonblocking.

For more information about performing networking with input and output streams, read [`Networking Programming Topics`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Introduction/Introduction.html#//apple_ref/doc/uid/TP40012488).

## Parameters

- `streamName`: A name for the stream. This name is provided to the nearby peer.
- `peerID`: The ID of the nearby peer.

## See Also

- [func send(Data, toPeers: [MCPeerID], with: MCSessionSendDataMode) throws](mcsession/send(_:topeers:with:).md)
  Sends a message to nearby peers.
- [func sendResource(at: URL, withName: String, toPeer: MCPeerID, withCompletionHandler: (((any Error)?) -> Void)?) -> Progress?](mcsession/sendresource(at:withname:topeer:withcompletionhandler:).md)
  Sends the contents of a URL to a peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/startstream(withname:topeer:))*