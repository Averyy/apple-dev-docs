# cancelConnect(toPeer:)

**Framework**: GameKit  
**Kind**: method

Cancels a pending request to connect to another iOS device.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func cancelConnect(toPeer peerID: String!)
```

#### Discussion

Your application previously called [`connect(toPeer:withTimeout:)`](gksession/connect(topeer:withtimeout:).md) to create a connection to another iOS device. When your application cancels the connection attempt, both delegates’ [`session(_:connectionWithPeerFailed:withError:)`](gksessiondelegate/session(_:connectionwithpeerfailed:witherror:).md) methods are called.

If your application already connected to the peer, your application should call [`disconnectFromAllPeers()`](gksession/disconnectfromallpeers().md) instead.

## Parameters

- `peerID`: The string identifying the peer you previously requested to connect to.

## See Also

- [func connect(toPeer: String!, withTimeout: TimeInterval)](gksession/connect(topeer:withtimeout:).md)
  Creates a connection to another iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/cancelconnect(topeer:))*