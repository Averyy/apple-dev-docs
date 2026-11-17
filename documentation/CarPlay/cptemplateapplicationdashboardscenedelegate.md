# CPTemplateApplicationDashboardSceneDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The methods for responding to the life-cycle events of your navigation app’s dashboard scene.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
protocol CPTemplateApplicationDashboardSceneDelegate : UISceneDelegate
```

```objc
@protocol CPTemplateApplicationDashboardSceneDelegate <UISceneDelegate>
```

## Overview

This protocol defines methods that CarPlay calls when the scene connects and disconnects, and your implementation provides the appropriate behavior when these events occur. For example, setting the window’s root view controller when CarPlay connects your navigation app’s dashboard scene.

You don’t create instances of your dashboard scene delegate directly. Instead, you specify the name of the class as part of the CarPlay scene configuration you add to your `Info.plist` file—see the example below—or that you return from your app delegate’s [`application(_:configurationForConnecting:options:)`](../UIKit/uiapplicationdelegate/application%28_,configurationforconnecting,options%29.md) method.

```plist
<key>CPTemplateApplicationDashboardSceneSessionRoleApplication</key>
<array> 
    <dict>
        <key>UISceneClassName</key>
        <string>CPTemplateApplicationDashboardScene</string>
        <key>UISceneConfigurationName</key>
        <string>MyCarPlayDashboardSceneConfiguration</string>
        <!-- Specify the name of your dashboard scene delegate class. --> 
        <key>UISceneDelegateClassName</key>
        <string>MyCarPlayDashboardSceneDelegate</string> 
    </dict>
</array>
```

## Topics

### Responding to the dashboard scene life cycle
- [func templateApplicationDashboardScene(CPTemplateApplicationDashboardScene, didConnect: CPDashboardController, to: UIWindow)](./cptemplateapplicationdashboardscenedelegate/templateapplicationdashboardscene%28_,didconnect,to%29.md)
  Tells the delegate about the addition of a CarPlay Dashboard scene to your navigation app.
- [func templateApplicationDashboardScene(CPTemplateApplicationDashboardScene, didDisconnect: CPDashboardController, from: UIWindow)](./cptemplateapplicationdashboardscenedelegate/templateapplicationdashboardscene%28_,diddisconnect,from%29.md)
  Tells the delegate when CarPlay removes the dashboard scene from your navigation app.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UISceneDelegate](../UIKit/uiscenedelegate.md)

## See Also

### Dashboard display
- [class CPDashboardController](./cpdashboardcontroller.md)
  A controller that provides shortcut buttons for the CarPlay Dashboard.
- [class CPDashboardButton](./cpdashboardbutton.md)
  A shortcut button for placement on the CarPlay Dashboard.
- [class CPTemplateApplicationDashboardScene](./cptemplateapplicationdashboardscene.md)
  A CarPlay scene that controls your app’s dashboard navigation window.
- [CPSupportsDashboardNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsdashboardnavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Dashboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscenedelegate)*