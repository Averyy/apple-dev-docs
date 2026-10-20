# GKMatchmakerViewControllerDelegate

**Framework**: GameKit  
**Kind**: protocol  
**Role**: Protocol

An object that handles when the status of matchmaking changes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol GKMatchmakerViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol GKMatchmakerViewControllerDelegate <NSObject>
```

## Mentions

- [Finding multiple players for a game](./finding-multiple-players-for-a-game.md)

#### Overview

The delegate of a [`GKMatchmakerViewController`](./gkmatchmakerviewcontroller.md) object implements this protocol to handle when players accept invitations, the player cancels matchmaking, or an error occurs. In all these cases, except when a hosted player accepts a invitation, for example, [`matchmakerViewController(_:hostedPlayerDidAccept:)`](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,hostedplayerdidaccept%29.md), the delegate needs to dismiss the view controller.

## Topics

### Starting matches
- [func matchmakerViewController(GKMatchmakerViewController, didFind: GKMatch)](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,didfind%29.md)
  Handles when the view controller finds players for a peer-to-peer match.
- [func matchmakerViewController(GKMatchmakerViewController, didFindHostedPlayers: [GKPlayer])](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,didfindhostedplayers%29.md)
  Handles when the view controller finds all requested players for a hosted match.
### Matching players using rules
- [func matchmakerViewController(GKMatchmakerViewController, getMatchPropertiesForRecipient: GKPlayer, withCompletionHandler: ([String : Any]) -> Void)](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,getmatchpropertiesforrecipient,withcompletionhandler%29.md)
  Returns the properties for another player that the local player invites using the view controller interface.
### Handling cancellations and errors
- [func matchmakerViewControllerWasCancelled(GKMatchmakerViewController)](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontrollerwascancelled%28_%29.md)
  Handles when a player cancels a request to find players for a match.
- [func matchmakerViewController(GKMatchmakerViewController, didFailWithError: any Error)](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,didfailwitherror%29.md)
  Handles when a view controller encounters an error while finding players for a match.
### Hosting matches
- [func matchmakerViewController(GKMatchmakerViewController, hostedPlayerDidAccept: GKPlayer)](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,hostedplayerdidaccept%29.md)
  Handles when a player in a hosted match accepts the invitation.
### Deprecated Methods
- [func matchmakerViewController(GKMatchmakerViewController, didFindPlayers: [String])](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,didfindplayers%29.md)
  Called when a hosted match is found.
- [func matchmakerViewController(GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer: String)](./gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller%28_,didreceiveacceptfromhostedplayer%29.md)
  Called when a player in a hosted match accepts the invitation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Setting the delegate
- [var matchmakerDelegate: (any GKMatchmakerViewControllerDelegate)?](./gkmatchmakerviewcontroller/matchmakerdelegate.md)
  The object that handles matchmaker view controller changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate)*