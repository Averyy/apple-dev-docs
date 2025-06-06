# matchmakerViewController(_:didReceiveAcceptFromHostedPlayer:)

**Framework**: GameKit  
**Kind**: method

Called when a player in a hosted match accepts the invitation.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer playerID: String)
```

#### Discussion

After a player accepts an invitation, that player’s device should connect to your server. Once the connection is established, your game should call the view controller’s [`setHostedPlayer(_:connected:)`](gkmatchmakerviewcontroller/sethostedplayer(_:connected:).md) method to update the player’s connection status.

## Parameters

- `viewController`: The view controller that accepted the invitation.
- `playerID`: The identifier of the accepting player.

## See Also

- [func matchmakerViewController(GKMatchmakerViewController, didFindPlayers: [String])](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfindplayers:).md)
  Called when a hosted match is found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didreceiveacceptfromhostedplayer:))*