# MKPinAnnotationView

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

An annotation view that displays a pin image on the map.

**Availability**:
- iOS 3.0+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- iPadOS 3.0+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- Mac Catalyst 13.1+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- macOS 10.9+ - Deprecated in 13.0 (renamed: MKMarkerAnnotationView)
- tvOS 9.2+ - Deprecated in 16.0 (renamed: MKMarkerAnnotationView)
- visionOS 1.0+ - Deprecated in 1.0 (renamed: MKMarkerAnnotationView)

> **Deprecated**: In iOS 16 and macOS 13 and later use an [`MKAnnotationView`](./mkannotationview.md) to create a custom map annotation

## Declaration

```swift
class MKPinAnnotationView
```

```objc
@interface MKPinAnnotationView : MKAnnotationView
```

#### Overview

Return instances of this class from the [`mapView(_:viewFor:)`](./mkmapviewdelegate/mapview%28_,viewfor%29-8humz.md) method of your map view delegate when you want to display a pin for one of your annotations. The pins displayed by this view are the same ones found in the Maps application. You can specify the type of pin you want to display and whether you want the pin to be animated into place.

> **Note**:  In iOS 5.1 and earlier, the MapKit framework uses the Google Mobile Maps (GMM) service to provide map data. Use of specific classes of this framework (and their associated interfaces) is subject to the Google Mobile Maps terms of service, found at [http://code.google.com/apis/maps/iphone/terms.html](http://code.google.com/apis/maps/iphone/terms.html).

## Topics

### Getting Standard Pin Colors
- [class func redPinColor() -> UIColor](./mkpinannotationview/redpincolor%28%29.md)
  Returns the standard color for red pins.
- [class func greenPinColor() -> UIColor](./mkpinannotationview/greenpincolor%28%29.md)
  Returns the standard color for green pins.
- [class func purplePinColor() -> UIColor](./mkpinannotationview/purplepincolor%28%29.md)
  Returns the standard color for purple pins.
- [enum MKPinAnnotationColor](./mkpinannotationcolor.md)
  The supported colors for pin annotations.
### Getting and Setting Attributes
- [var pinTintColor: UIColor!](./mkpinannotationview/pintintcolor.md)
  The color of the pin head.
- [var animatesDrop: Bool](./mkpinannotationview/animatesdrop.md)
  A Boolean value indicating whether the annotation view is animated onto the screen.
- [var pinColor: MKPinAnnotationColor](./mkpinannotationview/pincolor.md)
  The color of the pin head.

## Relationships

### Inherits From
- [MKAnnotationView](./mkannotationview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
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
- [class MKOverlayPathView](./mkoverlaypathview.md)
  Represents a generic overlay that draws its contents using a Core Graphics path data type.
- [class MKPolygonView](./mkpolygonview.md)
  Provides the visual representation for an [`MKPolygon`](./mkpolygon.md) annotation object.
- [class MKPolylineView](./mkpolylineview.md)
  Provides the visual representation for an [`MKPolyline`](./mkpolyline.md) annotation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpinannotationview)*