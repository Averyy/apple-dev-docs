# connectPeer(_:withNearbyConnectionData:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Call this method to connect a peer to the session when using your own service discovery code instead of an  `MCNearbyServiceBrowser` or `MCBrowserViewController` object.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func connectPeer(_ peerID: MCPeerID, withNearbyConnectionData data: Data)
```

#### Discussion

Call this method to connect to peers when you are using your own service discovery code instead of an `MCNearbyServiceBrowser` or `MCBrowserViewController` object. For more information, see the [`Managing Peers Manually`](mcsession#Managing-Peers-Manually.md) section in the overview of the `MCSession` class reference.

## Parameters

- `peerID`: The peer ID object obtained from the nearby peer.
- `data`: The connection data object obtained from the nearby peer.

## See Also

- [func cancelConnectPeer(MCPeerID)](mcsession/cancelconnectpeer(_:).md)
  Cancels an attempt to connect to a peer.
- [var connectedPeers: [MCPeerID]](mcsession/connectedpeers.md)
  An array of all peers that are currently connected to this session.
- [func nearbyConnectionData(forPeer: MCPeerID, withCompletionHandler: (Data?, (any Error)?) -> Void)](mcsession/nearbyconnectiondata(forpeer:withcompletionhandler:).md)
  Obtains connection data for the specified peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/connectpeer(_:withnearbyconnectiondata:))*