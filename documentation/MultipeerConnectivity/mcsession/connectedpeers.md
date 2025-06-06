# connectedPeers

**Framework**: Multipeer Connectivity  
**Kind**: property

An array of all peers that are currently connected to this session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var connectedPeers: [MCPeerID] { get }
```

## See Also

- [func connectPeer(MCPeerID, withNearbyConnectionData: Data)](mcsession/connectpeer(_:withnearbyconnectiondata:).md)
  Call this method to connect a peer to the session when using your own service discovery code instead of an  `MCNearbyServiceBrowser` or `MCBrowserViewController` object.
- [func cancelConnectPeer(MCPeerID)](mcsession/cancelconnectpeer(_:).md)
  Cancels an attempt to connect to a peer.
- [func nearbyConnectionData(forPeer: MCPeerID, withCompletionHandler: (Data?, (any Error)?) -> Void)](mcsession/nearbyconnectiondata(forpeer:withcompletionhandler:).md)
  Obtains connection data for the specified peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/connectedpeers)*