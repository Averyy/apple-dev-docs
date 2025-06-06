# CPTemplateApplicationSceneDelegate

**Framework**: CarPlay  
**Kind**: protocol

The methods for responding to the life cycle events of your app’s scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol CPTemplateApplicationSceneDelegate : UISceneDelegate
```

## Mentions

- [Displaying Content in CarPlay](displaying-content-in-carplay.md)

#### Overview

This protocol defines methods that CarPlay calls when the scene connects and disconnects, as well as methods for responding to certain user actions. Use your implementation to provide the appropriate behavior for when these events occur. For example, creating and setting your root template when CarPlay launches your app and connects its scene.

You don’t create instances of your scene delegate directly. Instead, you specify the name of the class as part of the CarPlay scene configuration you add to your `Info.plist` file—see the example below—or that you return from your app delegate’s [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:))  method.

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

## Topics

### Responding to the Scene Life Cycle
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md)
  Tells the delegate about the addition of a CarPlay scene to the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didConnect: CPInterfaceController, to: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md)
  Tells the delegate about the addition of a CarPlay scene to your navigation app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnectInterfaceController: CPInterfaceController)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnectinterfacecontroller:).md)
  Tells the delegate when CarPlay removes a scene from the app.
- [func templateApplicationScene(CPTemplateApplicationScene, didDisconnect: CPInterfaceController, from: CPWindow)](cptemplateapplicationscenedelegate/templateapplicationscene(_:diddisconnect:from:).md)
  Tells the delegate when CarPlay removes a scene from your navigation app.
### Responding to User Actions
- [func templateApplicationScene(CPTemplateApplicationScene, didSelect: CPManeuver)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didselect:)-5rf2h.md)
  Tells the delegate when the user selects a maneuver while the app is in the background.
- [func templateApplicationScene(CPTemplateApplicationScene, didSelect: CPNavigationAlert)](cptemplateapplicationscenedelegate/templateapplicationscene(_:didselect:)-7bie0.md)
  Tells the delegate when the user selects a navigation alert while the app is in the background.
### Instance Methods
- [func contentStyleDidChange(UIUserInterfaceStyle)](cptemplateapplicationscenedelegate/contentstyledidchange(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UISceneDelegate](../UIKit/UISceneDelegate.md)

## See Also

- [Requesting CarPlay Entitlements](requesting-carplay-entitlements.md)
  Configure your CarPlay-enabled app with the entitlements it requires.
- [Displaying Content in CarPlay](displaying-content-in-carplay.md)
  Use scenes to present your app’s content on the vehicle’s built-in screen.
- [Supporting Previous Versions of iOS](supporting-previous-versions-of-ios.md)
  Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [Using the CarPlay Simulator](using-the-carplay-simulator.md)
  Configure Simulator to run and debug your CarPlay-enabled app.
- [class CPTemplateApplicationScene](cptemplateapplicationscene.md)
  A CarPlay scene that controls your app’s user interface.
- [class CPSessionConfiguration](cpsessionconfiguration.md)
  An object that provides vehicle properties and configuration for the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscenedelegate)*