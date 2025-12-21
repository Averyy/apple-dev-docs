# MKPinAnnotationView

**Framework**: MapKit  
**Kind**: class

An annotation view that displays a pin image on the map.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MKPinAnnotationView
```

#### Overview

Return instances of this class from the [`mapView(_:viewFor:)`](mkmapviewdelegate/mapview(_:viewfor:)-8humz.md) method of your map view delegate when you want to display a pin for one of your annotations. The pins displayed by this view are the same ones found in the Maps application. You can specify the type of pin you want to display and whether you want the pin to be animated into place.

> **Note**:  In iOS 5.1 and earlier, the MapKit framework uses the Google Mobile Maps (GMM) service to provide map data. Use of specific classes of this framework (and their associated interfaces) is subject to the Google Mobile Maps terms of service, found at [`http://code.google.com/apis/maps/iphone/terms.html`](https://developer.apple.comhttp://code.google.com/apis/maps/iphone/terms.html).

## Topics

### Getting Standard Pin Colors
- [class func redPinColor() -> UIColor](mkpinannotationview/redpincolor.md)
  Returns the standard color for red pins.
- [class func greenPinColor() -> UIColor](mkpinannotationview/greenpincolor.md)
  Returns the standard color for green pins.
- [class func purplePinColor() -> UIColor](mkpinannotationview/purplepincolor.md)
  Returns the standard color for purple pins.
- [enum MKPinAnnotationColor](mkpinannotationcolor.md)
  The supported colors for pin annotations.
### Getting and Setting Attributes
- [var pinTintColor: UIColor!](mkpinannotationview/pintintcolor.md)
  The color of the pin head.
- [var animatesDrop: Bool](mkpinannotationview/animatesdrop.md)
  A Boolean value indicating whether the annotation view is animated onto the screen.
- [var pinColor: MKPinAnnotationColor](mkpinannotationview/pincolor.md)
  The color of the pin head.

## Relationships

### Inherits From
- [MKAnnotationView](mkannotationview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
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
- [class MKPolylineView](mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](mkpolyline.md) annotation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpinannotationview)*