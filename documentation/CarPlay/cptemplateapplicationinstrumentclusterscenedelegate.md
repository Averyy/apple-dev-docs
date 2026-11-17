# CPTemplateApplicationInstrumentClusterSceneDelegate

**Framework**: CarPlay  
**Kind**: protocol  
**Role**: Protocol

The methods for responding to the life cycle events in your app’s instrument cluster scene.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
@MainActor
protocol CPTemplateApplicationInstrumentClusterSceneDelegate : UISceneDelegate
```

```objc
@protocol CPTemplateApplicationInstrumentClusterSceneDelegate <UISceneDelegate>
```

## Overview

This protocol defines methods that CarPlay calls when it connects or disconnects an instrument cluster scene, as well as a method for updating the style of your interface. Adopt this protocol in one of your app’s custom types and use its methods to implement the expected behaviors. Your delegate object is responsible for setting up the instrument cluster content and handling any cleanup when the scene closes.

After you adopt this protocol in a custom type, you don’t instantiate that type directly. Instead, you specify the name of that type in your app’s scene manifest along with rest of your app’s scene information. In a vehicle that supports instrument cluster content, CarPlay instantiates the scene and your delegate type at appropriate times using the information in the scene manifest. The following example shows the keys and values for an instrument cluster scene. The `MyInstrumentClusterSceneDelegate ` string is the name of an app-specific type that implements this protocol.

```plist
<key>CPSupportsInstrumentClusterNavigationScene</key>
<bool>YES</bool>
<key>CPTemplateApplicationInstrumentClusterSceneSessionRoleApplication</key>
<array>
    <dict>
        <!-- Specify the name of the scene class. -->
        <key>UISceneClassName</key>
        <string> CPTemplateApplicationInstrumentClusterScene </string>
        <key>UISceneConfigurationName</key>
        <string>MyInstrumentClusterSceneConfiguration</string>
        <key>UISceneDelegateClassName</key>
        <string>MyInstrumentClusterSceneDelegate</string>
    </dict>
</array>
```

When CarPlay connects a new scene to your app, use the information in the [`CPInstrumentClusterController`](./cpinstrumentclustercontroller.md) to configure your instrument cluster interface. The controller object contains the window you use to display your content and additional properties to consider when building your content.

For information about how to specify your app’s scene manifest, see [Specifying the scenes your app supports](../UIKit/specifying-the-scenes-your-app-supports.md).

## Topics

### Responding to the scene life-cycle changes
- [func templateApplicationInstrumentClusterScene(CPTemplateApplicationInstrumentClusterScene, didConnect: CPInstrumentClusterController)](./cptemplateapplicationinstrumentclusterscenedelegate/templateapplicationinstrumentclusterscene%28_,didconnect%29.md)
  Tells the delegate that CarPlay added an instrument cluster scene to your app.
- [func templateApplicationInstrumentClusterScene(CPTemplateApplicationInstrumentClusterScene, didDisconnectInstrumentClusterController: CPInstrumentClusterController)](./cptemplateapplicationinstrumentclusterscenedelegate/templateapplicationinstrumentclusterscene%28_,diddisconnectinstrumentclustercontroller%29.md)
  Tells the delegate about the removal of an instrument cluster scene from your app.
### Responding to appearance changes
- [func contentStyleDidChange(UIUserInterfaceStyle)](./cptemplateapplicationinstrumentclusterscenedelegate/contentstyledidchange%28_%29.md)
  Tells your app that the suggested content style for this scene changed.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UISceneDelegate](../UIKit/uiscenedelegate.md)

## See Also

### Instrument cluster display
- [class CPTemplateApplicationInstrumentClusterScene](./cptemplateapplicationinstrumentclusterscene.md)
  A CarPlay scene that presents navigation-related instructions in the vehicle’s instrument display.
- [class CPInstrumentClusterController](./cpinstrumentclustercontroller.md)
  The controller you use to configure and manage your instrument cluster interface.
- [protocol CPInstrumentClusterControllerDelegate](./cpinstrumentclustercontrollerdelegate.md)
  The methods for responding to changes to instrument cluster settings.
- [enum CPInstrumentClusterSetting](./cpinstrumentclustersetting.md)
  Constants that indicate when to include or exclude vehicle-related data in your custom content.
- [CPSupportsInstrumentClusterNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscenedelegate)*