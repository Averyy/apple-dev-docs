# matchmakerViewController(_:didFind:)

**Framework**: GameKit  
**Kind**: method

Handles when the view controller finds players for a peer-to-peer match.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFind match: GKMatch)
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)
- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)
- [Assigning players to teams using rules](assigning-players-to-teams-using-rules.md)
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)

#### Discussion

When all the players accept their invitations to a match, GameKit invokes this method in the app instances for all players in the match, including the local player who initiates the match. This method needs to dismiss the view controller and start the game. Use the match object passed to this method to get the players and communicate between them during the game.

Although this method appears optional in the protocol, if you set the view controller’s delegate for a peer-to-peer match, GameKit expects the delegate to implement this method. If the view controller’s [`isHosted`](gkmatchmakerviewcontroller/ishosted.md) property is [`true`](https://developer.apple.com/documentation/swift/true), GameKit instead invokes the [`matchmakerViewController(_:didFindHostedPlayers:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfindhostedplayers:).md) method.

## Parameters

- `viewController`: The view controller that finds players for the match.
- `match`: The match that the players join.

## See Also

- [func matchmakerViewController(GKMatchmakerViewController, didFindHostedPlayers: [GKPlayer])](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfindhostedplayers:).md)
  Handles when the view controller finds all requested players for a hosted match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfind:))*