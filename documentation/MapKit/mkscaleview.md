# MKScaleView

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface MKScaleView : UIView
```

#### Overview

Use this class when you want to incorporate a standard scale view into your own view hierarchy. A scale view displays a legend with distance information for its associated map view. As the map region changes, the scale view updates automatically to reflect any changes in scale.

## Topics

### Creating a scale view
- [convenience init(mapView: MKMapView?)](./mkscaleview/init%28mapview%29.md)
  Creates a scale view and associates it with the specified map view.
### Getting the scale view attributes
- [var mapView: MKMapView?](./mkscaleview/mapview.md)
  The map view that provides the scale information to the scale view.
- [var scaleVisibility: MKFeatureVisibility](./mkscaleview/scalevisibility.md)
  The visibility of the scale view.
- [var legendAlignment: MKScaleView.Alignment](./mkscaleview/legendalignment.md)
  The alignment of the distance information in the scale view.
- [MKScaleView.Alignment](./mkscaleview/alignment.md)
  Constants that indicate how the framework should align measurements.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
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

### Map customization
- [class MKMapCamera](./mkmapcamera.md)
  A virtual camera for defining the appearance of the map.
- [class MKCompassButton](./mkcompassbutton.md)
  A specialized view that displays the compass heading for its associated map.
- [class MKZoomControl](./mkzoomcontrol.md)
  A specialized view that displays and controls the zoom level of the map view.
- [class MKPitchControl](./mkpitchcontrol.md)
  A specialized view that displays and controls the pitch angle of the map view.
- [class MKUserTrackingButton](./mkusertrackingbutton.md)
  A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [class MKUserTrackingBarButtonItem](./mkusertrackingbarbuttonitem.md)
  A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview)*