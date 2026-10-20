# MKMarkerAnnotationView

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

An annotation view that displays a balloon-shaped marker at the designated location.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MKMarkerAnnotationView
```

```objc
@interface MKMarkerAnnotationView : MKAnnotationView
```

#### Overview

Return an instance of this class from the [`mapView(_:viewFor:)`](./mkmapviewdelegate/mapview%28_,viewfor%29-8humz.md) method of your map view delegate when you want to display the same types of markers used in the Maps app.

The default [`displayPriority`](./mkannotationview/displaypriority.md) for an instance of this class is [`defaultLow`](./mkfeaturedisplaypriority/defaultlow.md).

## Topics

### Setting the Marker Color
- [var markerTintColor: UIColor?](./mkmarkerannotationview/markertintcolor.md)
  The background color of the marker balloon.
### Setting the Marker Content
- [var glyphText: String?](./mkmarkerannotationview/glyphtext.md)
  The text to display in the marker balloon.
- [var glyphImage: UIImage?](./mkmarkerannotationview/glyphimage.md)
  An image to display in the marker balloon.
- [var glyphTintColor: UIColor?](./mkmarkerannotationview/glyphtintcolor.md)
  The color to apply to the glyph text or image.
- [var selectedGlyphImage: UIImage?](./mkmarkerannotationview/selectedglyphimage.md)
  An image to display when the user selects the marker.
### Setting the Visibility
- [var titleVisibility: MKFeatureVisibility](./mkmarkerannotationview/titlevisibility.md)
  The visibility of the title text rendered beneath the marker balloon.
- [var subtitleVisibility: MKFeatureVisibility](./mkmarkerannotationview/subtitlevisibility.md)
  The visibility of the subtitle text rendered beneath the marker balloon.
- [enum MKFeatureVisibility](./mkfeaturevisibility.md)
  Constants that indicate the visibility of different map features.
### Animating the Marker onto the Screen
- [var animatesWhenAdded: Bool](./mkmarkerannotationview/animateswhenadded.md)
  A Boolean that indicates whether the marker animates into position onscreen.

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

### Location annotations
- [Annotating a Map with Custom Data](./annotating-a-map-with-custom-data.md)
  Annotate a map with location-specific data using default and customized annotation views and callouts.
- [class MKPointAnnotation](./mkpointannotation.md)
  A string-based piece of location-specific data that you apply to a specific point on a map.
- [class MKMapItemAnnotation](./mkmapitemannotation.md)
  An annotation that represents a map item
- [class MKPinAnnotationView](./mkpinannotationview.md)
  An annotation view that displays a pin image on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview)*