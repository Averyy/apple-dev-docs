# CPWindow

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A type that navigation apps use to present their map content.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class CPWindow
```

```objc
@interface CPWindow : UIWindow
```

## Mentions

- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)

## Overview

The `CPWindow` type provides navigation apps with the environment for displaying their map imagery. When implementing a navigation app, fetch this type and assign a view controller with your map content to the window’s [`rootViewController`](../UIKit/uiwindow/rootviewcontroller.md) property. For the rest of your navigation app’s content, present templates using the [`CPInterfaceController`](./cpinterfacecontroller.md) object of your app’s main scene. If you’re not implementing a navigation app, don’t use this type at all.

You don’t create `CPWindow` objects directly. When CarPlay creates the scene for your navigation app, it creates a window object and delivers it to the [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method of your scene delegate. In that method, configure a view controller with your map content and assign it as the window’s root view controller. The window provides a layout guide for its *safe area*, which you use to ensure important content remains visible. If you need to change your content, you can access the window from the scene’s [`carWindow`](./cptemplateapplicationscene/carwindow.md) property.

CarPlay doesn’t deliver tap or drag events to the view controller you associate with a `CPWindow` object. All interactions with your map content occur through the [`CPMapTemplate`](./cpmaptemplate.md) type you add as the root template of your app’s interface. When interactions occur, the map template reports them to its delegate object. Implement a custom type that adopts the [`CPMapTemplateDelegate`](./cpmaptemplatedelegate.md) protocol to receive the data you need to update your view controller’s content.

## Topics

### Getting the CarPlay scene
- [var templateApplicationScene: CPTemplateApplicationScene?](./cpwindow/templateapplicationscene.md)
  The scene associated with the window.
### Getting the layout guide
- [var mapButtonSafeAreaLayoutGuide: UILayoutGuide](./cpwindow/mapbuttonsafearealayoutguide.md)
  A layout guide that represents the portion of the window unobscured by other content.

## Relationships

### Inherits From
- [UIWindow](../UIKit/uiwindow.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### App management
- [Building your app’s initial CarPlay interface](./building-your-apps-initial-carplay-interface.md)
  Build the interface for your CarPlay app using scenes and templates from the CarPlay framework.
- [class CPTemplateApplicationScene](./cptemplateapplicationscene.md)
  A CarPlay scene that manages your app’s interface on the vehicle’s center display.
- [protocol CPTemplateApplicationSceneDelegate](./cptemplateapplicationscenedelegate.md)
  Methods for responding to  life-cycle events in your app’s scene.
- [class CPInterfaceController](./cpinterfacecontroller.md)
  The type you use to present your app’s CarPlay interface and change what appears on the vehicle’s display.
- [class CPSessionConfiguration](./cpsessionconfiguration.md)
  An object that keeps you informed of changes to the CarPlay environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpwindow)*