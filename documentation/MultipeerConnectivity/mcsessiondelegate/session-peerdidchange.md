# session(_:peer:didChange:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Called when the state of a nearby peer changes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func session(_ session: MCSession, peer peerID: MCPeerID, didChange state: MCSessionState)
```

#### Discussion

This delegate method is called with the following state values when the nearby peer’s state changes:

- [`MCSessionState.connected`](mcsessionstate/connected.md)—the nearby peer accepted the invitation and is now connected to the session.
- [`MCSessionState.notConnected`](mcsessionstate/notconnected.md)—the nearby peer declined the invitation, the connection could not be established, or a previously connected peer is no longer connected.

## Parameters

- `session`: The session that manages the nearby peer whose state changed.
- `peerID`: The ID of the nearby peer whose state changed.
- `state`: The new state of the nearby peer.

## See Also

- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:frompeer:).md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:).md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:).md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:withname:frompeer:).md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](mcsessiondelegate/session(_:didreceivecertificate:frompeer:certificatehandler:).md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:peer:didchange:))*