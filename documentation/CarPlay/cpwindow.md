# CPWindow

**Framework**: CarPlay  
**Kind**: class

A window that displays its content on the CarPlay screen.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class CPWindow
```

#### Overview

Navigation apps use a window to render their maps, and CarPlay provides one via the scene delegate’s [`templateApplicationScene(_:didConnect:to:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md) method. For all other categories of apps, you use templates exclusively to draw your user interface, and your scene delegate must implement [`templateApplicationScene(_:didConnect:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md) instead.

When CarPlay launches your navigation app, instantiate your map-drawing view controller and assign it to the window’s [`rootViewController`](https://developer.apple.com/documentation/UIKit/UIWindow/rootViewController) property. This becomes the base CarPlay view and is for drawing maps exclusively. You use templates for all other user interface elements.

The base view of a navigation app does not receive tap or drag events.

## Topics

### Accessing the Scene
- [var templateApplicationScene: CPTemplateApplicationScene?](cpwindow/templateapplicationscene.md)
  The application scene that contains the window.
### Layout
- [var mapButtonSafeAreaLayoutGuide: UILayoutGuide](cpwindow/mapbuttonsafearealayoutguide.md)
  The layout guide that represents the portion of the map template that map buttons don’t obscure.

## Relationships

### Inherits From
- [UIWindow](../UIKit/UIWindow.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [var carWindow: CPWindow](cptemplateapplicationscene/carwindow.md)
  The window that belongs to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpwindow)*