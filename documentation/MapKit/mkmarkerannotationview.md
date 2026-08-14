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
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
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