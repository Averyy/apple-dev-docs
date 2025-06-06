# init(mapView:)

**Framework**: MapKit  
**Kind**: init

Initializes the button with the map view that it should control.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(mapView: MKMapView?)
```

#### Return Value

An initialized [`MKUserTrackingButton`](mkusertrackingbutton.md) object.

## Parameters

- `mapView`: The mapView to associate with the button. Taps on the button change the appearance of this map view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkusertrackingbutton/init(mapview:))*