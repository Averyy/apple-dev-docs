# matchmakerViewController(_:hostedPlayerDidAccept:)

**Framework**: GameKit  
**Kind**: method

Handles when a player in a hosted match accepts the invitation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, hostedPlayerDidAccept player: GKPlayer)
```

#### Discussion

After a player accepts an invitation, connect the player to your server. Once the connection is established, your game needs to call the view controller’s [`setHostedPlayer(_:didConnect:)`](gkmatchmakerviewcontroller/sethostedplayer(_:didconnect:).md) method to update the player’s connection status.

## Parameters

- `viewController`: The view controller that performs the matchmaking.
- `player`: The player that accepts the invitation to join the match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:hostedplayerdidaccept:))*