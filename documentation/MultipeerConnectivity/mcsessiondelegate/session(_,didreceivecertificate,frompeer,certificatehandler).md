# session(_:didReceiveCertificate:fromPeer:certificateHandler:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Called to validate the client certificate provided by a peer when the connection is first established.

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
optional func session(_ session: MCSession, didReceiveCertificate certificate: [Any]?, fromPeer peerID: MCPeerID, certificateHandler: @escaping (Bool) -> Void)
```

```objc
- (void) session:(MCSession *) session didReceiveCertificate:(NSArray *) certificate fromPeer:(MCPeerID *) peerID certificateHandler:(void (^)(BOOL accept)) certificateHandler;
```

#### Discussion

Your app should inspect the nearby peer’s certificate, and then should decide whether to trust that certificate. Upon making that determination, your app should call the provided `certificateHandler` block, passing either [`true`](../../Swift/true.md) (to trust the nearby peer) or [`false`](../../Swift/false.md) (to reject it).

For information about validating certificates, read [Cryptographic Services Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172).

> ❗ **Important**:  The multipeer connectivity framework makes no attempt to validate the peer-provided identity or certificates in any way. If your delegate does not implement this method, all certificates are accepted automatically.

## Parameters

- `session`: The session that the nearby peer wishes to join.
- `certificate`: A certificate chain, presented as an array of SecCertificateRef certificate objects. The first certificate in this chain is the peer’s certificate, which is derived from the identity that the peer provided when it called the [`init(peer:securityIdentity:encryptionPreference:)`](../mcsession/init%28peer,securityidentity,encryptionpreference%29.md) method. The other certificates are the (optional) additional chain certificates provided in that same array.

  If the nearby peer did not provide a security identity, then this parameter’s value is `nil`.
- `peerID`: The peer ID of the sender.
- `certificateHandler`: Your app should call this handler with a value of [`true`](../../Swift/true.md) if the nearby peer should be allowed to join the session, or [`false`](../../Swift/false.md) otherwise.

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
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](./session%28_,peer,didchange%29.md)
  Called when the state of a nearby peer changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didreceivecertificate:frompeer:certificatehandler:))*