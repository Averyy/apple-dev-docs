# isHosted

**Framework**: GameKit  
**Kind**: property

A Boolean value that indicates whether the match is hosted or peer-to-peer.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isHosted: Bool { get set }
```

## Mentions

- [Finding players for custom server-based games](finding-players-for-custom-server-based-games.md)

#### Discussion

The value of this property determines which delegate methods GameKit calls when players are found.

If you host your own game, set this property to `true,` and then GameKit calls the [`matchmakerViewController(_:didFindHostedPlayers:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfindhostedplayers:).md) delegate method when it finds players. You must provide a server that hosts the players in the match.

Otherwise, set this property to [`false`](https://developer.apple.com/documentation/Swift/false), and then GameKit calls the [`matchmakerViewController(_:didFind:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfind:).md) delegate method when it finds players.

## See Also

- [func setHostedPlayer(GKPlayer, didConnect: Bool)](gkmatchmakerviewcontroller/sethostedplayer(_:didconnect:).md)
  Updates the connection status of a player in a hosted game.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/ishosted)*