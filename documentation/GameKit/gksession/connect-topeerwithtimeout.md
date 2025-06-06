# connect(toPeer:withTimeout:)

**Framework**: GameKit  
**Kind**: method

Creates a connection to another iOS device.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func connect(toPeer peerID: String!, withTimeout timeout: TimeInterval)
```

#### Discussion

When your application is acting as a client, it calls this method to connect to an available peer it discovered. When your application calls this method, a request is transmitted to the remote peer, who chooses whether to accept or reject the connection request.

If the connection to the remote peer is successful, the delegate’s [`session(_:peer:didChange:)`](gksessiondelegate/session(_:peer:didchange:).md) method is called for each peer it successfully connected to. If the connection fails or your application cancels the connection attempt, the session calls the delegate’s [`session(_:connectionWithPeerFailed:withError:)`](gksessiondelegate/session(_:connectionwithpeerfailed:witherror:).md) method.

## Parameters

- `peerID`: The string that identifies the peer to connect to.
- `timeout`: The amount of time to wait before canceling the connection attempt.

## See Also

- [func cancelConnect(toPeer: String!)](gksession/cancelconnect(topeer:).md)
  Cancels a pending request to connect to another iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/connect(topeer:withtimeout:))*