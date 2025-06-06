# mapView(_:regionDidChangeAnimated:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the region the map view is displaying changes.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool)
```

#### Discussion

The map view calls this method at the end of a change to the map’s visible region.

## Parameters

- `mapView`: The map view with the visible region that changes.
- `animated`: If  , the map view animates the change to the new region.

## See Also

- [func mapView(MKMapView, regionWillChangeAnimated: Bool)](mkmapviewdelegate/mapview(_:regionwillchangeanimated:).md)
  Tells the delegate when the region the map view is displaying is about to change.
- [func mapViewDidChangeVisibleRegion(MKMapView)](mkmapviewdelegate/mapviewdidchangevisibleregion(_:).md)
  Tells the delegate when the map view’s visible region changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:regiondidchangeanimated:))*