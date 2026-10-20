# peers

**Framework**: TabletopKit  
**Kind**: property  
**Role**: Instance Property

The set of peers known by the game

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var peers: Set<TabletopNetworkSession<Coordinator>.Peer> { get }
```

## See Also

### Managing network session peers
- [func addPeer(TabletopNetworkSession<Coordinator>.Peer)](./addpeer%28_%29.md)
  Notify the game that a new peer has connected
- [func removePeer(TabletopNetworkSession<Coordinator>.Peer)](./removepeer%28_%29.md)
  Notify the game that an existing peer disconnected
- [TabletopNetworkSession.Peer](./peer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/peers)*