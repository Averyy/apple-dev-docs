# GKPlayerConnectionState

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

The possible states of a connection to a match.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
enum GKPlayerConnectionState
```

```c
enum GKPlayerConnectionState : NSInteger;
```

## Topics

### States
- [GKPlayerConnectionState.unknown](./gkplayerconnectionstate/unknown.md)
  An undetermined state in which the player can’t receive data.
- [GKPlayerConnectionState.connected](./gkplayerconnectionstate/connected.md)
  A state in which a player connects to the match and can receive data.
- [GKPlayerConnectionState.disconnected](./gkplayerconnectionstate/disconnected.md)
  A state in which a player disconnects from the match and can’t receive data.
### Initializers
- [init?(rawValue: Int)](./gkplayerconnectionstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Receiving State Notifications About Other Players
- [func match(GKMatch, player: GKPlayer, didChange: GKPlayerConnectionState)](./gkmatchdelegate/match%28_,player,didchange%29-8ohgr.md)
  Handles when players connect or disconnect from a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate)*