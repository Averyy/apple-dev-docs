# connect(toPeer:withTimeout:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Creates a connection to another iOS device.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
func connect(toPeer peerID: String!, withTimeout timeout: TimeInterval)
```

```objc
- (void) connectToPeer:(NSString *) peerID withTimeout:(NSTimeInterval) timeout;
```

## Discussion

When your application is acting as a client, it calls this method to connect to an available peer it discovered. When your application calls this method, a request is transmitted to the remote peer, who chooses whether to accept or reject the connection request.

If the connection to the remote peer is successful, the delegate’s [`session(_:peer:didChange:)`](../gksessiondelegate/session%28_,peer,didchange%29.md) method is called for each peer it successfully connected to. If the connection fails or your application cancels the connection attempt, the session calls the delegate’s [`session(_:connectionWithPeerFailed:withError:)`](../gksessiondelegate/session%28_,connectionwithpeerfailed,witherror%29.md) method.

## Parameters

- `peerID`: The string that identifies the peer to connect to.
- `timeout`: The amount of time to wait before canceling the connection attempt.

## See Also

### Connecting to a Remote Peer
- [func cancelConnect(toPeer: String!)](./cancelconnect%28topeer%29.md)
  Cancels a pending request to connect to another iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/connect(topeer:withtimeout:))*