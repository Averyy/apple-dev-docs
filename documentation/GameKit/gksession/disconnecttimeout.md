# disconnectTimeout

**Framework**: GameKit  
**Kind**: property

A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var disconnectTimeout: TimeInterval { get set }
```

#### Discussion

The timeout is the waiting period before disconnecting a peer from the session. If a peer is disconnected, the delegate’s [`session(_:peer:didChange:)`](gksessiondelegate/session(_:peer:didchange:).md) method is called.

## See Also

- [func setDataReceiveHandler(Any!, withContext: UnsafeMutableRawPointer!)](gksession/setdatareceivehandler(_:withcontext:).md)
  Sets the object that handles data received from other peers connected to the session.
- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](gksession/send(_:topeers:with:).md)
  Transmits a collection of bytes to a list of connected peers.
- [func sendData(toAllPeers: Data!, with: GKSendDataMode) throws](gksession/senddata(toallpeers:with:).md)
  Transmits a collection of bytes to all connected peers.
- [func disconnectFromAllPeers()](gksession/disconnectfromallpeers.md)
  Disconnects the session from all connected peers.
- [func disconnectPeer(fromAllPeers: String!)](gksession/disconnectpeer(fromallpeers:).md)
  Disconnects a connected peer from all peers connected to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/disconnecttimeout)*