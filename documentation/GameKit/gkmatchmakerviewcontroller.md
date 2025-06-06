# GKMatchmakerViewController

**Framework**: GameKit  
**Kind**: class

An interface that allows a player to invite other players to a real-time game and automatch to fill any empty slots.

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
class GKMatchmakerViewController
```

## Mentions

- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)
- [Finding players with similar skill levels](finding-players-with-similar-skill-levels.md)
- [Finding players using matchmaking rules](finding-players-using-matchmaking-rules.md)

#### Overview

Before you create a `GKMatchmakerViewController` object, create a [`GKMatchRequest`](gkmatchrequest.md) object and configure it according to the parameters of your game. Then pass the match request to the [`init(matchRequest:)`](gkmatchmakerviewcontroller/init(matchrequest:).md) initializer to create the view controller.

Configure the view controller and set its delegate before you present it to the local player. The view controller allows the local player to choose other players and, optionally, fill empty slots using automatch. If you add the Group Activities capability to your Xcode project, the player can invite others using SharePlay. See [`Configuring Group Activities`](https://developer.apple.com/documentation/Xcode/configuring-group-activities).

Implement the [`GKLocalPlayerListener`](gklocalplayerlistener.md) and [`GKMatchmakerViewControllerDelegate`](gkmatchmakerviewcontrollerdelegate.md) protocols to handle when players send and accept invitations. Implement the [`player(_:didAccept:)`](gkinviteeventlistener/player(_:didaccept:).md) delegate method to present a `GKMatchmakerViewController` object, which you create using the [`init(invite:)`](gkmatchmakerviewcontroller/init(invite:).md) initializer, to the player who accepts an invitation. Then, implement the [`matchmakerViewController(_:didFind:)`](gkmatchmakerviewcontrollerdelegate/matchmakerviewcontroller(_:didfind:).md) delegate method to dismiss the view controller and start the game when all players accept their invitations.

In iOS, you present and dismiss the view controller from another view controller in your game, using the methods from the [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) class. If you use SwiftUI, you can get the root view controller from the [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) object.

```swift
let rootViewController = UIApplication.shared.windows.first!.rootViewController
```

For visionOS games, the view controller appears anchored to the window, scene, or view relative to where you present the view controller. For immersive games, set the parent window to a separate window group than the immersive space window group.

For macOS games, use the [`GKDialogController`](gkdialogcontroller.md) class to present and dismiss the view controller.

For the complete matchmaking flow with code fragments, see [`Finding multiple players for a game`](finding-multiple-players-for-a-game.md).

## Topics

### Creating and configuring the view controller
- [init?(matchRequest: GKMatchRequest)](gkmatchmakerviewcontroller/init(matchrequest:).md)
  Creates a matchmaker view controller for the local player to start inviting other players.
- [init?(invite: GKInvite)](gkmatchmakerviewcontroller/init(invite:).md)
  Creates a matchmaker view controller to present to a player who accepts an invitation.
- [var matchRequest: GKMatchRequest](gkmatchmakerviewcontroller/matchrequest.md)
  The configuration for the desired match.
- [var canStartWithMinimumPlayers: Bool](gkmatchmakerviewcontroller/canstartwithminimumplayers.md)
  A Boolean value that indicates whether your game can start after a minimum number of players join a match.
- [var matchmakingMode: GKMatchmakingMode](gkmatchmakerviewcontroller/matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.
### Setting the delegate
- [var matchmakerDelegate: (any GKMatchmakerViewControllerDelegate)?](gkmatchmakerviewcontroller/matchmakerdelegate.md)
  The object that handles matchmaker view controller changes.
- [protocol GKMatchmakerViewControllerDelegate](gkmatchmakerviewcontrollerdelegate.md)
  An object that handles when the status of matchmaking changes.
### Adding players to matches
- [func addPlayers(to: GKMatch)](gkmatchmakerviewcontroller/addplayers(to:).md)
  Invites additional players to join an existing match.
### Hosting matches
- [var isHosted: Bool](gkmatchmakerviewcontroller/ishosted.md)
  A Boolean value that indicates whether the match is hosted or peer-to-peer.
- [func setHostedPlayer(GKPlayer, didConnect: Bool)](gkmatchmakerviewcontroller/sethostedplayer(_:didconnect:).md)
  Updates the connection status of a player in a hosted game.
### Deprecated
- [func setHostedPlayer(String, connected: Bool)](gkmatchmakerviewcontroller/sethostedplayer(_:connected:).md)
  Updates a player’s status on the view to show that the player has connected or disconnected from your server.
- [func setHostedPlayerReady(String)](gkmatchmakerviewcontroller/sethostedplayerready(_:).md)
  Informs the controller that a player has joined a hosted match.
- [var defaultInvitationMessage: String?](gkmatchmakerviewcontroller/defaultinvitationmessage.md)
  The default invitation message sent to a player.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UINavigationController](../UIKit/UINavigationController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [GKViewController](gkviewcontroller.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Creating real-time games](creating-real-time-games.md)
  Develop games where multiple players interact in real time.
- [Finding multiple players for a game](finding-multiple-players-for-a-game.md)
  Discover and invite other players to participate in a real-time game.
- [Exchanging data between players in real-time games](exchanging-data-between-players-in-real-time-games.md)
  Send data between players in a real-time multiplayer game.
- [Adding voice chat to multiplayer games](adding-voice-chat-to-multiplayer-games.md)
  Enable players to voice chat with all, or groups of, players in a multiplayer game.
- [Matchmaking rules](matchmaking-rules.md)
  Game Center applies different type of rules you create in a particular order to find the best matches.
- [class GKMatchRequest](gkmatchrequest.md)
  An object that encapsulates the parameters to create a real-time or turn-based match.
- [class GKMatchmaker](gkmatchmaker.md)
  An object that creates matches with other players without presenting an interface to the players.
- [protocol GKInviteEventListener](gkinviteeventlistener.md)
  A protocol that handles invite events from Game Center.
- [class GKInvite](gkinvite.md)
  An invitation to join a match sent to the local player from another player.
- [class GKMatch](gkmatch.md)
  A peer-to-peer network between a group of players that sign into Game Center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller)*