# GKTurnBasedMatchmakerViewController

**Framework**: GameKit  
**Kind**: class

An interface that allows a player to invite other players to a turn-based match and automatch to fill any empty slots.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class GKTurnBasedMatchmakerViewController
```

## Mentions

- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)

#### Overview

Before you create a `GKTurnBasedMatchmakerViewController` object, create a [`GKMatchRequest`](gkmatchrequest.md) object and configure it according to the parameters of your game. Then, pass the match request to the [`init(matchRequest:)`](gkmatchmakerviewcontroller/init(matchrequest:).md) initializer to create the view controller.

Configure the view controller and set its delegate before you present it to the local player. The view controller allows the local player to choose other players and optionally fill empty slots using automatch. The interface also allows players to select an existing match, forfeit a match, or view a completed match.

Implement the [`GKTurnBasedMatchmakerViewControllerDelegate`](gkturnbasedmatchmakerviewcontrollerdelegate.md) protocol to handle when a player selects players, cancels matchmaking, or encounters an error. Implement the [`turnBasedMatchmakerViewController(_:didFind:)`](gkturnbasedmatchmakerviewcontrollerdelegate/turnbasedmatchmakerviewcontroller(_:didfind:).md) delegate method to dismiss the view controller when the local player invites players.

Register as a listener of the [`GKLocalPlayerListener`](gklocalplayerlistener.md) protocol and implement [`GKTurnBasedEventListener`](gkturnbasedeventlistener.md) methods that handle other turn-based events. For example, implement the [`player(_:receivedTurnEventFor:didBecomeActive:)`](gkturnbasedeventlistener/player(_:receivedturneventfor:didbecomeactive:).md) to update match data and present the gameplay interface for the local player to take their turn.

In iOS, you present and dismiss the view controller from another view controller in your game, using the methods provided by the [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) class. If you use SwiftUI, you can get the root view controller from the [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication) object. In macOS, you use the [`GKDialogController`](gkdialogcontroller.md) class to present and dismiss the view controller.

## Topics

### Creating and Configuring the View Controller
- [init(matchRequest: GKMatchRequest)](gkturnbasedmatchmakerviewcontroller/init(matchrequest:).md)
  Creates a matchmaker view controller for the local player to start inviting other players to a turn-based game.
- [var showExistingMatches: Bool](gkturnbasedmatchmakerviewcontroller/showexistingmatches.md)
  A Boolean value that determines whether the view controller shows existing matches.
- [var matchmakingMode: GKMatchmakingMode](gkturnbasedmatchmakerviewcontroller/matchmakingmode.md)
  The mode that a multiplayer game uses to find players.
- [enum GKMatchmakingMode](gkmatchmakingmode.md)
  Possible modes that a multiplayer game uses to find matches.
### Setting the Delegate
- [var turnBasedMatchmakerDelegate: (any GKTurnBasedMatchmakerViewControllerDelegate)?](gkturnbasedmatchmakerviewcontroller/turnbasedmatchmakerdelegate.md)
  The object that handles turn-based matchmaker view controller changes.
- [protocol GKTurnBasedMatchmakerViewControllerDelegate](gkturnbasedmatchmakerviewcontrollerdelegate.md)
  A protocol that handles when the status of turn-based matchmaking changes.

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
- [SendableMetatype](../Swift/SendableMetatype.md)
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

- [Creating turn-based games](creating-turn-based-games.md)
  Develop games where multiple players take turns and can exchange data while waiting for their turn.
- [Starting turn-based matches and passing turns between players](starting-turn-based-matches-and-passing-turns-between-players.md)
  Let Game Center store and forward match data between players in a turn-based game.
- [Sending messages to players in turn-based games](sending-messages-to-players-in-turn-based-games.md)
  Notify players of match events by sending messages and game data.
- [Exchanging data between players in turn-based games](exchanging-data-between-players-in-turn-based-games.md)
  Add the ability for players to exchange game data and send messages while waiting for their turns.
- [class GKTurnBasedMatch](gkturnbasedmatch.md)
  An object that encapsulates the match data for games where players take turns.
- [class GKTurnBasedParticipant](gkturnbasedparticipant.md)
  A participant in a turn-based match.
- [protocol GKTurnBasedEventListener](gkturnbasedeventlistener.md)
  The protocol that handles turn-based and data-exchange events between participants in a match.
- [class GKTurnBasedExchange](gkturnbasedexchange.md)
  Exchange request information that participants send in a turn-based match.
- [class GKTurnBasedExchangeReply](gkturnbasedexchangereply.md)
  Details about a recipient’s response to an exchange request.
- [GKGameCenterBadgingDisabled](../BundleResources/Information-Property-List/GKGameCenterBadgingDisabled.md)
  A Boolean value indicating whether GameKit can add badges to a turn-based game icon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller)*