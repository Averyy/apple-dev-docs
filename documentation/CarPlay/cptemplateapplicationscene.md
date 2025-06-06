# CPTemplateApplicationScene

**Framework**: CarPlay  
**Kind**: class

A CarPlay scene that controls your app’s user interface.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPTemplateApplicationScene
```

#### Overview

A scene manages your app’s user interface, including the window that CarPlay displays from that scene. Only navigation apps have access to that window, and use it for drawing map content. All other categories of apps use the scene’s interface controller exclusively for constructing their user interfaces.

The scene manages the display of the window on the vehicle’s CarPlay screen, and the life cycle of that scene as CarPlay and the user interact with it. The scene notifies its delegate—an object that conforms to [`CPTemplateApplicationSceneDelegate`](cptemplateapplicationscenedelegate.md)—about various state changes and user actions.

You don’t create scenes directly. Instead, you specify the name of the appropriate scene class as part of the CarPlay scene configuration you add to your `Info.plist` file—see the example below—or that you return from your app delegate’s [`application(_:configurationForConnecting:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:configurationForConnecting:options:))  method.

```plist
<key>CPTemplateApplicationSceneSessionRoleApplication</key>
<array> 
    <dict>
        <!-- Specify the name of the scene class. -->
        <key>UISceneClassName</key>
        <string>CPTemplateApplicationScene</string>
        <key>UISceneConfigurationName</key>
        <string>MyCarPlaySceneConfiguration</string> 
        <key>UISceneDelegateClassName</key>
        <string>MyCarPlaySceneDelegate</string> 
    </dict>
</array>

```

## Topics

### Responding to the Scene Life Cycle
- [var delegate: (any CPTemplateApplicationSceneDelegate)?](cptemplateapplicationscene/delegate.md)
  The object that receives the scene’s life-cycle events.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.
### Accessing the Interface Controller
- [var interfaceController: CPInterfaceController](cptemplateapplicationscene/interfacecontroller.md)
  The controller that manages the scene’s user interface.
- [class CPInterfaceController](cpinterfacecontroller.md)
  A controller that manages the templates for constructing a scene’s user interface.
### Accessing the Window
- [var carWindow: CPWindow](cptemplateapplicationscene/carwindow.md)
  The window that belongs to the scene.
- [class CPWindow](cpwindow.md)
  A window that displays its content on the CarPlay screen.
### Instance Properties
- [var contentStyle: UIUserInterfaceStyle](cptemplateapplicationscene/contentstyle.md)

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
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Requesting CarPlay Entitlements](requesting-carplay-entitlements.md)
  Configure your CarPlay-enabled app with the entitlements it requires.
- [Displaying Content in CarPlay](displaying-content-in-carplay.md)
  Use scenes to present your app’s content on the vehicle’s built-in screen.
- [Supporting Previous Versions of iOS](supporting-previous-versions-of-ios.md)
  Make your CarPlay-enabled apps compatible with older system versions, such as iOS 13 and earlier.
- [Using the CarPlay Simulator](using-the-carplay-simulator.md)
  Configure Simulator to run and debug your CarPlay-enabled app.
- [protocol CPTemplateApplicationSceneDelegate](cptemplateapplicationscenedelegate.md)
  The methods for responding to the life cycle events of your app’s scene.
- [class CPSessionConfiguration](cpsessionconfiguration.md)
  An object that provides vehicle properties and configuration for the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene)*