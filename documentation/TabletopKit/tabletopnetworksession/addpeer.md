# addPeer(_:)

**Framework**: TabletopKit  
**Kind**: method

Notify the game that a new peer has connected

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func addPeer(_ peer: TabletopNetworkSession<Coordinator>.Peer)
```

## Parameters

- `peer`: The new peer

## See Also

- [var peers: Set<TabletopNetworkSession<Coordinator>.Peer>](tabletopnetworksession/peers.md)
  The set of peers known by the game
- [func removePeer(TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/removepeer(_:).md)
  Notify the game that an existing peer disconnected
- [TabletopNetworkSession.Peer](tabletopnetworksession/peer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/addpeer(_:))*