# Displaying the Game Center dashboard

**Framework**: GameKit

Provide an interface for players to navigate to their Game Center data from your game.

#### Overview

The  provides a central location from which players can browse and manage their Game Center data. The player can access information about their profile, as well as leaderboards, achievements, and challenges. The dashboard also displays highlights in these areas as the players navigate.

![Image of an iPhone screen in landscape layout, showing the dashboard with three sections, including icons and text, for navigating to the player’s profile, achievements, and leaderboards.](https://docs-assets.developer.apple.com/published/7300ae7964e4061207ae14afc4b1795e/media-3678721%402x.png)

Use the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class to present the dashboard in a specific state — such as the ,_ _from which the player can navigate to any area, including the player profile or a list of leaderboards. For visionOS games, the dashboard appears anchored to the window, scene, or view relative to where you present the view controller.

Alternatively, to add the access point to a fixed location in your game that allows the player to open the dashboard whenever they want, see [`Adding an access point to your game`](adding-an-access-point-to-your-game.md).

For design guidance, see [`Human Interface Guidelines > Technologies > Game Center > Custom dashboard links`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/game-center#Custom-dashboard-links).

##### Present the Main Dashboard

To display the main dashboard, pass `dashboard` as the state parameter to the [`init(state:)`](gkgamecenterviewcontroller/init(state:).md) method when you create the view controller, set the delegate of the view controller to your object, and then present it:

```swift
// Display the dashboard.
let viewController = GKGameCenterViewController(state: .dashboard)
viewController.gameCenterDelegate = self
present(viewController, animated: true, completion: nil)
```

##### Show the Players Profile

In the profile area, the player can see their achievements, find friends, and see what games their friends are playing. They can also edit their Game Center settings, such as their nickname and avatar.

![Image of an iPhone in landscape mode, showing the dashboard that displays the player’s profile.](https://docs-assets.developer.apple.com/published/100df426b285d711b3d63686901ae752/media-3678724%402x.png)

To present the local player’s profile, pass `localPlayerProfile` as the state parameter to the [`init(state:)`](gkgamecenterviewcontroller/init(state:).md) method:

```swift
// Display the player's profile.
let viewController = GKGameCenterViewController(state: .localPlayerProfile)
viewController.gameCenterDelegate = self
present(viewController, animated: true, completion: nil)
```

##### Present the List of Leaderboards

You can display a list of leaderboards in the dashboard that allows the player to navigate to the leaderboards they want to see. When the player selects a leaderboard, the dashboard displays the details for that leaderboard.

![Image of an iPhone in landscape mode, showing the dashboard that displays leaderboards for the game.](https://docs-assets.developer.apple.com/published/13649c99eaebea89da0e177b48486dea/media-3678722%402x.png)

To present a list of leaderboards, pass `leaderboards` as the state parameter to the [`init(state:)`](gkgamecenterviewcontroller/init(state:).md) method:

```swift
// Display a list of leaderboards.
let viewController = GKGameCenterViewController(state: .leaderboards)
viewController.gameCenterDelegate = self
present(viewController, animated: true, completion: nil)
```

##### Display a Single Leaderboard

You can present a specific leaderboard in the dashboard that allows players to see how they rank against friends, players with whom they played recently, and players from all over the world. They can use the filter in the header area to adjust the scope of the leaderboard by a time period, or show a specific occurrence of a recurring leaderboard. They can scroll to the top of the list by tapping on the name in the header.

![Image of an iPhone in landscape mode, showing the dashboard that displays a single leaderboard containing ranked player scores.](https://docs-assets.developer.apple.com/published/2d3d69cf494a3bb1b3b8546d0e650d57/media-3678725%402x.png)

To present a single leaderboard, pass the leaderboard ID (the identifier you entered in App Store Connect when creating the leaderboard) along with the player scope and time scope when you create the view controller:

```swift
// Display scores for a specific leaderboard.
let viewController = GKGameCenterViewController(
                leaderboardID: "grp.xyz.laketahoe",
                playerScope: .global,
                timeScope: .allTime)
viewController.gameCenterDelegate = self
present(viewController, animated: true, completion: nil)
```

The player can filter and scope scores by player (Friends, Recent, or Global) and time period (for example, All Time).

##### Display the Players Achievements

You can show the player a list of achievements they received and achievements they’ve yet to complete. An  is a collectible item indicating that the player successfully reached a particular goal in your game. In the dashboard, an achievement appears as either locked, in-progress, completed, or hidden.

![Image of an iPhone in landscape mode, showing the dashboard that displays the player’s achievements in a game.](https://docs-assets.developer.apple.com/published/ae95236da22d2a840c22fac2b1e99bee/media-3729931%402x.png)

To present the achievements, pass `achievements` as the state parameter to the [`init(state:)`](gkgamecenterviewcontroller/init(state:).md) method:

```swift
// Display a list of achievements.
let viewController = GKGameCenterViewController(state: .achievements)
viewController.gameCenterDelegate = self
present(viewController, animated: true, completion: nil)
```

##### Dismiss the Dashboard

Implement the [`gameCenterViewControllerDidFinish(_:)`](gkgamecentercontrollerdelegate/gamecenterviewcontrollerdidfinish(_:).md) delegate method in the [`GKGameCenterControllerDelegate`](gkgamecentercontrollerdelegate.md) protocol to dismiss the dashboard when the player closes it.

```swift
func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController) {
    // Dismiss the view controller.
    gameCenterViewController.dismiss(animated:true)
}
```

## See Also

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)
  Provide your users a convenient connection to the Game Center dashboard.
- [class GKAccessPoint](gkaccesspoint.md)
  An object that allows players to view and manage their Game Center information from within your game.
- [class GKDialogController](gkdialogcontroller.md)
  An object that provides the ability to present the dashboard in macOS games.
- [protocol GKViewController](gkviewcontroller.md)
  The abstract base protocol adopted by GameKit view controller classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/displaying-the-game-center-dashboard)*