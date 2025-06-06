# session(_:didStartReceivingResourceWithName:fromPeer:with:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Indicates that the local peer began receiving a resource from a nearby peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func session(_ session: MCSession, didStartReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, with progress: Progress)
```

## Parameters

- `session`: The session that started receiving the resource.
- `resourceName`: The name of the resource, as provided by the sender.
- `peerID`: The sender’s peer ID.
- `progress`: An   object that can be used to cancel the transfer or queried to determine how far the transfer has progressed.

## See Also

- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:frompeer:).md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:).md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:withname:frompeer:).md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](mcsessiondelegate/session(_:peer:didchange:).md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](mcsessiondelegate/session(_:didreceivecertificate:frompeer:certificatehandler:).md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:))*