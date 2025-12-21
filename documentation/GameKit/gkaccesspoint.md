# GKAccessPoint

**Framework**: GameKit  
**Kind**: class

An object that allows players to view and manage their Game Center information from within your game.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class GKAccessPoint
```

## Mentions

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)

#### Overview

The access point displays a control in a corner of your game that opens a Game Center dashboard when the player taps or clicks it.

Use the [`shared`](gkaccesspoint/shared.md) property to get the shared access point object. GameKit attaches the access point to the window you specify in the [`parentWindow`](gkaccesspoint/parentwindow.md) property, in the corner you specify using the [`location`](gkaccesspoint/location-swift.property.md) property. If you don’t specify a parent window, GameKit infers an appropriate location. For the location of the access point on visionOS, see [`Configure the access point on visionOS`](adding-an-access-point-to-your-game#Configure-the-access-point-on-visionOS.md).

To display highlights, set the [`showHighlights`](gkaccesspoint/showhighlights.md) property to [`true`](https://developer.apple.com/documentation/Swift/true). Then set [`isActive`](gkaccesspoint/isactive.md) to [`true`](https://developer.apple.com/documentation/Swift/true) to display the access point control.

## Topics

### Getting the shared access point
- [class var shared: GKAccessPoint](gkaccesspoint/shared.md)
  The shared access point object.
### Managing the location
- [var location: GKAccessPoint.Location](gkaccesspoint/location-swift.property.md)
  The corner of the screen to display the access point.
- [GKAccessPoint.Location](gkaccesspoint/location-swift.enum.md)
  Specifies the corner of the screen to display the access point.
- [var frameInScreenCoordinates: CGRect](gkaccesspoint/frameinscreencoordinates.md)
  The frame of the access point in screen coordinates.
- [var parentWindow: UIWindow?](gkaccesspoint/parentwindow.md)
  The window that contains the access point.
### Displaying the access point
- [var isActive: Bool](gkaccesspoint/isactive.md)
  A Boolean value that determines whether to display the access point.
- [var isPresentingGameCenter: Bool](gkaccesspoint/ispresentinggamecenter.md)
  A Boolean value that indicates whether the game is presenting the Game Center dashboard.
- [var isVisible: Bool](gkaccesspoint/isvisible.md)
  A Boolean value that indicates whether the access point is visible.
- [var showHighlights: Bool](gkaccesspoint/showhighlights.md)
  A Boolean value that indicates whether to display highlights for achievements and current ranks for leaderboards.
### Managing the access point
- [var isFocused: Bool](gkaccesspoint/isfocused.md)
  A Boolean value that indicates whether the access point is in focus on tvOS.
- [func trigger(handler: () -> Void)](gkaccesspoint/trigger(handler:).md)
  Displays the Game Center dashboard as if the player taps or presses the access point.
- [func trigger(state: GKGameCenterViewControllerState, handler: () -> Void)](gkaccesspoint/trigger(state:handler:).md)
  Displays the Game Center dashboard in the specified state as if the player taps or presses the access point.
- [func trigger(player: GKPlayer, handler: (() -> Void)?)](gkaccesspoint/trigger(player:handler:).md)
  Displays the Game Center dashboard in a state that shows a player profile.
- [func trigger(achievementID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(achievementid:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific achievement.
- [func trigger(leaderboardID: String, playerScope: GKLeaderboard.PlayerScope, timeScope: GKLeaderboard.TimeScope, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardid:playerscope:timescope:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard.
- [func trigger(leaderboardSetID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(leaderboardsetid:handler:).md)
  Displays the Game Center dashboard in a state that shows a specific leaderboard set.
### Instance Methods
- [func trigger(challengeDefinitionID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(challengedefinitionid:handler:).md)
  Displays the challenge creation view for the provided challenge definition ID.
- [func trigger(gameActivity: GKGameActivity, handler: (() -> Void)?)](gkaccesspoint/trigger(gameactivity:handler:)-6lnz8.md)
- [func trigger(gameActivity: GKGameActivity, handler: (() -> Void)?)](gkaccesspoint/trigger(gameactivity:handler:)-8i6w7.md)
  Displays the game activity view for the provided activity instance.
- [func trigger(gameActivityDefinitionID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(gameactivitydefinitionid:handler:)-9hemd.md)
  Displays the game activity creation view for the provided activity definition ID.
- [func trigger(gameActivityDefinitionID: String, handler: (() -> Void)?)](gkaccesspoint/trigger(gameactivitydefinitionid:handler:)-9m45r.md)
- [func triggerForArcade(handler: (() -> Void)?)](gkaccesspoint/triggerforarcade(handler:).md)
  Brings up the Arcade dashboard.
- [func triggerForChallenges(handler: (() -> Void)?)](gkaccesspoint/triggerforchallenges(handler:).md)
  Displays the view that allows players to engage each other with challenges.
- [func triggerForFriending(handler: (() -> Void)?)](gkaccesspoint/triggerforfriending(handler:).md)
  Brings up the invite friends view.
- [func triggerForPlayTogether(handler: (() -> Void)?)](gkaccesspoint/triggerforplaytogether(handler:).md)
  Displays the view that allows players to engage each other with activities and challenges.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)
  Provide your users a convenient connection to the Game Center dashboard.
- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)
  Provide an interface for players to navigate to their Game Center data from your game.
- [class GKDialogController](gkdialogcontroller.md)
  An object that provides the ability to present the dashboard in macOS games.
- [protocol GKViewController](gkviewcontroller.md)
  The abstract base protocol adopted by GameKit view controller classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint)*