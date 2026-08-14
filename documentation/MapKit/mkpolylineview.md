# MKPolylineView

**Framework**: MapKit  
**Kind**: class

Provides the visual representation for an [`MKPolyline`](mkpolyline.md) annotation object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
class MKPolylineView
```

#### Overview

This view strokes the path represented by the annotation. (This class does not fill the area enclosed by the path.) You can change the color and other drawing attributes of the path by modifying the properties inherited from the [`MKOverlayPathView`](mkoverlaypathview.md) class. This class is typically used as is and not subclassed.

In iOS 7 and later, use the [`MKPolylineRenderer`](mkpolylinerenderer.md) class to display polyline overlays instead.

## Relationships

### Inherits From
- [MKOverlayPathView](mkoverlaypathview.md)
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
- [class MKOverlayPathView](mkoverlaypathview.md)
  Represents a generic overlay that draws its contents using a Core Graphics path data type.
- [class MKPolygonView](mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](mkpolygon.md) annotation object.
- [class MKPinAnnotationView](mkpinannotationview.md)
  An annotation view that displays a pin image on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpolylineview)*