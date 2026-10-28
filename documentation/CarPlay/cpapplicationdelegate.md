# CPApplicationDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The interface for handling CarPlay life-cycle events.

**Availability**:
- iOS 12.0+ - Deprecated in 13.0
- iPadOS 12.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

## Declaration

```swift
protocol CPApplicationDelegate : UIApplicationDelegate
```

```objc
@protocol CPApplicationDelegate <UIApplicationDelegate>
```

## Overview

You must implement [`CPApplicationDelegate`](./cpapplicationdelegate.md) on the same object that serves as the delegate to your app.

## Topics

### Connecting to the CarPlay Interface
- [func application(UIApplication, didConnectCarInterfaceController: CPInterfaceController, to: CPWindow)](./cpapplicationdelegate/application%28_,didconnectcarinterfacecontroller,to%29.md)
  Tells the app delegate that the app connected to the CarPlay interface.
- [func application(UIApplication, didDisconnectCarInterfaceController: CPInterfaceController, from: CPWindow)](./cpapplicationdelegate/application%28_,diddisconnectcarinterfacecontroller,from%29.md)
  Tells the app delegate that the app disconnected from the CarPlay interface.
### Receiving the Selected Maneuver
- [func application(UIApplication, didSelect: CPManeuver)](./cpapplicationdelegate/application%28_,didselect%29-6ybyy.md)
  Tells the app delegate that the user selected a maneuver.
### Handling Navigation Alert Actions
- [func application(UIApplication, didSelect: CPNavigationAlert)](./cpapplicationdelegate/application%28_,didselect%29-478jb.md)
  Tells the app delegate that the user selected an action from a navigation alert.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIApplicationDelegate](../UIKit/uiapplicationdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate)*