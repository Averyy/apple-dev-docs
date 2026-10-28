# MKOverlayPathView

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

Represents a generic overlay that draws its contents using a Core Graphics path data type.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use MKOverlayPathRenderer

## Declaration

```swift
class MKOverlayPathView
```

```objc
@interface MKOverlayPathView : MKOverlayView
```

## Overview

You can use this class to implement simple path-based overlay views or subclass it to define additional drawing behaviors. The default drawing behavior of this class is to apply the object’s current fill attributes, fill the path, apply the current stroke attributes, and then stroke the path.

If you subclass, you should override the [`createPath`](./mkoverlaypathview/createpath.md) method and use that method to build the appropriate path for the overlay. You can invalidate this path as needed and force the path to be recreated using whatever new data your subclass has obtained.

In iOS 7 and later, use the [`MKOverlayPathRenderer`](./mkoverlaypathrenderer.md) class to display path-based overlays instead.

## Topics

### Accessing the drawing attributes
- [fillColor](./mkoverlaypathview/fillcolor.md)
  The fill color to use for the path.
- [strokeColor](./mkoverlaypathview/strokecolor.md)
  The stroke color to use for the path.
- [lineWidth](./mkoverlaypathview/linewidth.md)
  The stroke width to use for the path.
- [lineJoin](./mkoverlaypathview/linejoin.md)
  The line join style to apply to corners of the path.
- [lineCap](./mkoverlaypathview/linecap.md)
  The line cap style to apply to the open ends of the path.
- [miterLimit](./mkoverlaypathview/miterlimit.md)
  The limiting value that helps avoid spikes at junctions between connected line segments.
- [lineDashPhase](./mkoverlaypathview/linedashphase.md)
  The offset (in points) at which to start drawing the dash pattern.
- [lineDashPattern](./mkoverlaypathview/linedashpattern.md)
  An array of numbers indicating the dash pattern for paths.
### Creating and managing the path
- [path](./mkoverlaypathview/path.md)
  The current path to use when drawing the overlay.
- [- createPath](./mkoverlaypathview/createpath.md)
  Creates the path for the overlay.
- [- invalidatePath](./mkoverlaypathview/invalidatepath.md)
  Releases the path associated with the receiver.
### Drawing the Path
- [- applyStrokePropertiesToContext:atZoomScale:](./mkoverlaypathview/applystrokepropertiestocontext_atzoomscale_.md)
  Applies the receiver’s current stroke-related drawing properties to the specified graphics context.
- [- applyFillPropertiesToContext:atZoomScale:](./mkoverlaypathview/applyfillpropertiestocontext_atzoomscale_.md)
  Applies the receiver’s current fill-related drawing properties to the specified graphics context
- [- strokePath:inContext:](./mkoverlaypathview/strokepath_incontext_.md)
  Draws a line along the specified path.
- [- fillPath:inContext:](./mkoverlaypathview/fillpath_incontext_.md)
  Fills the area enclosed by the specified path.

## Relationships

### Inherits From
- [MKOverlayView](./mkoverlayview.md)
### Inherited By
- [MKCircleView](./mkcircleview.md)
- [MKPolygonView](./mkpolygonview.md)
- [MKPolylineView](./mkpolylineview.md)
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
- [class MKOverlayView](./mkoverlayview.md)
  Defines the basic behavior associated with all overlay views.
- [class MKPolygonView](./mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](./mkpolygon.md) annotation object.
- [class MKPolylineView](./mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](./mkpolyline.md) annotation object.
- [class MKPinAnnotationView](./mkpinannotationview.md)
  An annotation view that displays a pin image on the map.
- [MKReverseGeocoder](./mkreversegeocoder.md)
  Provides services for converting a map coordinate (specified as a latitude/longitude pair) into information about that coordinate, such as the country or region, city, or street.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlaypathview)*