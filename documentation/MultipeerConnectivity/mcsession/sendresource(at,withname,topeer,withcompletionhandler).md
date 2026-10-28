# sendResource(at:withName:toPeer:withCompletionHandler:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Sends the contents of a URL to a peer.

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
func sendResource(at resourceURL: URL, withName resourceName: String, toPeer peerID: MCPeerID, withCompletionHandler completionHandler: (((any Error)?) -> Void)? = nil) -> Progress?
```

```objc
- (NSProgress *) sendResourceAtURL:(NSURL *) resourceURL withName:(NSString *) resourceName toPeer:(MCPeerID *) peerID withCompletionHandler:(void (^)(NSError *error)) completionHandler;
```

## Return Value

An `NSProgress` object that can be used to query the status of the transfer or cancel the transfer.

## Discussion

This method is asynchronous (nonblocking).

On the local device, the completion handler block is called when delivery succeeds or when an error occurs.

On the recipient device, the session calls its delegate’s [`session(_:didStartReceivingResourceWithName:fromPeer:with:)`](../mcsessiondelegate/session%28_,didstartreceivingresourcewithname,frompeer,with%29.md) method as soon as it begins receiving the resource. This method provides an `NSProgress` object that your app can use to cancel the transfer or check its status.

Upon successful delivery, on the recipient device, the session calls its delegate’s [`session(_:didFinishReceivingResourceWithName:fromPeer:at:withError:)`](../mcsessiondelegate/session%28_,didfinishreceivingresourcewithname,frompeer,at,witherror%29.md) method. The received resource is written to a file in a temporary location with the same base name; the app is responsible for opening the file or moving it to a permanent location before that delegate method returns.

## Parameters

- `resourceURL`: A file or HTTP URL.
- `resourceName`: A name for the resource.
- `peerID`: The peer that should receive this resource.
- `completionHandler`: A block that gets called when delivery succeeds or fails. Upon success, the handler is called with an error value of `nil`. Upon failure, the handle is called with an error object that indicates what went wrong.

## See Also

### Sending Data and Resources
- [func send(Data, toPeers: [MCPeerID], with: MCSessionSendDataMode) throws](./send%28_,topeers,with%29.md)
  Sends a message to nearby peers.
- [func startStream(withName: String, toPeer: MCPeerID) throws -> OutputStream](./startstream%28withname,topeer%29.md)
  Opens a byte stream to a nearby peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/sendresource(at:withname:topeer:withcompletionhandler:))*