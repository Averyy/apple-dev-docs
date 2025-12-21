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
@MainActor
class MKPolylineView
```

#### Overview

This view strokes the path represented by the annotation. (This class does not fill the area enclosed by the path.) You can change the color and other drawing attributes of the path by modifying the properties inherited from the [`MKOverlayPathView`](mkoverlaypathview.md) class. This class is typically used as is and not subclassed.

In iOS 7 and later, use the [`MKPolylineRenderer`](mkpolylinerenderer.md) class to display polyline overlays instead.

## Relationships

### Inherits From
- [MKOverlayPathView](mkoverlaypathview.md)
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