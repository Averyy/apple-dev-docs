# session(_:didFinishReceivingResourceWithName:fromPeer:at:withError:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Indicates that the local peer finished receiving a resource from a nearby peer.

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
func session(_ session: MCSession, didFinishReceivingResourceWithName resourceName: String, fromPeer peerID: MCPeerID, at localURL: URL?, withError error: (any Error)?)
```

```objc
- (void) session:(MCSession *) session didFinishReceivingResourceWithName:(NSString *) resourceName fromPeer:(MCPeerID *) peerID atURL:(NSURL *) localURL withError:(NSError *) error;
```

#### Discussion

The file referenced by `resourceURL` is a temporary file. Your app must either read the file or make a copy in a permanent location before this delegate method returns.

## Parameters

- `session`: The session through which the data was received.
- `resourceName`: The name of the resource, as provided by the sender.
- `peerID`: The peer ID of the sender.
- `localURL`: An `NSURL` object that provides the location of a temporary file containing the received data.
- `error`: An error object indicating what went wrong if the file was not received successfully, or `nil`.

## See Also

### MCSession Delegate Methods
- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](./session%28_,didreceive,frompeer%29.md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](./session%28_,didstartreceivingresourcewithname,frompeer,with%29.md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](./session%28_,didreceive,withname,frompeer%29.md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](./session%28_,peer,didchange%29.md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](./session%28_,didreceivecertificate,frompeer,certificatehandler%29.md)
  Called to validate the client certificate provided by a peer when the connection is first established.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:))*