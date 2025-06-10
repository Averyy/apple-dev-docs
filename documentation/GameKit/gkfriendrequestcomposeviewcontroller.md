# GKFriendRequestComposeViewController

**Framework**: GameKit  
**Kind**: class

Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class GKFriendRequestComposeViewController
```

#### Overview

> ❗ **Important**:  Your game must initialize a local player before you can use any Game Center classes. If there is no initialized player, your game receives a [`GKError.Code.notAuthenticated`](gkerror/code/notauthenticated.md) error. For more information, see [`Authenticating a player`](authenticating-a-player.md).

To show a friend request, initialize a new `GKFriendRequestComposeViewController` object and set the delegate. Optionally, you can customize the request by adding a text message or a list of recipients. Then, present the new view controller and wait for the delegate to be called. Once the delegate is called, dismiss the view controller.

On iOS, you present and dismiss the view controller from another view controller in your game, using the methods provided by the [`UIViewController`](https://developer.apple.com/documentation/UIKit/UIViewController) class. In macOS, you use the [`GKDialogController`](gkdialogcontroller.md) class to present and dismiss the view controller. The listing below shows one way your view controller can allow a player to send a request to other players. For this method, an array of [`GKPlayer`](gkplayer.md) objects is passed in as a parameter. The method instantiates a `GKFriendRequestComposeViewController` object, sets its delegate, and adds the list of players intended to receive the invitation. The view controller then presents the friend request and returns.

```objc
- (void) inviteFriends: (NSArray*) players
{
    GKFriendRequestComposeViewController *friendRequestViewController = [[GKFriendRequestComposeViewController alloc] init];
    friendRequestViewController.composeViewDelegate = self;
    if (players.count)
    {
        [friendRequestViewController addRecipientPlayers: players];
    }
    [self presentViewController: friendRequestViewController animated: YES completion:nil];
    [friendRequestViewController release];
}
```

##### Subclassing Notes

The [`GKFriendRequestComposeViewController`](gkfriendrequestcomposeviewcontroller.md) class is not intended to be subclassed.

## Topics

### Determining the Maximum Number of Recipients
- [class func maxNumberOfRecipients() -> Int](gkfriendrequestcomposeviewcontroller/maxnumberofrecipients.md)
  Returns the maximum number of recipients permitted in a single request.
### Delegate
- [var composeViewDelegate: (any GKFriendRequestComposeViewControllerDelegate)?](gkfriendrequestcomposeviewcontroller/composeviewdelegate.md)
  The view controller’s delegate
### Adding Recipients
- [func addRecipients(withEmailAddresses: [String])](gkfriendrequestcomposeviewcontroller/addrecipients(withemailaddresses:).md)
  Adds recipients based on their email addresses.
- [func addRecipientPlayers([GKPlayer])](gkfriendrequestcomposeviewcontroller/addrecipientplayers(_:).md)
  Adds recipients based on their Game Center player identifiers.
- [func addRecipients(withPlayerIDs: [String])](gkfriendrequestcomposeviewcontroller/addrecipients(withplayerids:).md)
  Adds recipients based on their Game Center player identifiers.
### Setting an Invitation Message
- [func setMessage(String?)](gkfriendrequestcomposeviewcontroller/setmessage(_:).md)
  Sets the text message included in the friend invitation.

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
- [class GKGameCenterViewController](gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
- [class GKGameSession](gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
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

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller)*