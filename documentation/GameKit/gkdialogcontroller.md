# GKDialogController

**Framework**: GameKit  
**Kind**: class

An object that provides the ability to present the dashboard in macOS games.

**Availability**:
- macOS 10.8+

## Declaration

```swift
@MainActor
class GKDialogController
```

#### Overview

For macOS games, use a `GKDialogController` object to present the dashboard from which players can browse and manage their Game Center data.

Initialize a new [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) object, as you would for an iOS game, specifying the state and setting its delegate. Then get the singleton dialog controller using the [`shared()`](gkdialogcontroller/shared().md) class method, or initialize a new `GKDialogController` object.

To present the dashboard, set the [`parentWindow`](gkdialogcontroller/parentwindow.md) property to the window that should display the dashboard and then call the [`present(_:)`](gkdialogcontroller/present(_:).md) method, passing the `GKGameCenterViewController` object.

```swift
func presentAchievement() {
    let viewController = GKGameCenterViewController(achievementID: "101")
    viewController.gameCenterDelegate = self
    
    let dialogController = GKDialogController.shared()
    dialogController.parentWindow = NSApplication.shared.mainWindow
    dialogController.present(viewController)
}
```

When the player closes the dashboard, GameKit calls the [`gameCenterViewControllerDidFinish(_:)`](gkgamecentercontrollerdelegate/gamecenterviewcontrollerdidfinish(_:).md) delegate method. Implement this method to dismiss the shared dialog controller using the [`dismiss(_:)`](gkdialogcontroller/dismiss(_:).md) method.

```swift
func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController) {
    // Dismiss the view controller.
    let dialogController = GKDialogController.shared()
    dialogController.dismiss(self)
}
```

## Topics

### Accessing the Shared Dialog Controller
- [class func shared() -> GKDialogController](gkdialogcontroller/shared.md)
  Retrieves the shared instance of the dialog controller.
### Setting the Presentation Window
- [var parentWindow: NSWindow?](gkdialogcontroller/parentwindow.md)
  The window that displays the dashboard.
### Presenting and Dismissing the Dialog
- [func present(any NSViewController & GKViewController) -> Bool](gkdialogcontroller/present(_:).md)
  Presents the dashboard in the window.
- [func dismiss(Any)](gkdialogcontroller/dismiss(_:).md)
  Dismisses the dashboard.

## Relationships

### Inherits From
- [NSResponder](../AppKit/NSResponder.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)
  Provide your users a convenient connection to the Game Center dashboard.
- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)
  Provide an interface for players to navigate to their Game Center data from your game.
- [class GKAccessPoint](gkaccesspoint.md)
  An object that allows players to view and manage their Game Center information from within your game.
- [class GKGameCenterViewController](gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
- [protocol GKViewController](gkviewcontroller.md)
  The abstract base protocol adopted by GameKit view controller classes.
- [class GKNotificationBanner](gknotificationbanner.md)
  A Game Center-style banner that displays a message to the local player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkdialogcontroller)*