# CPApplicationDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

A set of methods that are called by the @c UIApplication singleton in response to CarPlay lifecycle events.

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

This must be implemented by the same object that serves as your application’s delegate object.

## Topics

### Instance Methods
- [func application(UIApplication, didConnectCarInterfaceController: CPInterfaceController, to: CPWindow)](./cpapplicationdelegate/application%28_,didconnectcarinterfacecontroller,to%29.md)
  The CarPlay screen has connected and is ready to present content.
- [func application(UIApplication, didDisconnectCarInterfaceController: CPInterfaceController, from: CPWindow)](./cpapplicationdelegate/application%28_,diddisconnectcarinterfacecontroller,from%29.md)
  The CarPlay screen has disconnected.
- [func application(UIApplication, didSelect: CPNavigationAlert)](./cpapplicationdelegate/application%28_,didselect%29-478jb.md)
  If your application posts a @c CPNavigationAlert while backgrounded, a notification banner may be presented to the user. If the user taps on that banner, your application will launch on the car screen and this method will be called with the alert the user tapped.
- [func application(UIApplication, didSelect: CPManeuver)](./cpapplicationdelegate/application%28_,didselect%29-6ybyy.md)
  If your application posts a @c CPManeuver while backgrounded, a notification banner may be presented to the user. If the user taps on that banner, your application will launch on the car screen and this method will be called with the maneuver the user tapped.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIApplicationDelegate](../UIKit/uiapplicationdelegate.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpapplicationdelegate)*