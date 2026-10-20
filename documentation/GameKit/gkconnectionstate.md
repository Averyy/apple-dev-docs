# GKConnectionState

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Possible connection states for a player

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKConnectionState
```

```c
enum GKConnectionState : NSInteger;
```

## Topics

### Constants
- [GKConnectionState.connected](./gkconnectionstate/connected.md)
  The player is connected to the game session.
- [GKConnectionState.notConnected](./gkconnectionstate/notconnected.md)
  The player is not connected to the game session.
### Initializers
- [init?(rawValue: Int)](./gkconnectionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Changing Player Status
- [func session(GKGameSession, didAdd: GKCloudPlayer)](./gkgamesessioneventlistener/session%28_,didadd%29.md)
  Tells the listener a new player has been added to a game session.
- [func session(GKGameSession, didRemove: GKCloudPlayer)](./gkgamesessioneventlistener/session%28_,didremove%29.md)
  Tells the listener a player left a game session.
- [func session(GKGameSession, player: GKCloudPlayer, didChange: GKConnectionState)](./gkgamesessioneventlistener/session%28_,player,didchange%29.md)
  Tells the listener a player’s connection state has changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkconnectionstate)*