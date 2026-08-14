# GKGameCenterViewController

**Framework**: GameKit  
**Kind**: class

The dashboard that allows players to access their Game Center data in your game.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKGameCenterViewController
```

## Mentions

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)
- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)

#### Overview

This view controller presents the dashboard from which players can browse and manage their Game Center data. You can present the dashboard in a specific state from which players can navigate to other areas, including their profile. Your game should pause other activities before presenting the dashboard.

To present the dashboard, initialize a new [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) object and set its delegate. Optionally, initialize a view controller in a specific state, to show a leaderboard with scores from a set of players or during a time period, or to show a specific achievement. Then present the view controller to the player, and GameKit calls your delegate when the player dismisses it.

For visionOS games, the dashboard appears anchored to the window, scene, or view relative to where you present the view controller. For immersive games, set the parent window to a separate window group than the immersive space window group. For the visionOS location of the dashboard when using the access point, see [`Configure the access point on visionOS`](adding-an-access-point-to-your-game#Configure-the-access-point-on-visionOS.md).

## Topics

### Configuring Game Center content
- [init(state: GKGameCenterViewControllerState)](gkgamecenterviewcontroller/init(state:).md)
  Creates a view controller that presents the specified Game Center content.
- [enum GKGameCenterViewControllerState](gkgamecenterviewcontrollerstate.md)
  The type of content for the view controller to present.
- [init(leaderboard: GKLeaderboard, playerScope: GKLeaderboard.PlayerScope)](gkgamecenterviewcontroller/init(leaderboard:playerscope:).md)
  Creates a view controller that presents a leaderboard with data for the specified players.
- [init(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope)](gkgamecenterviewcontroller/init(leaderboardid:playerscope:timescope:).md)
  Creates a view controller that presents a leaderboard with data from the specified players and time period.
- [init(leaderboardSetID: String)](gkgamecenterviewcontroller/init(leaderboardsetid:).md)
  Creates a view controller that presents a leaderboard set.
- [init(achievementID: String)](gkgamecenterviewcontroller/init(achievementid:).md)
  Creates a view controller that presents an achievement.
- [init(player: GKPlayer)](gkgamecenterviewcontroller/init(player:).md)
  Creates a view controller that presents a player’s Game Center profile.
### Setting the view controller delegate
- [var gameCenterDelegate: (any GKGameCenterControllerDelegate)?](gkgamecenterviewcontroller/gamecenterdelegate.md)
  The view controller’s delegate.
- [protocol GKGameCenterControllerDelegate](gkgamecentercontrollerdelegate.md)
  The delegate that GameKit calls when the player dismisses the dashboard.
### Deprecated
- [Deprecated Symbols](gkgamecenterviewcontroller-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UINavigationController](../uikit/uinavigationcontroller.md)
### Inherited By
- [GKAchievementViewController](gkachievementviewcontroller.md)
- [GKLeaderboardViewController](gkleaderboardviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [GKViewController](gkviewcontroller.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
- [class GKChallenge](gkchallenge.md)
  A challenge issued by the local player to another player.
- [class GKScoreChallenge](gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [class GKCloudPlayer](gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameSession](gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
- [class GKFriendRequestComposeViewController](gkfriendrequestcomposeviewcontroller.md)
  Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.
- [class GKLeaderboardViewController](gkleaderboardviewcontroller.md)
  The `GKLeaderboardViewController` class provides a standard user interface that displays leaderboard scores to the player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKPeerPickerController](gkpeerpickercontroller.md)
  Provides a standard user interface to allow one iOS device to discover and connect to another.
- [class GKScore](gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKSession](gksession.md)
  A [`GKSession`](gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.
- [class GKTurnBasedEventHandler](gkturnbasedeventhandler.md)
  The [`GKTurnBasedEventHandler`](gkturnbasedeventhandler.md) class is used to respond to important messages related to turn-based matches. To use it, call the [`shared()`](gkturnbasedeventhandler/shared().md) class method to get the singleton instance and assign an object that implements the [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol to its [`delegate`](gkturnbasedeventhandler/delegate.md) property. All methods are called on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller)*