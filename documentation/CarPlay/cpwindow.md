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
class CPWindow
```

#### Overview

Navigation apps use a window to render their maps, and CarPlay provides one via the scene delegate’s [`templateApplicationScene(_:didConnect:to:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:to:).md) method. For all other categories of apps, you use templates exclusively to draw your user interface, and your scene delegate must implement [`templateApplicationScene(_:didConnect:)`](cptemplateapplicationscenedelegate/templateapplicationscene(_:didconnect:).md) instead.

When CarPlay launches your navigation app, instantiate your map-drawing view controller and assign it to the window’s [`rootViewController`](https://developer.apple.com/documentation/uikit/uiwindow/rootviewcontroller) property. This becomes the base CarPlay view and is for drawing maps exclusively. You use templates for all other user interface elements.

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
- [UIWindow](../uikit/uiwindow.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [var carWindow: CPWindow](cptemplateapplicationscene/carwindow.md)
  The window that belongs to the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpwindow)*