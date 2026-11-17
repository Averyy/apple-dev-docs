# CPTemplateApplicationSceneDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

Methods for responding to  life-cycle events in your app’s scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
protocol CPTemplateApplicationSceneDelegate : UISceneDelegate
```

```objc
@protocol CPTemplateApplicationSceneDelegate <UISceneDelegate>
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

This protocol defines methods that CarPlay calls when it connects or disconnects a scene, as well as methods for responding to specific interactions with your interface. Adopt this protocol in one of your app’s custom types and use its methods to implement the expected behaviors. Your delegate object is responsible for setting up your app’s initial interface and handling any cleanup when the scene closes.

After you adopt this protocol in a custom type, you don’t instantiate that type directly. Instead, you specify the name of that type in your app’s scene manifest along with rest of the scene information. When someone launches your app, CarPlay instantiates the scene and your delegate type using the information in the scene manifest. The following example shows the keys and values from an app’s main CarPlay scene. The `MyCarPlaySceneDelegate` string is the name of an app-specific type that implements this protocol.

```plist
<key>CPTemplateApplicationSceneSessionRoleApplication</key>
<array>
    <dict>
        <key>UISceneClassName</key>
        <string>CPTemplateApplicationScene</string>
        <key>UISceneConfigurationName</key>
        <string>MyCarPlaySceneConfiguration</string>
        <!-- Specify the name of your scene delegate class. -->
        <key>UISceneDelegateClassName</key>
        <string>MyCarPlaySceneDelegate</string>
    </dict>
</array>
```

At the start of a session, the system delivers a [`CPInterfaceController`](./cpinterfacecontroller.md) object to your delegate’s [`templateApplicationScene(_:didConnect:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) or [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method. You can also retrieve this object from the scene’s [`interfaceController`](./cptemplateapplicationscene/interfacecontroller.md) property at any time. Use this controller object to present the content for your app’s interface. If you’re creating a navigation app, you also need to present your map content using the scene’s window object.

For information about how to specify your app’s scene manifest, see [Specifying the scenes your app supports](../UIKit/specifying-the-scenes-your-app-supports.md).

## Topics

### Responding to scene life-cycle events
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md)
  Tells the delegate that CarPlay added a main scene to your app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md)
  Tells the delegate that CarPlay added a main scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,diddisconnectinterfacecontroller%29.md)
  Tells the delegate about the removal of a CarPlay scene from your app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,diddisconnect,from%29.md)
  Tells the delegate about the removal of a CarPlay scene from your navigation app.
### Responding to interactions
- [func templateApplicationScene(CPTemplateApplicationScene, didSelect: CPManeuver)](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didselect%29-5rf2h.md)
  Tells your navigation app when someone selects a maneuver while your app is in the background.
- [func templateApplicationScene(CPTemplateApplicationScene, didSelect: CPNavigationAlert)](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didselect%29-7bie0.md)
  Tells your navigation app that someone selected a navigation alert while your app was in the background.
### Responding to interface changes
- [func contentStyleDidChange(UIUserInterfaceStyle)](./cptemplateapplicationscenedelegate/contentstyledidchange%28_%29.md)
  Tells your app that the suggested content style for this scene changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UISceneDelegate](../UIKit/uiscenedelegate.md)

## See Also

### App management
- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)
  Build the interface for your CarPlay app using scenes and templates from the CarPlay framework.
- [class CPTemplateApplicationScene](./cptemplateapplicationscene.md)
  A CarPlay scene that manages your app’s interface on the vehicle’s center display.
- [class CPInterfaceController](./cpinterfacecontroller.md)
  The type you use to present your app’s CarPlay interface and change what appears on the vehicle’s display.
- [class CPSessionConfiguration](./cpsessionconfiguration.md)
  An object that keeps you informed of changes to the CarPlay environment.
- [class CPWindow](./cpwindow.md)
  A type that navigation apps use to present their map content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate)*