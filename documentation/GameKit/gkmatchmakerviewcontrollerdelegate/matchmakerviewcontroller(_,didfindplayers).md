# matchmakerViewController(_:didFindPlayers:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called when a hosted match is found.

**Availability**:
- iOS 4.1+ - Deprecated in 8.0
- iPadOS 4.1+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindPlayers playerIDs: [String])
```

```objc
- (void) matchmakerViewController:(GKMatchmakerViewController *) viewController didFindPlayers:(NSArray<NSString *> *) playerIDs;
```

#### Discussion

This method is called when the view controller’s `hosted` property is [`true`](../../Swift/true.md). Although optional in the protocol, if your game attaches a delegate to the view controller for a hosted match, the view controller expects your game to provide an implementation of this method.

The view controller returns the list of players to your game by calling this method. Your game is responsible for connecting these players to your own server and then using that server to relay messages between the players.

## Parameters

- `viewController`: The view controller that performed the matchmaking.
- `playerIDs`: An array of `NSString` objects containing player identifier for the matched players.

## See Also

### Related Documentation
- [func matchmakerViewController(GKMatchmakerViewController, didFind: GKMatch)](./matchmakerviewcontroller%28_,didfind%29.md)
  Handles when the view controller finds players for a peer-to-peer match.
### Deprecated Methods
- [func matchmakerViewController(GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer: String)](./matchmakerviewcontroller%28_,didreceiveacceptfromhostedplayer%29.md)
  Called when a player in a hosted match accepts the invitation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfindplayers:))*