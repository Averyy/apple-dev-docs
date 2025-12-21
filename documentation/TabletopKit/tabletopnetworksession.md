# TabletopNetworkSession

**Framework**: TabletopKit  
**Kind**: class

An object that coordinates network-related tasks in multiplayer games.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
class TabletopNetworkSession<Coordinator> where Coordinator : TabletopNetworkSessionCoordinator
```

#### Overview

To start a multiplayer game for a local player, use the [`start()`](tabletopnetworksession/start().md) method. TabletopKit syncs the current table state between all peers in the session, so update the table state before invoking this method.

After invoking the [`start()`](tabletopnetworksession/start().md) method, the local player becomes the arbiter who ensures that TabletopKit applies actions in order for all players. To switch the arbiter role between players, use the [`becomeArbiter()`](tabletopnetworksession/becomearbiter().md) and [`followArbiter(_:)`](tabletopnetworksession/followarbiter(_:).md) methods.

To join an existing game, use the [`join()`](tabletopnetworksession/join().md) method, and to pass incoming messages to the game, use the [`processIncomingMessage(_:from:)`](tabletopnetworksession/processincomingmessage(_:from:).md) method.

To get all the people who join the session, not just the players, use the [`peers`](tabletopnetworksession/peers.md) property.

## Topics

### Joining multiplayer games
- [func start()](tabletopnetworksession/start.md)
  Start a new multiplayer game, promoting the local state of the table to all connected peers
- [func join()](tabletopnetworksession/join.md)
  Join an existing game started between the connected peers
- [func leave()](tabletopnetworksession/leave.md)
  Leave the current multiplayer game
- [func terminate()](tabletopnetworksession/terminate.md)
### Changing the arbiter role between players
- [func becomeArbiter()](tabletopnetworksession/becomearbiter.md)
- [func followArbiter(TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/followarbiter(_:).md)
### Managing network session peers
- [var peers: Set<TabletopNetworkSession<Coordinator>.Peer>](tabletopnetworksession/peers.md)
  The set of peers known by the game
- [func addPeer(TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/addpeer(_:).md)
  Notify the game that a new peer has connected
- [func removePeer(TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/removepeer(_:).md)
  Notify the game that an existing peer disconnected
- [TabletopNetworkSession.Peer](tabletopnetworksession/peer.md)
### Receiving messages from peers
- [func processIncomingMessage(Data, from: TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/processincomingmessage(_:from:).md)
  Pass incoming messages from the reliable channel to the game.
- [func processIncomingUnreliableMessage(Data, from: TabletopNetworkSession<Coordinator>.Peer)](tabletopnetworksession/processincomingunreliablemessage(_:from:).md)
  Pass incoming messages from the unreliable channel to the game.

## See Also

- [protocol TabletopNetworkSessionCoordinator](tabletopnetworksessioncoordinator.md)
  A protocol for objects that manage network sessions between peers.
- [enum TabletopSendMessageResult](tabletopsendmessageresult.md)
  The possible results of sending messages in a network session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksession)*