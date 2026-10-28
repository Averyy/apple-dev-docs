# MKCompassButton

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A specialized view that displays the compass heading for its associated map.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MKCompassButton
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@interface MKCompassButton : UIView
```

*macOS*

```objc
@interface MKCompassButton : NSView
```

## Overview

Use this class when you want to incorporate a standard compass button into your own view hierarchy. A compass button reflects the current orientation of its associated map view. Tapping the compass button reorients the map so that due north is at the top of the map view.

## Topics

### Creating a compass button
- [convenience init(mapView: MKMapView?)](./mkcompassbutton/init%28mapview%29.md)
  Creates a compass button and associates it with the specified map view.
### Getting the compass attributes
- [var mapView: MKMapView?](./mkcompassbutton/mapview.md)
  The map view that provides the heading information for the compass button.
- [var compassVisibility: MKFeatureVisibility](./mkcompassbutton/compassvisibility.md)
  The visibility of the compass button.
- [enum MKFeatureVisibility](./mkfeaturevisibility.md)
  Constants that indicate the visibility of different map features.

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
- [class MKScaleView](./mkscaleview.md)
  A specialized view that displays the scale information for its associated map.
- [class MKZoomControl](./mkzoomcontrol.md)
  A specialized view that displays and controls the zoom level of the map view.
- [class MKPitchControl](./mkpitchcontrol.md)
  A specialized view that displays and controls the pitch angle of the map view.
- [class MKUserTrackingButton](./mkusertrackingbutton.md)
  A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.
- [class MKUserTrackingBarButtonItem](./mkusertrackingbarbuttonitem.md)
  A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcompassbutton)*