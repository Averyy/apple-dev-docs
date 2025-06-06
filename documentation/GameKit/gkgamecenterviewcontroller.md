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
@MainActor
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
- [NSViewController](../AppKit/NSViewController.md)
- [UINavigationController](../UIKit/UINavigationController.md)
### Inherited By
- [GKAchievementViewController](gkachievementviewcontroller.md)
- [GKLeaderboardViewController](gkleaderboardviewcontroller.md)
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

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)
  Provide your users a convenient connection to the Game Center dashboard.
- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)
  Provide an interface for players to navigate to their Game Center data from your game.
- [class GKAccessPoint](gkaccesspoint.md)
  An object that allows players to view and manage their Game Center information from within your game.
- [class GKDialogController](gkdialogcontroller.md)
  An object that provides the ability to present the dashboard in macOS games.
- [protocol GKViewController](gkviewcontroller.md)
  The abstract base protocol adopted by GameKit view controller classes.
- [class GKNotificationBanner](gknotificationbanner.md)
  A Game Center-style banner that displays a message to the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller)*