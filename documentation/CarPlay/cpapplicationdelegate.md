# CPApplicationDelegate

**Framework**: CarPlay  
**Kind**: protocol

The interface for handling CarPlay life-cycle events.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol CPApplicationDelegate : UIApplicationDelegate
```

#### Overview

You must implement [`CPApplicationDelegate`](cpapplicationdelegate.md) on the same object that serves as the delegate to your app.

## Topics

### Connecting to the CarPlay Interface
- [func application(UIApplication, didConnectCarInterfaceController: CPInterfaceController, to: CPWindow)](cpapplicationdelegate/application(_:didconnectcarinterfacecontroller:to:).md)
  Tells the app delegate that the app connected to the CarPlay interface.
- [func application(UIApplication, didDisconnectCarInterfaceController: CPInterfaceController, from: CPWindow)](cpapplicationdelegate/application(_:diddisconnectcarinterfacecontroller:from:).md)
  Tells the app delegate that the app disconnected from the CarPlay interface.
### Receiving the Selected Maneuver
- [func application(UIApplication, didSelect: CPManeuver)](cpapplicationdelegate/application(_:didselect:)-6ybyy.md)
  Tells the app delegate that the user selected a maneuver.
### Handling Navigation Alert Actions
- [func application(UIApplication, didSelect: CPNavigationAlert)](cpapplicationdelegate/application(_:didselect:)-478jb.md)
  Tells the app delegate that the user selected an action from a navigation alert.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIApplicationDelegate](../UIKit/UIApplicationDelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate)*