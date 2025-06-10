# peers

**Framework**: TabletopKit  
**Kind**: property

The set of peers known by the game

**Availability**:
- visionOS 2.0+

## Declaration

```swift
var peers: Set<TabletopNetworkSession<Coordinator>.Peer> { get }
```

## See Also

- [func addPeer(TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/addpeer(_:).md)
  Notify the game that a new peer has connected
- [func removePeer(TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/removepeer(_:).md)
  Notify the game that an existing peer disconnected
- [TabletopNetworkSession.Peer](tabletopnetworksession/peer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession/peers)*