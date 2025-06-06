# session(_:didFinishReceivingResourceWithName:fromPeer:at:withError:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Required**: Yes

Indicates that the local peer finished receiving a resource from a nearby peer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func session(_ session: MCSession, didFinishReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, at localURL: URL?, withError error: (any Error)?)
```

#### Discussion

The file referenced by `resourceURL` is a temporary file. Your app must either read the file or make a copy in a permanent location before this delegate method returns.

## Parameters

- `session`: The session through which the data was received.
- `resourceName`: The name of the resource, as provided by the sender.
- `peerID`: The peer ID of the sender.
- `localURL`: An   object that provides the location of a temporary file containing the received data.
- `error`: An error object indicating what went wrong if the file was not received successfully, or  .

## See Also

- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:frompeer:).md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:).md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](mcsessiondelegate/session(_:didreceive:withname:frompeer:).md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](mcsessiondelegate/session(_:peer:didchange:).md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](mcsessiondelegate/session(_:didreceivecertificate:frompeer:certificatehandler:).md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:))*