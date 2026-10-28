# MKPitchControl

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A specialized view that displays and controls the pitch angle of the map view.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
class MKPitchControl
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@interface MKPitchControl : UIView
```

*macOS*

```objc
@interface MKPitchControl : NSView
```

## Overview

Use this class when you want to incorporate a standard, fixed-size pitch control into your own view hierarchy. A pitch control allows the user to change the pitch angle of its associated map view.

## Topics

### Creating a pitch control
- [convenience init(mapView: MKMapView?)](./mkpitchcontrol/init%28mapview%29.md)
  Creates a pitch control and associates it with the specified map view.
### Accessing the map view
- [var mapView: MKMapView?](./mkpitchcontrol/mapview.md)
  The map view associated with this control.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
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

### Map customization
- [class MKMapCamera](./mkmapcamera.md)
  A virtual camera for defining the appearance of the map.
- [class MKCompassButton](./mkcompassbutton.md)
  A specialized view that displays the compass heading for its associated map.
- [class MKScaleView](./mkscaleview.md)
  A specialized view that displays the scale information for its associated map.
- [class MKZoomControl](./mkzoomcontrol.md)
  A specialized view that displays and controls the zoom level of the map view.
- [class MKUserTrackingButton](./mkusertrackingbutton.md)
  A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [class MKUserTrackingBarButtonItem](./mkusertrackingbarbuttonitem.md)
  A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpitchcontrol)*