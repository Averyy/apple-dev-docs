# session(_:didReceive:withName:fromPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Called when a nearby peer opens a byte stream connection to the local peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func session(_ session: MCSession, didReceive stream: InputStream, withName streamName: String, fromPeer peerID: MCPeerID)
```

## Parameters

- `session`: The session through which the byte stream was opened.
- `stream`: An   object that represents the local endpoint for the byte stream.
- `streamName`: The name of the stream, as provided by the originator.
- `peerID`: The peer ID of the originator of the stream.

## See Also

- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:frompeer:).md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:).md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:).md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](mcsessiondelegate/session(_:peer:didchange:).md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](mcsessiondelegate/session(_:didreceivecertificate:frompeer:certificatehandler:).md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didreceive:withname:frompeer:))*