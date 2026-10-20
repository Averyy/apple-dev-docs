# removePeer(_:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

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

### Managing network session peers
- [var peers: Set<TabletopNetworkSession<Coordinator>.Peer>](./peers.md)
  The set of peers known by the game
- [func addPeer(TabletopNetworkSession<Coordinator>.Peer)](./addpeer%28_%29.md)
  Notify the game that a new peer has connected
- [TabletopNetworkSession.Peer](./peer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/removepeer(_:))*