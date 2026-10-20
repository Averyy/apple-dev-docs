# session(_:didReceive:withName:fromPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when a nearby peer opens a byte stream connection to the local peer.

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
func session(_ session: MCSession, didReceive stream: InputStream, withName streamName: String, fromPeer peerID: MCPeerID)
```

```objc
- (void) session:(MCSession *) session didReceiveStream:(NSInputStream *) stream withName:(NSString *) streamName fromPeer:(MCPeerID *) peerID;
```

## Parameters

- `session`: The session through which the byte stream was opened.
- `stream`: An `NSInputStream` object that represents the local endpoint for the byte stream.
- `streamName`: The name of the stream, as provided by the originator.
- `peerID`: The peer ID of the originator of the stream.

## See Also

### MCSession Delegate Methods
- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](./session%28_,didreceive,frompeer%29.md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](./session%28_,didstartreceivingresourcewithname,frompeer,with%29.md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](./session%28_,didfinishreceivingresourcewithname,frompeer,at,witherror%29.md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](./session%28_,peer,didchange%29.md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](./session%28_,didreceivecertificate,frompeer,certificatehandler%29.md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didreceive:withname:frompeer:))*