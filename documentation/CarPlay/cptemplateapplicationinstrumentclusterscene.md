# CPTemplateApplicationInstrumentClusterScene

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A CarPlay scene that presents navigation-related instructions in the vehicle’s instrument display.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+

## Declaration

```swift
class CPTemplateApplicationInstrumentClusterScene
```

```objc
@interface CPTemplateApplicationInstrumentClusterScene : UIScene
```

## Overview

A `CPTemplateApplicationInstrumentClusterScene` object manages the content that appears in a vehicle’s instrument cluster display. When you implement a navigation app, add support for this scene type to your app and use it to display navigation-related details. For example, you might use it to display upcoming maneuvers, arrival times, or other information. The scene provides the interface controller you use to display your content and reports scene-related events to its associated delegate object.

You don’t create a `CPTemplateApplicationInstrumentClusterScene ` object directly. Instead, you specify the type name in your app’s scene manifest along with other information about the scene such as the type of its associated delegate object. In a vehicle with an instrument cluster display, CarPlay instantiates the scene and delegate types at appropriate times using the information in the scene manifest. The following example shows the keys and values for an instrument cluster scene. The [`UISceneClassName`](../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication/uisceneclassname.md) key contains the name of this scene class. The [`CPSupportsInstrumentClusterNavigationScene`](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md) key tells CarPlay that your app supports this type of scene.

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

At the start of a session, the system delivers a [`CPInstrumentClusterController`](./cpinstrumentclustercontroller.md) object to the delegate’s `CPTemplateApplicationSceneDelegate/instrumentClusterControllerDidConnect(_:)` method. You can also retrieve this object from the scene’s `CPTemplateApplicationScene/instrumentClusterController ` property at any time. Use this controller object to present the instrument cluster content.

## Topics

### Managing the scene’s interface
- [var instrumentClusterController: CPInstrumentClusterController](./cptemplateapplicationinstrumentclusterscene/instrumentclustercontroller.md)
  The controller object you use to present your map content in the instrument cluster.
- [var contentStyle: UIUserInterfaceStyle](./cptemplateapplicationinstrumentclusterscene/contentstyle.md)
  The current interface style for the instrument-cluster content.
### Responding to scene life-cycle events
- [var delegate: (any CPTemplateApplicationInstrumentClusterSceneDelegate)?](./cptemplateapplicationinstrumentclusterscene/delegate.md)
  The custom object you provide to handle scene’s life-cycle events.
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](./cptemplateapplicationinstrumentclusterscenedelegate.md)
  The methods for responding to the life cycle events in your app’s instrument cluster scene.

## Relationships

### Inherits From
- [UIScene](../UIKit/uiscene.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Instrument cluster display
- [protocol CPTemplateApplicationInstrumentClusterSceneDelegate](./cptemplateapplicationinstrumentclusterscenedelegate.md)
  The methods for responding to the life cycle events in your app’s instrument cluster scene.
- [class CPInstrumentClusterController](./cpinstrumentclustercontroller.md)
  The controller you use to configure and manage your instrument cluster interface.
- [protocol CPInstrumentClusterControllerDelegate](./cpinstrumentclustercontrollerdelegate.md)
  The methods for responding to changes to instrument cluster settings.
- [enum CPInstrumentClusterSetting](./cpinstrumentclustersetting.md)
  Constants that indicate when to include or exclude vehicle-related data in your custom content.
- [CPSupportsInstrumentClusterNavigationScene](../BundleResources/information-property-list/uiapplicationscenemanifest/cpsupportsinstrumentclusternavigationscene.md)
  A Boolean value that indicates whether your app supports displaying navigation content in the CarPlay Instrument Cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationinstrumentclusterscene)*