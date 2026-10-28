# MKOverlayView

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

Defines the basic behavior associated with all overlay views.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use MKOverlayRenderer

## Declaration

```swift
class MKOverlayView
```

```objc
@interface MKOverlayView : UIView
```

## Overview

An overlay view provides the visual representation of an overlay object—that is, an object that conforms to the [`MKOverlay`](./mkoverlay.md) protocol. This class defines the drawing infrastructure used by the map view but does not do any actual drawing. Subclasses are expected to override the [`drawMapRect:zoomScale:inContext:`](./mkoverlayview/drawmaprect_zoomscale_incontext_.md) method in order to draw the contents of the overlay view.

The Map Kit framework provides several concrete instances of overlay views. Specifically, it provides overlay views for each of the concrete overlay objects. You can use one of these existing overlay views or define your own subclass if you want to draw the overlay contents differently.

In iOS 7 and later, use the [`MKOverlayRenderer`](./mkoverlayrenderer.md) class to display overlays instead.

### Subclassing notes

You can subclass `MKOverlayView` to create overlays based on custom shapes and content. The only method subclasses are expected to override is the [`drawMapRect:zoomScale:inContext:`](./mkoverlayview/drawmaprect_zoomscale_incontext_.md) method. However, if your class contains content that may not be ready for drawing right away, you should also override the [`canDrawMapRect:zoomScale:`](./mkoverlayview/candrawmaprect_zoomscale_.md) method and use it to report when your class is ready and able to draw.

The implementation of your [`drawMapRect:zoomScale:inContext:`](./mkoverlayview/drawmaprect_zoomscale_incontext_.md) method must be safe to run from multiple threads simultaneously. To improve performance, the map view may tile overlays that are large enough and distribute the rendering of each tile to separate threads.

## Topics

### Initializing an overlay view
- [- initWithOverlay:](./mkoverlayview/initwithoverlay_.md)
  Initializes and returns the overlay view and associates it with the specified overlay object.
### Attributes of the overlay
- [overlay](./mkoverlayview/overlay.md)
  The overlay object containing the data for drawing.
### Converting points on the map
- [- pointForMapPoint:](./mkoverlayview/pointformappoint_.md)
  Returns the point in the overlay view that corresponds to specified point on the map.
- [- mapPointForPoint:](./mkoverlayview/mappointforpoint_.md)
  Returns the map point that corresponds to the specified point in the overlay view.
- [- rectForMapRect:](./mkoverlayview/rectformaprect_.md)
  Returns the rectangle in the overlay view that corresponds to the specified rectangle on the map.
- [- mapRectForRect:](./mkoverlayview/maprectforrect_.md)
  Returns the map rectangle that corresponds to the rectangle in the overlay view’s coordinate system.
### Drawing the overlay
- [- canDrawMapRect:zoomScale:](./mkoverlayview/candrawmaprect_zoomscale_.md)
  Returns a Boolean value indicating whether the overlay view is ready to draw its content.
- [- drawMapRect:zoomScale:inContext:](./mkoverlayview/drawmaprect_zoomscale_incontext_.md)
  Draws the contents of the overlay view.
- [- setNeedsDisplayInMapRect:](./mkoverlayview/setneedsdisplayinmaprect_.md)
  Invalidates the view in the given map rectangle at all zoom scales.
- [- setNeedsDisplayInMapRect:zoomScale:](./mkoverlayview/setneedsdisplayinmaprect_zoomscale_.md)
  Invalidates the view in the given map rectangle but only at the specified zoom scale.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Inherited By
- [MKOverlayPathView](./mkoverlaypathview.md)
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

### Classes
- [class MKCircleView](./mkcircleview.md)
  Provides the visual representation for an [`MKCircle`](./mkcircle.md) annotation object.
- [class MKOverlayPathView](./mkoverlaypathview.md)
  Represents a generic overlay that draws its contents using a Core Graphics path data type.
- [class MKPolygonView](./mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](./mkpolygon.md) annotation object.
- [class MKPolylineView](./mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](./mkpolyline.md) annotation object.
- [class MKPinAnnotationView](./mkpinannotationview.md)
  An annotation view that displays a pin image on the map.
- [MKReverseGeocoder](./mkreversegeocoder.md)
  Provides services for converting a map coordinate (specified as a latitude/longitude pair) into information about that coordinate, such as the country or region, city, or street.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayview)*