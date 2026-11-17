# CPTemplateApplicationScene

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A CarPlay scene that manages your app’s interface on the vehicle’s center display.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPTemplateApplicationScene
```

```objc
@interface CPTemplateApplicationScene : UIScene
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

The `CPTemplateApplicationScene` class is an extension of the [`UIScene`](../UIKit/uiscene.md) type, and it manages an instance of your app’s CarPlay interface. Scenes serve as the main entry point to your CarPlay app. When someone launches your app from their vehicle, CarPlay starts a session and creates your app’s main scene. During the session, use the scene object to retrieve the interface controller you need to create your app’s interface.

You don’t create a `CPTemplateApplicationScene` object directly. Instead, you specify the type name in your app’s scene manifest, along with other information about the scene such as the type of its associated delegate object. When someone launches your app, CarPlay instantiates the scene and delegate types using the information in the scene manifest. The following example shows the keys and values from an app’s main CarPlay scene. The [`UISceneClassName`](../BundleResources/information-property-list/uiapplicationscenemanifest/uisceneconfigurations/cptemplateapplicationinstrumentclusterscenesessionroleapplication/uisceneclassname.md) key contains the name of this scene class.

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

At the start of a session, the system delivers a [`CPInterfaceController`](./cpinterfacecontroller.md) object to the delegate’s [`templateApplicationScene(_:didConnect:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) or [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method. You can also retrieve this object from the scene’s [`interfaceController`](./cptemplateapplicationscene/interfacecontroller.md) property at any time. Use this controller object to present the content for your app’s interface. If you’re creating a navigation app, you also need to present your map content using the scene’s window object.

For information about how to specify your app’s scene manifest, see [Specifying the scenes your app supports](../UIKit/specifying-the-scenes-your-app-supports.md).

## Topics

### Getting the interface controller
- [var interfaceController: CPInterfaceController](./cptemplateapplicationscene/interfacecontroller.md)
  The controller object you use to present your app’s interface.
### Responding to scene life-cycle events
- [var delegate: (any CPTemplateApplicationSceneDelegate)?](./cptemplateapplicationscene/delegate.md)
  The custom object you provide to handle scene’s life-cycle events.
- [protocol CPTemplateApplicationSceneDelegate](./cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.
### Accessing the scene’s window
- [var carWindow: CPWindow](./cptemplateapplicationscene/carwindow.md)
  The window that displays the scene’s content.
### Getting the interface style
- [var contentStyle: UIUserInterfaceStyle](./cptemplateapplicationscene/contentstyle.md)
  The current interface style for your app’s content.

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

### App management
- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)
  Build the interface for your CarPlay app using scenes and templates from the CarPlay framework.
- [protocol CPTemplateApplicationSceneDelegate](./cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.
- [class CPInterfaceController](./cpinterfacecontroller.md)
  The type you use to present your app’s CarPlay interface and change what appears on the vehicle’s display.
- [class CPSessionConfiguration](./cpsessionconfiguration.md)
  An object that keeps you informed of changes to the CarPlay environment.
- [class CPWindow](./cpwindow.md)
  A type that navigation apps use to present their map content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cptemplateapplicationscene)*