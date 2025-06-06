# GKPeerPickerController

**Framework**: GameKit  
**Kind**: class

Provides a standard user interface to allow one iOS device to discover and connect to another.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
class GKPeerPickerController
```

#### Overview

The result is a configured [`GKSession`](gksession.md) object connecting the two devices. To use a [`GKPeerPickerController`](gkpeerpickercontroller.md) object, your application creates the controller, adds a delegate, configures the allowed connection types, and then shows the peer picker. The delegate is called as the user makes selections within the peer picker interface.

In iOS 3.0, the peer picker can be configured to select between Bluetooth and Internet connections.

> ❗ **Important**:  Although users can select Internet connections in the peer picker, [`GKPeerPickerController`](gkpeerpickercontroller.md) has no user interface for configuring them. If your application configures the peer picker to allow Internet connections, your application must also dismiss the peer picker and present its own interface to configure an Internet connection.

 Although users can select Internet connections in the peer picker, [`GKPeerPickerController`](gkpeerpickercontroller.md) has no user interface for configuring them. If your application configures the peer picker to allow Internet connections, your application must also dismiss the peer picker and present its own interface to configure an Internet connection.

On iOS 3.0, your application should release the peer picker object after it dismisses the peer picker dialog. On iOS 3.1 or later, your application may release the peer picker after it is shown to the user. If you do this, the peer picker controller is automatically deallocated after the dialog is dismissed.

## Topics

### Setting and Getting the Delegate
- [var delegate: (any GKPeerPickerControllerDelegate)?](gkpeerpickercontroller/delegate.md)
  The delegate of the peer picker controller.
### Displaying the Picker Dialog
- [func dismiss()](gkpeerpickercontroller/dismiss.md)
  Hides the peer picker dialog.
- [func show()](gkpeerpickercontroller/show.md)
  Displays the peer picker dialog to the user.
- [var isVisible: Bool](gkpeerpickercontroller/isvisible.md)
  A Boolean value that indicates whether the picker dialog is visible.
### Configuring Connectivity Options
- [var connectionTypesMask: GKPeerPickerConnectionType](gkpeerpickercontroller/connectiontypesmask.md)
  A mask that determines the types of connections a dialog presents to the user.
### Constants
- [enum GKPeerPickerConnectionType](gkpeerpickerconnectiontype.md)
  Network connections available to the peer picker dialog.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
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
- [class GKScore](gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKSession](gksession.md)
  A [`GKSession`](gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.
- [class GKTurnBasedEventHandler](gkturnbasedeventhandler.md)
  The [`GKTurnBasedEventHandler`](gkturnbasedeventhandler.md) class is used to respond to important messages related to turn-based matches. To use it, call the [`shared()`](gkturnbasedeventhandler/shared().md) class method to get the singleton instance and assign an object that implements the [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol to its [`delegate`](gkturnbasedeventhandler/delegate.md) property. All methods are called on the main thread.
- [class GKVoiceChat](gkvoicechat.md)
  A voice channel that allows players to speak with each other in a multiplayer game.
- [class GKVoiceChatService](gkvoicechatservice.md)
  The [`GKVoiceChatService`](gkvoicechatservice.md) class allows your application to connect two iOS devices into a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontroller)*