# init(mapView:)

**Framework**: MapKit  
**Kind**: init

Creates a compass button and associates it with the specified map view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(mapView: MKMapView?)
```

#### Return Value

An initialized compass button.

## Parameters

- `mapView`: The map to associate with the compass button. The compass button reflects the orientation of this map, and tapping the button reorients the map appropriately.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkcompassbutton/init(mapview:))*