# sendResource(at:withName:toPeer:withCompletionHandler:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Sends the contents of a URL to a peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func sendResource(at resourceURL: URL, withName resourceName: String, toPeer peerID: MCPeerID, withCompletionHandler completionHandler: (((any Error)?) -> Void)? = nil) -> Progress?
```

#### Return Value

An `NSProgress` object that can be used to query the status of the transfer or cancel the transfer.

#### Discussion

This method is asynchronous (nonblocking).

On the local device, the completion handler block is called when delivery succeeds or when an error occurs.

On the recipient device, the session calls its delegate’s [`session(_:didStartReceivingResourceWithName:fromPeer:with:)`](mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:).md) method as soon as it begins receiving the resource. This method provides an `NSProgress` object that your app can use to cancel the transfer or check its status.

Upon successful delivery, on the recipient device, the session calls its delegate’s [`session(_:didFinishReceivingResourceWithName:fromPeer:at:withError:)`](mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:).md) method. The received resource is written to a file in a temporary location with the same base name; the app is responsible for opening the file or moving it to a permanent location before that delegate method returns.

## Parameters

- `resourceURL`: A file or HTTP URL.
- `resourceName`: A name for the resource.
- `peerID`: The peer that should receive this resource.
- `completionHandler`: A block that gets called when delivery succeeds or fails. Upon success, the handler is called with an error value of  . Upon failure, the handle is called with an error object that indicates what went wrong.

## See Also

- [func send(Data, toPeers: [MCPeerID], with: MCSessionSendDataMode) throws](mcsession/send(_:topeers:with:).md)
  Sends a message to nearby peers.
- [func startStream(withName: String, toPeer: MCPeerID) throws -> OutputStream](mcsession/startstream(withname:topeer:).md)
  Opens a byte stream to a nearby peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/sendresource(at:withname:topeer:withcompletionhandler:))*