# lastModifiedPlayer

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The last player to modify the game session.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.12+ - Deprecated in 10.14
- tvOS 10.0+ - Deprecated in 12.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: For real-time matches, use GKMatchmakerViewController. For turn-based matches, use GKTurnBasedMatchmakerViewController.

## Declaration

```swift
var lastModifiedPlayer: GKCloudPlayer { get }
```

```objc
@property (nonatomic, readonly) GKCloudPlayer * lastModifiedPlayer;
```

#### Discussion

This property contains the [`GKCloudPlayer`](../gkcloudplayer.md) object representing the last player to modify the game session.

## See Also

### Accessing Information About a Game Session
- [var identifier: String](./identifier.md)
  A unique identifier for a game session.
- [var lastModifiedDate: Date](./lastmodifieddate.md)
  The date that the game session was last modified.
- [var maxNumberOfConnectedPlayers: Int](./maxnumberofconnectedplayers.md)
  The maximum number of players allowed to connect to the game session at the same time.
- [var owner: GKCloudPlayer](./owner.md)
  A player object that represents the owner of the game session.
- [var players: [GKCloudPlayer]](./players.md)
  An array of player objects associated with the game session.
- [var title: String](./title.md)
  The title of the game session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamesession/lastmodifiedplayer)*