# connectedPeers

**Framework**: Multipeer Connectivity  
**Kind**: property  
**Role**: Instance Property

An array of all peers that are currently connected to this session.

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
var connectedPeers: [MCPeerID] { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) NSArray<MCPeerID *> * connectedPeers;
```

*macOS*

```objc
@property (atomic, readonly) NSArray<MCPeerID *> * connectedPeers;
```

## See Also

### Managing Peers Manually
- [func connectPeer(MCPeerID, withNearbyConnectionData: Data)](./connectpeer%28_,withnearbyconnectiondata%29.md)
  Call this method to connect a peer to the session when using your own service discovery code instead of an  `MCNearbyServiceBrowser` or `MCBrowserViewController` object.
- [func cancelConnectPeer(MCPeerID)](./cancelconnectpeer%28_%29.md)
  Cancels an attempt to connect to a peer.
- [func nearbyConnectionData(forPeer: MCPeerID, withCompletionHandler: (Data?, (any Error)?) -> Void)](./nearbyconnectiondata%28forpeer,withcompletionhandler%29.md)
  Obtains connection data for the specified peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/connectedpeers)*