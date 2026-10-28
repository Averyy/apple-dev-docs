# mapView(_:regionDidChangeAnimated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
optional func mapView(_ mapView: MKMapView, regionDidChangeAnimated animated: Bool)
```

```objc
- (void) mapView:(MKMapView *) mapView regionDidChangeAnimated:(BOOL) animated;
```

## Discussion

The map view calls this method at the end of a change to the map’s visible region.

## Parameters

- `mapView`: The map view with the visible region that changes.
- `animated`: If [`true`](../../Swift/true.md), the map view animates the change to the new region.

## See Also

### Responding to map position changes
- [func mapView(MKMapView, regionWillChangeAnimated: Bool)](./mapview%28_,regionwillchangeanimated%29.md)
  Tells the delegate when the region the map view is displaying is about to change.
- [func mapViewDidChangeVisibleRegion(MKMapView)](./mapviewdidchangevisibleregion%28_%29.md)
  Tells the delegate when the map view’s visible region changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:regiondidchangeanimated:))*