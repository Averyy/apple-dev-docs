# session(_:peer:didChange:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called when the state of a nearby peer changes.

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
func session(_ session: MCSession, peer peerID: MCPeerID, didChange state: MCSessionState)
```

```objc
- (void) session:(MCSession *) session peer:(MCPeerID *) peerID didChangeState:(MCSessionState) state;
```

## Discussion

This delegate method is called with the following state values when the nearby peer’s state changes:

- [`MCSessionState.connected`](../mcsessionstate/connected.md)—the nearby peer accepted the invitation and is now connected to the session.
- [`MCSessionState.notConnected`](../mcsessionstate/notconnected.md)—the nearby peer declined the invitation, the connection could not be established, or a previously connected peer is no longer connected.

## Parameters

- `session`: The session that manages the nearby peer whose state changed.
- `peerID`: The ID of the nearby peer whose state changed.
- `state`: The new state of the nearby peer.

## See Also

### MCSession Delegate Methods
- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](./session%28_,didreceive,frompeer%29.md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](./session%28_,didstartreceivingresourcewithname,frompeer,with%29.md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](./session%28_,didfinishreceivingresourcewithname,frompeer,at,witherror%29.md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](./session%28_,didreceive,withname,frompeer%29.md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](./session%28_,didreceivecertificate,frompeer,certificatehandler%29.md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:peer:didchange:))*