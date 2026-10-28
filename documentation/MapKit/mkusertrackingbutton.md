# MKUserTrackingButton

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MKUserTrackingButton
```

```objc
@interface MKUserTrackingButton : UIView
```

## Overview

Use this class when you need a standard button that you can incorporate into your view hierarchy. Tapping the button lets the user toggles between modes for displaying the map with and without the current heading applied. The button also reflects the current user tracking mode if set elsewhere.

## Topics

### Creating a user tracking button
- [convenience init(mapView: MKMapView?)](./mkusertrackingbutton/init%28mapview%29.md)
  Initializes the button with the map view that it should control.
### Getting the parent map
- [var mapView: MKMapView?](./mkusertrackingbutton/mapview.md)
  The map view associated with the button.

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
- [class MKScaleView](./mkscaleview.md)
  A specialized view that displays the scale information for its associated map.
- [class MKZoomControl](./mkzoomcontrol.md)
  A specialized view that displays and controls the zoom level of the map view.
- [class MKPitchControl](./mkpitchcontrol.md)
  A specialized view that displays and controls the pitch angle of the map view.
- [class MKUserTrackingBarButtonItem](./mkusertrackingbarbuttonitem.md)
  A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkusertrackingbutton)*