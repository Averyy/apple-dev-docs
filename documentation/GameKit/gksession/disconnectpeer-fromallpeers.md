# disconnectPeer(fromAllPeers:)

**Framework**: GameKit  
**Kind**: method

Disconnects a connected peer from all peers connected to the session.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func disconnectPeer(fromAllPeers peerID: String!)
```

## Parameters

- `peerID`: A string identifying the peer to disconnect.

## See Also

- [func setDataReceiveHandler(Any!, withContext: UnsafeMutableRawPointer!)](gksession/setdatareceivehandler(_:withcontext:).md)
  Sets the object that handles data received from other peers connected to the session.
- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](gksession/send(_:topeers:with:).md)
  Transmits a collection of bytes to a list of connected peers.
- [func sendData(toAllPeers: Data!, with: GKSendDataMode) throws](gksession/senddata(toallpeers:with:).md)
  Transmits a collection of bytes to all connected peers.
- [var disconnectTimeout: TimeInterval](gksession/disconnecttimeout.md)
  A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.
- [func disconnectFromAllPeers()](gksession/disconnectfromallpeers.md)
  Disconnects the session from all connected peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/disconnectpeer(fromallpeers:))*