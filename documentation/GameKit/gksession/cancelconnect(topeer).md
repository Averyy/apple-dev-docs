# cancelConnect(toPeer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Cancels a pending request to connect to another iOS device.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 2.0+ - Deprecated in 2.0

## Declaration

```swift
func cancelConnect(toPeer peerID: String!)
```

```objc
- (void) cancelConnectToPeer:(NSString *) peerID;
```

## Discussion

Your application previously called [`connect(toPeer:withTimeout:)`](./connect%28topeer,withtimeout%29.md) to create a connection to another iOS device. When your application cancels the connection attempt, both delegates’ [`session(_:connectionWithPeerFailed:withError:)`](../gksessiondelegate/session%28_,connectionwithpeerfailed,witherror%29.md) methods are called.

If your application already connected to the peer, your application should call [`disconnectFromAllPeers()`](./disconnectfromallpeers%28%29.md) instead.

## Parameters

- `peerID`: The string identifying the peer you previously requested to connect to.

## See Also

### Connecting to a Remote Peer
- [func connect(toPeer: String!, withTimeout: TimeInterval)](./connect%28topeer,withtimeout%29.md)
  Creates a connection to another iOS device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/cancelconnect(topeer:))*