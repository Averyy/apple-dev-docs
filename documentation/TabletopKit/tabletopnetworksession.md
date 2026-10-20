# TabletopNetworkSession

**Framework**: TabletopKit  
**Kind**: class  
**Role**: Class

An object that coordinates network-related tasks in multiplayer games.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
class TabletopNetworkSession<Coordinator> where Coordinator : TabletopNetworkSessionCoordinator
```

#### Overview

To start a multiplayer game for a local player, use the [`start()`](./tabletopnetworksession/start%28%29.md) method. TabletopKit syncs the current table state between all peers in the session, so update the table state before invoking this method.

After invoking the [`start()`](./tabletopnetworksession/start%28%29.md) method, the local player becomes the arbiter who ensures that TabletopKit applies actions in order for all players. To switch the arbiter role between players, use the [`becomeArbiter()`](./tabletopnetworksession/becomearbiter%28%29.md) and [`followArbiter(_:)`](./tabletopnetworksession/followarbiter%28_%29.md) methods.

To join an existing game, use the [`join()`](./tabletopnetworksession/join%28%29.md) method, and to pass incoming messages to the game, use the [`processIncomingMessage(_:from:)`](./tabletopnetworksession/processincomingmessage%28_,from%29.md) method.

To get all the people who join the session, not just the players, use the [`peers`](./tabletopnetworksession/peers.md) property.

## Topics

### Joining multiplayer games
- [func start()](./tabletopnetworksession/start%28%29.md)
  Start a new multiplayer game, promoting the local state of the table to all connected peers
- [func join()](./tabletopnetworksession/join%28%29.md)
  Join an existing game started between the connected peers
- [func leave()](./tabletopnetworksession/leave%28%29.md)
  Leave the current multiplayer game
- [func terminate()](./tabletopnetworksession/terminate%28%29.md)
### Changing the arbiter role between players
- [func becomeArbiter()](./tabletopnetworksession/becomearbiter%28%29.md)
- [func followArbiter(TabletopNetworkSession<Coordinator>.Peer)](./tabletopnetworksession/followarbiter%28_%29.md)
### Managing network session peers
- [var peers: Set<TabletopNetworkSession<Coordinator>.Peer>](./tabletopnetworksession/peers.md)
  The set of peers known by the game
- [func addPeer(TabletopNetworkSession<Coordinator>.Peer)](./tabletopnetworksession/addpeer%28_%29.md)
  Notify the game that a new peer has connected
- [func removePeer(TabletopNetworkSession<Coordinator>.Peer)](./tabletopnetworksession/removepeer%28_%29.md)
  Notify the game that an existing peer disconnected
- [TabletopNetworkSession.Peer](./tabletopnetworksession/peer.md)
### Receiving messages from peers
- [func processIncomingMessage(Data, from: TabletopNetworkSession<Coordinator>.Peer)](./tabletopnetworksession/processincomingmessage%28_,from%29.md)
  Pass incoming messages from the reliable channel to the game.
- [func processIncomingUnreliableMessage(Data, from: TabletopNetworkSession<Coordinator>.Peer)](./tabletopnetworksession/processincomingunreliablemessage%28_,from%29.md)
  Pass incoming messages from the unreliable channel to the game.

## See Also

### Multiplayer network session
- [protocol TabletopNetworkSessionCoordinator](./tabletopnetworksessioncoordinator.md)
  A protocol for objects that manage network sessions between peers.
- [enum TabletopSendMessageResult](./tabletopsendmessageresult.md)
  The possible results of sending messages in a network session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession)*