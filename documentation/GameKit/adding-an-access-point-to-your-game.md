# Adding an access point to your game

**Framework**: GameKit

Provide your users a convenient connection to the Game Center dashboard.

#### Overview

You can add an  to your game that provides a way for players to manage their profile, and view leaderboards, achievements, and challenges.

The access point initially shows player highlights, like how many achievements they’ve earned and where they stand in leaderboards. Then the access point collapses into the player’s avatar and remains on your game’s screen. When the player taps or clicks the avatar, GameKit displays the dashboard so players can drill down into the details of their Game Center data, including more highlights and statistics. You can choose where to display the access point, and select the highlights to display.

![Image of an iPhone screen in landscape layout, showing a game called The Coast. In the upper left corner of the screen, the access point appears as a small icon and two lines of text documenting the player’s completed achievements.](https://docs-assets.developer.apple.com/published/067f62fec291874a8a29c06e09a9f0dc/media-3729929%402x.png)

You can also display the dashboard on its own, or a particular section of the dashboard. For more information, see [`Displaying the Game Center dashboard`](displaying-the-game-center-dashboard.md). For design guidance, see [`Human Interface Guidelines > Technologies > Game Center > Access point`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/game-center#Access-point).

##### Configure the Access Point

You can place the access point in a corner of the screen and choose whether to show highlights when the access point first appears, such as the number of achievements or the player’s rank on the default leaderboard. Start by obtaining the shared [`GKAccessPoint`](gkaccesspoint.md) object using the [`shared`](gkaccesspoint/shared.md) class property.

If you don’t want the access point to appear on the main window, set it to another window using the [`parentWindow`](gkaccesspoint/parentwindow.md) property. For example, set the parent window to your title screen or main menu. For volumetric games on visionOS, you need to set the parent window for the access point to appear. For immersive games on visionOS, it appears below the HUD and in front of the person by default.

Use the [`location`](gkaccesspoint/location-swift.property.md) property to set the corner in which the access point appears. The default location is the upper-left corner ([`GKAccessPoint.Location.topLeading`](gkaccesspoint/location-swift.enum/topleading.md)). For volumetric and immersive games on visionOS, if you don’t set the parent window, GameKit ignores the [`location`](gkaccesspoint/location-swift.property.md) property (see [`Configure the access point on visionOS`](adding-an-access-point-to-your-game#Configure-the-access-point-on-visionOS.md)).

```swift
// Place the access point on the upper-left corner.
GKAccessPoint.shared.location = .topLeading
```

For right-to-left languages, such as Arabic and Hebrew, the system flips the location. For example, [`GKAccessPoint.Location.topLeading`](gkaccesspoint/location-swift.enum/topleading.md) specifies the upper-right corner and [`GKAccessPoint.Location.bottomLeading`](gkaccesspoint/location-swift.enum/bottomleading.md) specifies the bottom-left corner.

To display highlights when the access point appears, set the [`showHighlights`](gkaccesspoint/showhighlights.md) property to [`true`](https://developer.apple.com/documentation/swift/true):

```swift
GKAccessPoint.shared.showHighlights = true
```

When you’re done configuring the access point, set the [`isActive`](gkaccesspoint/isactive.md) property to [`true`](https://developer.apple.com/documentation/swift/true):

```swift
GKAccessPoint.shared.isActive = true
```

Hide the access point when displaying game intros or settings. To give your players a consistent experience, see [`Access Point`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/game-center/overview/access-point/) in the [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/).

##### Adapt Your Game to the Access Point

You can observe access point properties to adjust your game when the access point either changes sizes or just before it presents the dashboard.

![Image of an iPhone screen in landscape layout, showing a player’s dashboard after the player clicks or taps the access point. The dashboard shows three sections, including icons and text, for navigating to the player’s profile, achievements, and leaderboards.](https://docs-assets.developer.apple.com/published/3d9b06cab64bffc6a1b78ffe862593e3/media-3680165%402x.png)

To adjust your graphics when the access point size changes (for example, while it displays highlights), observe the [`frameInScreenCoordinates`](gkaccesspoint/frameinscreencoordinates.md) property. Be sure to convert the screen coordinates of the access point to your view’s coordinates.

```swift
// Observe when the access point changes its size.
let observation = GKAccessPoint.shared.observe(
           \.frameInScreenCoordinates
    ) { [weak self] _,_ in
    let screenFrame = GKAccessPoint.shared.frameInScreenCoordinates
    let accessPointFrame = myView.convert(screenFrame, from: nil)
    // Adjust your layout.
}
```

To make changes to your game before the player interacts with the dashboard, observe the [`isPresentingGameCenter`](gkaccesspoint/ispresentinggamecenter.md) property. For example, you should pause animations when the player clicks or taps the access point to display the dashboard.

```swift
// Observe when the access point displays the dashboard.
let observation = GKAccessPoint.shared.observe(
           \.isPresentingGameCenter
    ) { [weak self] _,_ in
    self.paused = GKAccessPoint.shared.isPresentingGameCenter
}
```

##### Change the Focus and Display the Dashboard Programmatically

If you handle the input from an Apple TV remote and game controller yourself, you need to programmatically change the focus to the access point and display the dashboard when the player taps or clicks it.

You can use the [`frameInScreenCoordinates`](gkaccesspoint/frameinscreencoordinates.md) property to change the focus when the player navigates the area behind the access point:

```swift
// Track and update focus.
func trackController(position: CGPoint) {
  let screenFrame = GKAccessPoint.shared.frameInScreenCoordinates
  let accessFrame = myView.convert(screenFrame, from: nil)
  // If the point is in the access point, turn on feedback.
  accessPointElement.focusFeedback = CGRectContainsPoint(accessFrame, position)
}
```

Then use the [`trigger(state:handler:)`](gkaccesspoint/trigger(state:handler:).md) method to show the dashboard when the player selects the access point.

##### Configure the Access Point on Visionos

The location of the access point and dashboard varies depending on the type of visionOS game. To change the default behavior below, set the [`location`](gkaccesspoint/location-swift.property.md) and [`parentWindow`](gkaccesspoint/parentwindow.md) properties before you set [`isActive`](gkaccesspoint/isactive.md) to [`true`](https://developer.apple.com/documentation/swift/true). For example, if you don’t set the parent window of volumetric games, the access point doesn’t appear.

| Type | Access point behavior |
| --- | --- |
| Compatible | Appears over the main or parent window in the specified location. |
| Native | Appears outside of the main or parent window in the specified location. |
| Volumetric | If the parent window is non-`nil`, appears outside of it in the specified location. If the parent window is `nil` (the default value), it doesn’t appear. |
| Immersive | If the parent window is non-`nil`, appears outside of it in the specified location. If the parent window is `nil` (the default value), it appears below the HUD in front of the person and tracks their head position. |

For all types of visionOS games, when the person displays the dashboard using the access point, it appears in a separate floating container app that the person can position in the space. However, if you use the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class to present the dashboard (see [`Displaying the Game Center dashboard`](displaying-the-game-center-dashboard.md)), it appears anchored to the window, scene, or view relative to where you present the view controller.

## See Also

- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)
  Provide an interface for players to navigate to their Game Center data from your game.
- [class GKAccessPoint](gkaccesspoint.md)
  An object that allows players to view and manage their Game Center information from within your game.
- [class GKDialogController](gkdialogcontroller.md)
  An object that provides the ability to present the dashboard in macOS games.
- [protocol GKViewController](gkviewcontroller.md)
  The abstract base protocol adopted by GameKit view controller classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/adding-an-access-point-to-your-game)*