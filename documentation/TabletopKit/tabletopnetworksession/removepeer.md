# removePeer(_:)

**Framework**: TabletopKit  
**Kind**: method

Notify the game that an existing peer disconnected

**Availability**:
- visionOS 2.0+

## Declaration

```swift
func removePeer(_ peer: TabletopNetworkSession<Coordinator>.Peer)
```

## Parameters

- `peer`: The peer that disconnected

## See Also

- [var peers: Set<TabletopNetworkSession<Coordinator>.Peer>](tabletopnetworksession/peers.md)
  The set of peers known by the game
- [func addPeer(TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/addpeer(_:).md)
  Notify the game that a new peer has connected
- [TabletopNetworkSession.Peer](tabletopnetworksession/peer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/removepeer(_:))*