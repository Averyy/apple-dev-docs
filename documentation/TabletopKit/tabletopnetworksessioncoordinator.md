# TabletopNetworkSessionCoordinator

**Framework**: TabletopKit  
**Kind**: protocol

A protocol for objects that manage network sessions between peers.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
protocol TabletopNetworkSessionCoordinator
```

#### Overview

Peers are networking participants that might or might not join a multiplayer game.

## Topics

### Starting network sessions
- [func coordinateWithSession(Self.NetworkSession)](tabletopnetworksessioncoordinator/coordinatewithsession(_:).md)
- [TabletopNetworkSessionCoordinator.NetworkSession](tabletopnetworksessioncoordinator/networksession.md)
### Managing network session peers
- [func peerJoinedGame(Self.Peer.ID)](tabletopnetworksessioncoordinator/peerjoinedgame(_:).md)
- [func peerLeftGame(Self.Peer.ID)](tabletopnetworksessioncoordinator/peerleftgame(_:).md)
- [associatedtype Peer : Hashable, Identifiable](tabletopnetworksessioncoordinator/peer.md)
### Sending messages between peers
- [func sendMessage(Data, to: Set<Self.Peer>, completion: (TabletopSendMessageResult) -> Void)](tabletopnetworksessioncoordinator/sendmessage(_:to:completion:).md)
- [func sendMessageUnreliably(Data, to: Set<Self.Peer>, completion: (TabletopSendMessageResult) -> Void)](tabletopnetworksessioncoordinator/sendmessageunreliably(_:to:completion:).md)

## See Also

- [class TabletopNetworkSession](tabletopnetworksession.md)
  An object that coordinates network-related tasks in multiplayer games.
- [enum TabletopSendMessageResult](tabletopsendmessageresult.md)
  The possible results of sending messages in a network session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopnetworksessioncoordinator)*