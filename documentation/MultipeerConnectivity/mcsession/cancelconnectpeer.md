# cancelConnectPeer(_:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Cancels an attempt to connect to a peer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func cancelConnectPeer(_ peerID: MCPeerID)
```

#### Discussion

Call this method to cancel connections to peers when you are using your own service discovery code instead of an `MCNearbyServiceBrowser` or `MCBrowserViewController` object. It should be called in two situations:

- If your app calls [`connectPeer(_:withNearbyConnectionData:)`](mcsession/connectpeer(_:withnearbyconnectiondata:).md) and later needs to cancel the connection attempt
- If your app has obtained nearby connection data for a peer but you decide not to connect to the peer

For more information, see the [`Managing Peers Manually`](mcsession#Managing-Peers-Manually.md) section in the overview of the `MCSession` class reference.

## Parameters

- `peerID`: The ID of the nearby peer.

## See Also

- [func connectPeer(MCPeerID, withNearbyConnectionData: Data)](mcsession/connectpeer(_:withnearbyconnectiondata:).md)
  Call this method to connect a peer to the session when using your own service discovery code instead of an  `MCNearbyServiceBrowser` or `MCBrowserViewController` object.
- [var connectedPeers: [MCPeerID]](mcsession/connectedpeers.md)
  An array of all peers that are currently connected to this session.
- [func nearbyConnectionData(forPeer: MCPeerID, withCompletionHandler: (Data?, (any Error)?) -> Void)](mcsession/nearbyconnectiondata(forpeer:withcompletionhandler:).md)
  Obtains connection data for the specified peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/cancelconnectpeer(_:))*