# MKCircleView

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

Provides the visual representation for an [`MKCircle`](./mkcircle.md) annotation object.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use MKCircleRenderer

## Declaration

```swift
class MKCircleView
```

```objc
@interface MKCircleView : MKOverlayPathView
```

## Overview

This view fills and strokes the circle represented by the annotation. You can change the color and other drawing attributes of the circle by modifying the properties inherited from the [`MKOverlayPathView`](./mkoverlaypathview.md) class. This class is typically used as is and not subclassed.

Use of this class is discouraged in iOS 7 and later. Use the [`MKCircleRenderer`](./mkcirclerenderer.md) class instead.

## Topics

### Initializing the overlay view
- [- initWithCircle:](./mkcircleview/initwithcircle_.md)
  Initializes and returns a new overlay view using the specified circle overlay object.
### Accessing the overlay
- [circle](./mkcircleview/circle.md)
  The circle overlay object that contains the information used to draw the overlay.

## Relationships

### Inherits From
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
- [class MKOverlayView](./mkoverlayview.md)
  Defines the basic behavior associated with all overlay views.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcircleview)*