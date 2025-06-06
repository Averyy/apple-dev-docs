# GKPlayerConnectionState

**Framework**: GameKit  
**Kind**: enum

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

## Topics

### States
- [GKPlayerConnectionState.unknown](gkplayerconnectionstate/unknown.md)
  An undetermined state in which the player can’t receive data.
- [GKPlayerConnectionState.connected](gkplayerconnectionstate/connected.md)
  A state in which a player connects to the match and can receive data.
- [GKPlayerConnectionState.disconnected](gkplayerconnectionstate/disconnected.md)
  A state in which a player disconnects from the match and can’t receive data.
### Initializers
- [init?(rawValue: Int)](gkplayerconnectionstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func match(GKMatch, player: GKPlayer, didChange: GKPlayerConnectionState)](gkmatchdelegate/match(_:player:didchange:)-8ohgr.md)
  Handles when players connect or disconnect from a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate)*