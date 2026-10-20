# session(_:didReceive:fromPeer:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates that an `NSData` object has been received from a nearby peer.

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
func session(_ session: MCSession, didReceive data: Data, fromPeer peerID: MCPeerID)
```

```objc
- (void) session:(MCSession *) session didReceiveData:(NSData *) data fromPeer:(MCPeerID *) peerID;
```

## Parameters

- `session`: The session through which the data was received.
- `data`: An object containing the received data.
- `peerID`: The peer ID of the sender.

## See Also

### MCSession Delegate Methods
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](./session%28_,didstartreceivingresourcewithname,frompeer,with%29.md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](./session%28_,didfinishreceivingresourcewithname,frompeer,at,witherror%29.md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](./session%28_,didreceive,withname,frompeer%29.md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](./session%28_,peer,didchange%29.md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](./session%28_,didreceivecertificate,frompeer,certificatehandler%29.md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didreceive:frompeer:))*