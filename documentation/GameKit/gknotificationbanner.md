# GKNotificationBanner

**Framework**: GameKit  
**Kind**: class

A Game Center-style banner that displays a message to the local player.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class GKNotificationBanner
```

#### Overview

This class displays a message in a banner to the local player, similar to the banner that GameKit displays when a player earns an achievement. If the game is in the foreground, the banner appears immediately. If the game is in the background, the banner appears when the game becomes active.

To display the banner with your message, use the [`show(withTitle:message:completionHandler:)`](gknotificationbanner/show(withtitle:message:completionhandler:).md) method. To specify a duration that GameKit presents the banner, use the [`show(withTitle:message:duration:completionHandler:)`](gknotificationbanner/show(withtitle:message:duration:completionhandler:).md) method instead. Optionally, pass these methods a completion handler that GameKit calls after it dismisses the banner.

```swift
GKNotificationBanner.show(withTitle:"Hooray",
                          message:"You passed level 1 and can move to level 2.",
                          completionHandler: nil)
```

## Topics

### Displaying the Banner
- [class func show(withTitle: String?, message: String?, completionHandler: (() -> Void)?)](gknotificationbanner/show(withtitle:message:completionhandler:).md)
  Displays a banner with a title and message to the player.
- [class func show(withTitle: String?, message: String?, duration: TimeInterval, completionHandler: (() -> Void)?)](gknotificationbanner/show(withtitle:message:duration:completionhandler:).md)
  Displays a banner to the player for a specified period of time.

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

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)
  Provide your users a convenient connection to the Game Center dashboard.
- [Displaying the Game Center dashboard](displaying-the-game-center-dashboard.md)
  Provide an interface for players to navigate to their Game Center data from your game.
- [class GKAccessPoint](gkaccesspoint.md)
  An object that allows players to view and manage their Game Center information from within your game.
- [class GKGameCenterViewController](gkgamecenterviewcontroller.md)
  The dashboard that allows players to access their Game Center data in your game.
- [class GKDialogController](gkdialogcontroller.md)
  An object that provides the ability to present the dashboard in macOS games.
- [protocol GKViewController](gkviewcontroller.md)
  The abstract base protocol adopted by GameKit view controller classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gknotificationbanner)*