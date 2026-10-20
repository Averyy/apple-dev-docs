# GKAchievementViewController

**Framework**: GameKit  
**Kind**: class  
**Role**: Class

An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](./gkgamecenterviewcontroller.md) class is available, you should use it instead.

**Availability**:
- iOS 4.1+ - Deprecated in 7.0
- iPadOS 4.1+ - Deprecated in 7.0
- Mac Catalyst 4.1+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

## Declaration

```swift
class GKAchievementViewController
```

```objc
@interface GKAchievementViewController : GKGameCenterViewController
```

#### Overview

> ❗ **Important**:  Your game must initialize a local player before you can use any Game Center classes. If there is no initialized player, your game receives a [`GKError.Code.notAuthenticated`](./gkerror/code/notauthenticated.md) error. For more information, see [Authenticating a player](./authenticating-a-player.md).

To show achievements for the local player, initialize a new `GKAchievementViewController` object and set the delegate. Then present the new view controller and wait for the delegate to be called. Once the delegate is called, dismiss the view controller.

On iOS, you present and dismiss the view controller from another view controller in your game, using the methods provided by the [`UIViewController`](../UIKit/uiviewcontroller.md) class. In macOS, you use the [`GKDialogController`](./gkdialogcontroller.md) class to present and dismiss the view controller in a window.

##### Subclassing Notes

The `GKAchievementViewController` class is not intended to be subclassed.

## Topics

### Setting the Delegate
- [var achievementDelegate: (any GKAchievementViewControllerDelegate)!](./gkachievementviewcontroller/achievementdelegate.md)
  The achievement view controller’s delegate.

## Relationships

### Inherits From
- [GKGameCenterViewController](./gkgamecenterviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [GKViewController](./gkviewcontroller.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Deprecated classes
- [class GKChallengeEventHandler](./gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](./gkchallengesviewcontroller.md)
- [class GKChallenge](./gkchallenge.md)
  A challenge issued by the local player to another player.
- [class GKScoreChallenge](./gkscorechallenge.md)
  A type of challenge where a player must beat the leaderboard score of another player.
- [class GKAchievementChallenge](./gkachievementchallenge.md)
  A type of challenge where a player must earn another player’s achievement.
- [class GKCloudPlayer](./gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameCenterViewController](./gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
- [class GKGameSession](./gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](./gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
- [class GKFriendRequestComposeViewController](./gkfriendrequestcomposeviewcontroller.md)
  Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.
- [class GKLeaderboardViewController](./gkleaderboardviewcontroller.md)
  The `GKLeaderboardViewController` class provides a standard user interface that displays leaderboard scores to the player. If the [`GKGameCenterViewController`](./gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKPeerPickerController](./gkpeerpickercontroller.md)
  Provides a standard user interface to allow one iOS device to discover and connect to another.
- [class GKScore](./gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKSession](./gksession.md)
  A [`GKSession`](./gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.
- [class GKTurnBasedEventHandler](./gkturnbasedeventhandler.md)
  The [`GKTurnBasedEventHandler`](./gkturnbasedeventhandler.md) class is used to respond to important messages related to turn-based matches. To use it, call the [`shared()`](./gkturnbasedeventhandler/shared%28%29.md) class method to get the singleton instance and assign an object that implements the [`GKTurnBasedEventHandlerDelegate`](./gkturnbasedeventhandlerdelegate.md) protocol to its [`delegate`](./gkturnbasedeventhandler/delegate.md) property. All methods are called on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller)*