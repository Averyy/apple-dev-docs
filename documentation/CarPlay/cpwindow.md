# CPWindow

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

A window that displays its content on the CarPlay screen.

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

## Overview

Navigation apps use a window to render their maps, and CarPlay provides one via the scene delegate’s [`templateApplicationScene(_:didConnect:to:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect,to%29.md) method. For all other categories of apps, you use templates exclusively to draw your user interface, and your scene delegate must implement [`templateApplicationScene(_:didConnect:)`](./cptemplateapplicationscenedelegate/templateapplicationscene%28_,didconnect%29.md) instead.

When CarPlay launches your navigation app, instantiate your map-drawing view controller and assign it to the window’s [`rootViewController`](../UIKit/uiwindow/rootviewcontroller.md) property. This becomes the base CarPlay view and is for drawing maps exclusively. You use templates for all other user interface elements.

The base view of a navigation app does not receive tap or drag events.

## Topics

### Accessing the Scene
- [var templateApplicationScene: CPTemplateApplicationScene?](./cpwindow/templateapplicationscene.md)
  The application scene that contains the window.
### Layout
- [var mapButtonSafeAreaLayoutGuide: UILayoutGuide](./cpwindow/mapbuttonsafearealayoutguide.md)
  The layout guide that represents the portion of the map template that map buttons don’t obscure.

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

### Accessing the Window
- [var carWindow: CPWindow](./cptemplateapplicationscene/carwindow.md)
  The window that belongs to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpwindow)*