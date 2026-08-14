# MKOverlayPathView

**Framework**: MapKit  
**Kind**: class

Represents a generic overlay that draws its contents using a Core Graphics path data type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MKOverlayPathView
```

#### Overview

You can use this class to implement simple path-based overlay views or subclass it to define additional drawing behaviors. The default drawing behavior of this class is to apply the object’s current fill attributes, fill the path, apply the current stroke attributes, and then stroke the path.

If you subclass, you should override the [`createPath`](mkoverlaypathview/createpath.md) method and use that method to build the appropriate path for the overlay. You can invalidate this path as needed and force the path to be recreated using whatever new data your subclass has obtained.

In iOS 7 and later, use the [`MKOverlayPathRenderer`](mkoverlaypathrenderer.md) class to display path-based overlays instead.

## Relationships

### Inherits From
- [MKOverlayView](mkoverlayview.md)
### Inherited By
- [MKCircleView](mkcircleview.md)
- [MKPolygonView](mkpolygonview.md)
- [MKPolylineView](mkpolylineview.md)
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

- [class MKCircleView](mkcircleview.md)
  Provides the visual representation for an [`MKCircle`](mkcircle.md) annotation object.
- [class MKOverlayView](mkoverlayview.md)
  Defines the basic behavior associated with all overlay views.
- [class MKPolygonView](mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](mkpolygon.md) annotation object.
- [class MKPolylineView](mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](mkpolyline.md) annotation object.
- [class MKPinAnnotationView](mkpinannotationview.md)
  An annotation view that displays a pin image on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview)*