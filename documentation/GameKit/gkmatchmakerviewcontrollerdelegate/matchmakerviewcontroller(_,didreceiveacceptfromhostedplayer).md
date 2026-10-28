# matchmakerViewController(_:didReceiveAcceptFromHostedPlayer:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Called when a player in a hosted match accepts the invitation.

**Availability**:
- iOS 5.0+ - Deprecated in 8.0
- iPadOS 5.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer playerID: String)
```

```objc
- (void) matchmakerViewController:(GKMatchmakerViewController *) viewController didReceiveAcceptFromHostedPlayer:(NSString *) playerID;
```

## Discussion

After a player accepts an invitation, that player’s device should connect to your server. Once the connection is established, your game should call the view controller’s [`setHostedPlayer(_:connected:)`](../gkmatchmakerviewcontroller/sethostedplayer%28_,connected%29.md) method to update the player’s connection status.

## Parameters

- `viewController`: The view controller that accepted the invitation.
- `playerID`: The identifier of the accepting player.

## See Also

### Deprecated Methods
- [func matchmakerViewController(GKMatchmakerViewController, didFindPlayers: [String])](./matchmakerviewcontroller%28_,didfindplayers%29.md)
  Called when a hosted match is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didreceiveacceptfromhostedplayer:))*