# matchmakerViewController(_:didFindPlayers:)

**Framework**: GameKit  
**Kind**: method

Called when a hosted match is found.

**Availability**:
- iOS 4.1+
- iPadOS 4.1+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindPlayers playerIDs: [String])
```

#### Discussion

This method is called when the view controller’s `hosted` property is [`true`](https://developer.apple.com/documentation/swift/true). Although optional in the protocol, if your game attaches a delegate to the view controller for a hosted match, the view controller expects your game to provide an implementation of this method.

The view controller returns the list of players to your game by calling this method. Your game is responsible for connecting these players to your own server and then using that server to relay messages between the players.

## Parameters

- `viewController`: The view controller that performed the matchmaking.
- `playerIDs`: An array of   objects containing player identifier for the matched players.

## See Also

- [func matchmakerViewController(GKMatchmakerViewController, didFind: GKMatch)](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfind:).md)
  Handles when the view controller finds players for a peer-to-peer match.
- [func matchmakerViewController(GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer: String)](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didreceiveacceptfromhostedplayer:).md)
  Called when a player in a hosted match accepts the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfindplayers:))*