# mapView(_:regionWillChangeAnimated:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the region the map view is displaying is about to change.

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
optional func mapView(_ mapView: MKMapView, regionWillChangeAnimated animated: Bool)
```

#### Discussion

The framework calls this method at the beginning of a change to the map’s visible region.

## Parameters

- `mapView`: The map view with the visible region that’s about to change.
- `animated`: If  , the map view animates the change to the new region. If  , the map view makes the change immediately.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [func mapViewDidChangeVisibleRegion(MKMapView)](mkmapviewdelegate/mapviewdidchangevisibleregion(_:).md)
  Tells the delegate when the map view’s visible region changes.
- [func mapView(MKMapView, regionDidChangeAnimated: Bool)](mkmapviewdelegate/mapview(_:regiondidchangeanimated:).md)
  Tells the delegate when the region the map view is displaying changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:regionwillchangeanimated:))*