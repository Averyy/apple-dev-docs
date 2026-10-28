# startStream(withName:toPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Opens a byte stream to a nearby peer.

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
func startStream(withName streamName: String, toPeer peerID: MCPeerID) throws -> OutputStream
```

```objc
- (NSOutputStream *) startStreamWithName:(NSString *) streamName toPeer:(MCPeerID *) peerID error:(NSError **) error;
```

## Return Value

In Swift, an output stream instance. In Objective-C, an output stream object upon success or `nil` if a stream could not be established.

## Discussion

This method is nonblocking.

For more information about performing networking with input and output streams, read [Networking Programming Topics](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingTopics/Introduction/Introduction.html#//apple_ref/doc/uid/TP40012488).

## Parameters

- `streamName`: A name for the stream. This name is provided to the nearby peer.
- `peerID`: The ID of the nearby peer.

## See Also

### Sending Data and Resources
- [func send(Data, toPeers: [MCPeerID], with: MCSessionSendDataMode) throws](./send%28_,topeers,with%29.md)
  Sends a message to nearby peers.
- [func sendResource(at: URL, withName: String, toPeer: MCPeerID, withCompletionHandler: (((any Error)?) -> Void)?) -> Progress?](./sendresource%28at,withname,topeer,withcompletionhandler%29.md)
  Sends the contents of a URL to a peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/startstream(withname:topeer:))*