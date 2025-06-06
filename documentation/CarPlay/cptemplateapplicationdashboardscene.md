# CPTemplateApplicationDashboardScene

**Framework**: CarPlay  
**Kind**: class

A CarPlay scene that controls your app’s dashboard navigation window.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+

## Declaration

```swift
@MainActor
class CPTemplateApplicationDashboardScene
```

#### Overview

A dashboard scene manages the display of your navigation app’s dashboard window on the CarPlay Dashboard, and notifies its delegate—an object that conforms to [`CPTemplateApplicationDashboardSceneDelegate`](cptemplateapplicationdashboardscenedelegate.md)—about scene life-cycle events. Use the dashboard controller the scene provides to supply shortcut buttons to display when there’s no active navigation session, further customizing you app’s presence on the CarPlay Dashboard.

You don’t create an instance of the dashboard scene directly. Instead, you specify the name of the class as part of the CarPlay Dashboard scene configuration that you add to your `Info.plist` file—see the example below—or that you return from your app delegate’s [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:)) method.

```plist
<key>CPTemplateApplicationDashboardSceneSessionRoleApplication</key>
<array> 
    <dict>
        <!-- Specify the name of the CarPlay Dashboard scene class. -->
        <key>UISceneClassName</key>
        <string>CPTemplateApplicationDashboardScene</string>
        <key>UISceneConfigurationName</key>
        <string>MyCarPlayDashboardSceneConfiguration</string> 
        <key>UISceneDelegateClassName</key>
        <string>MyCarPlayDashboardSceneDelegate</string> 
    </dict>
</array>
```

## Topics

### Responding to the Dashboard Scene Life Cycle
- [var delegate: (any CPTemplateApplicationDashboardSceneDelegate)?](cptemplateapplicationdashboardscene/delegate.md)
  The object that receives the dashboard scene’s life-cycle events.
- [protocol CPTemplateApplicationDashboardSceneDelegate](cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
### Accessing the Dashboard Controller
- [var dashboardController: CPDashboardController](cptemplateapplicationdashboardscene/dashboardcontroller.md)
  The controller that manages the dashboard scene’s shortcut buttons.
- [class CPDashboardController](cpdashboardcontroller.md)
  A controller that provides shortcut buttons for the CarPlay Dashboard.
### Accessing the Dashboard Window
- [var dashboardWindow: UIWindow](cptemplateapplicationdashboardscene/dashboardwindow.md)
  The window that belongs to the dashboard scene.

## Relationships

### Inherits From
- [UIScene](../UIKit/UIScene.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Integrating CarPlay with Your Navigation App](integrating-carplay-with-your-navigation-app.md)
  Configure your navigation app to work with CarPlay by displaying your custom map and directions.
- [protocol CPTemplateApplicationDashboardSceneDelegate](cptemplateapplicationdashboardscenedelegate.md)
  The methods for responding to the life-cycle events of your navigation app’s dashboard scene.
- [class CPMapTemplate](cpmaptemplate.md)
  A template that displays a navigation overlay that your app draws on the map.
- [class CPSearchTemplate](cpsearchtemplate.md)
  A template that provides the ability to search for a destination and see a list of search results.
- [class CPVoiceControlTemplate](cpvoicecontroltemplate.md)
  A template that displays a voice control indicator during audio input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationdashboardscene)*