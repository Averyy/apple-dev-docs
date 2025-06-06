# init(mapView:)

**Framework**: MapKit  
**Kind**: init

Creates a scale view and associates it with the specified map view.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(mapView: MKMapView?)
```

#### Return Value

An initialized scale view.

## Parameters

- `mapView`: The map to associate with the scale view. The scale view automatically updates to reflect the scale of this map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkscaleview/init(mapview:))*