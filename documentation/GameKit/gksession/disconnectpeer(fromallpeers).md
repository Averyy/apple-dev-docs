# disconnectPeer(fromAllPeers:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Disconnects a connected peer from all peers connected to the session.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
func disconnectPeer(fromAllPeers peerID: String!)
```

```objc
- (void) disconnectPeerFromAllPeers:(NSString *) peerID;
```

## Parameters

- `peerID`: A string identifying the peer to disconnect.

## See Also

### Working with Connected Peers
- [func setDataReceiveHandler(Any!, withContext: UnsafeMutableRawPointer!)](./setdatareceivehandler%28_,withcontext%29.md)
  Sets the object that handles data received from other peers connected to the session.
- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](./send%28_,topeers,with%29.md)
  Transmits a collection of bytes to a list of connected peers.
- [func sendData(toAllPeers: Data!, with: GKSendDataMode) throws](./senddata%28toallpeers,with%29.md)
  Transmits a collection of bytes to all connected peers.
- [var disconnectTimeout: TimeInterval](./disconnecttimeout.md)
  A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.
- [func disconnectFromAllPeers()](./disconnectfromallpeers%28%29.md)
  Disconnects the session from all connected peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/disconnectpeer(fromallpeers:))*