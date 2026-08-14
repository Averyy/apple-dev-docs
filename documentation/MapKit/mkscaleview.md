# MKScaleView

**Framework**: MapKit  
**Kind**: class

A specialized view that displays the scale information for its associated map.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MKScaleView
```

#### Overview

Use this class when you want to incorporate a standard scale view into your own view hierarchy. A scale view displays a legend with distance information for its associated map view. As the map region changes, the scale view updates automatically to reflect any changes in scale.

## Topics

### Creating a scale view
- [convenience init(mapView: MKMapView?)](mkscaleview/init(mapview:).md)
  Creates a scale view and associates it with the specified map view.
### Getting the scale view attributes
- [var mapView: MKMapView?](mkscaleview/mapview.md)
  The map view that provides the scale information to the scale view.
- [var scaleVisibility: MKFeatureVisibility](mkscaleview/scalevisibility.md)
  The visibility of the scale view.
- [var legendAlignment: MKScaleView.Alignment](mkscaleview/legendalignment.md)
  The alignment of the distance information in the scale view.
- [MKScaleView.Alignment](mkscaleview/alignment.md)
  Constants that indicate how the framework should align measurements.

## Relationships

### Inherits From
- [UIView](../uikit/uiview.md)
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

- [class MKMapCamera](mkmapcamera.md)
  A virtual camera for defining the appearance of the map.
- [class MKCompassButton](mkcompassbutton.md)
  A specialized view that displays the compass heading for its associated map.
- [class MKZoomControl](mkzoomcontrol.md)
  A specialized view that displays and controls the zoom level of the map view.
- [class MKPitchControl](mkpitchcontrol.md)
  A specialized view that displays and controls the pitch angle of the map view.
- [class MKUserTrackingButton](mkusertrackingbutton.md)
  A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [class MKUserTrackingBarButtonItem](mkusertrackingbarbuttonitem.md)
  A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview)*