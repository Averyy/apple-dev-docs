# addPeer(_:)

**Framework**: TabletopKit  
**Kind**: method  
**Role**: Instance Method

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

### Managing network session peers
- [var peers: Set<TabletopNetworkSession<Coordinator>.Peer>](./peers.md)
  The set of peers known by the game
- [func removePeer(TabletopNetworkSession<Coordinator>.Peer)](./removepeer%28_%29.md)
  Notify the game that an existing peer disconnected
- [TabletopNetworkSession.Peer](./peer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/addpeer(_:))*