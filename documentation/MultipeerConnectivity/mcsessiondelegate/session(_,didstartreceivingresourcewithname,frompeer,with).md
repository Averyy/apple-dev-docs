# session(_:didStartReceivingResourceWithName:fromPeer:with:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates that the local peer began receiving a resource from a nearby peer.

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
func session(_ session: MCSession, didStartReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, with progress: Progress)
```

```objc
- (void) session:(MCSession *) session didStartReceivingResourceWithName:(NSString *) resourceName fromPeer:(MCPeerID *) peerID withProgress:(NSProgress *) progress;
```

## Parameters

- `session`: The session that started receiving the resource.
- `resourceName`: The name of the resource, as provided by the sender.
- `peerID`: The sender’s peer ID.
- `progress`: An `NSProgress` object that can be used to cancel the transfer or queried to determine how far the transfer has progressed.

## See Also

### MCSession Delegate Methods
- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](./session%28_,didreceive,frompeer%29.md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](./session%28_,didfinishreceivingresourcewithname,frompeer,at,witherror%29.md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](./session%28_,didreceive,withname,frompeer%29.md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](./session%28_,peer,didchange%29.md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](./session%28_,didreceivecertificate,frompeer,certificatehandler%29.md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:))*