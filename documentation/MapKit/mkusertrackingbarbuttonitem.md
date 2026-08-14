# MKUserTrackingBarButtonItem

**Framework**: MapKit  
**Kind**: class

A specialized bar button item that allows the user to toggle whether the map tracks to the heading the user is facing.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class MKUserTrackingBarButtonItem
```

#### Overview

Tapping the button lets the user toggles between modes for displaying the map with and without the current heading applied. The button also reflects the current user tracking mode if set elsewhere. This bar button item is associated to a single map view.

## Topics

### Creating a user tracking bar button item
- [init(mapView: MKMapView?)](mkusertrackingbarbuttonitem/init(mapview:).md)
  Initializes a newly created bar button item with the specified map view.
### Accessing the owning map
- [var mapView: MKMapView?](mkusertrackingbarbuttonitem/mapview.md)
  The map view associated with this bar button item.

## Relationships

### Inherits From
- [UIBarButtonItem](../uikit/uibarbuttonitem.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UISpringLoadedInteractionSupporting](../uikit/uispringloadedinteractionsupporting.md)

## See Also

- [class MKMapCamera](mkmapcamera.md)
  A virtual camera for defining the appearance of the map.
- [class MKCompassButton](mkcompassbutton.md)
  A specialized view that displays the compass heading for its associated map.
- [class MKScaleView](mkscaleview.md)
  A specialized view that displays the scale information for its associated map.
- [class MKZoomControl](mkzoomcontrol.md)
  A specialized view that displays and controls the zoom level of the map view.
- [class MKPitchControl](mkpitchcontrol.md)
  A specialized view that displays and controls the pitch angle of the map view.
- [class MKUserTrackingButton](mkusertrackingbutton.md)
  A specialized button that allows the user to toggle whether the map tracks to the heading the user is facing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkusertrackingbarbuttonitem)*