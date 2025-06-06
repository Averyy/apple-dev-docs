# MKMarkerAnnotationView

**Framework**: MapKit  
**Kind**: class

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
@MainActor
class MKMarkerAnnotationView
```

#### Overview

Return an instance of this class from the [`mapView(_:viewFor:)`](mkmapviewdelegate/mapview(_:viewfor:)-8humz.md) method of your map view delegate when you want to display the same types of markers used in the Maps app.

The default [`displayPriority`](mkannotationview/displaypriority.md) for an instance of this class is [`defaultLow`](mkfeaturedisplaypriority/defaultlow.md).

## Topics

### Setting the Marker Color
- [var markerTintColor: UIColor?](mkmarkerannotationview/markertintcolor.md)
  The background color of the marker balloon.
### Setting the Marker Content
- [var glyphText: String?](mkmarkerannotationview/glyphtext.md)
  The text to display in the marker balloon.
- [var glyphImage: UIImage?](mkmarkerannotationview/glyphimage.md)
  An image to display in the marker balloon.
- [var glyphTintColor: UIColor?](mkmarkerannotationview/glyphtintcolor.md)
  The color to apply to the glyph text or image.
- [var selectedGlyphImage: UIImage?](mkmarkerannotationview/selectedglyphimage.md)
  An image to display when the user selects the marker.
### Setting the Visibility
- [var titleVisibility: MKFeatureVisibility](mkmarkerannotationview/titlevisibility.md)
  The visibility of the title text rendered beneath the marker balloon.
- [var subtitleVisibility: MKFeatureVisibility](mkmarkerannotationview/subtitlevisibility.md)
  The visibility of the subtitle text rendered beneath the marker balloon.
- [enum MKFeatureVisibility](mkfeaturevisibility.md)
  Constants that indicate the visibility of different map features.
### Animating the Marker onto the Screen
- [var animatesWhenAdded: Bool](mkmarkerannotationview/animateswhenadded.md)
  A Boolean that indicates whether the marker animates into position onscreen.

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

- [Annotating a Map with Custom Data](annotating-a-map-with-custom-data.md)
  Annotate a map with location-specific data using default and customized annotation views and callouts.
- [class MKPointAnnotation](mkpointannotation.md)
  A string-based piece of location-specific data that you apply to a specific point on a map.
- [class MKMapItemAnnotation](mkmapitemannotation.md)
  An annotation that represents a map item
- [class MKPinAnnotationView](mkpinannotationview.md)
  An annotation view that displays a pin image on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview)*