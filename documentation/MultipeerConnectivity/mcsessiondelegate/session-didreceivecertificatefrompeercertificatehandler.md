# session(_:didReceiveCertificate:fromPeer:certificateHandler:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Called to validate the client certificate provided by a peer when the connection is first established.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func session(_ session: MCSession, didReceiveCertificate certificate: [Any]?, fromPeer peerID: MCPeerID, certificateHandler: @escaping (Bool) -> Void)
```

#### Discussion

Your app should inspect the nearby peer’s certificate, and then should decide whether to trust that certificate. Upon making that determination, your app should call the provided `certificateHandler` block, passing either [`true`](https://developer.apple.com/documentation/swift/true) (to trust the nearby peer) or [`false`](https://developer.apple.com/documentation/swift/false) (to reject it).

For information about validating certificates, read [`Cryptographic Services Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172).

> ❗ **Important**:  The multipeer connectivity framework makes no attempt to validate the peer-provided identity or certificates in any way. If your delegate does not implement this method, all certificates are accepted automatically.

## Parameters

- `session`: The session that the nearby peer wishes to join.
- `certificate`: If the nearby peer did not provide a security identity, then this parameter’s value is  .
- `peerID`: The peer ID of the sender.
- `certificateHandler`: Your app should call this handler with a value of   if the nearby peer should be allowed to join the session, or   otherwise.

## See Also

- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:frompeer:).md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:).md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:).md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:withname:frompeer:).md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](mcsessiondelegate/session(_:peer:didchange:).md)
  Called when the state of a nearby peer changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didreceivecertificate:frompeer:certificatehandler:))*