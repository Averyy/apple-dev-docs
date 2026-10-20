# mapView(_:regionWillChangeAnimated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
optional func mapView(_ mapView: MKMapView, regionWillChangeAnimated animated: Bool)
```

```objc
- (void) mapView:(MKMapView *) mapView regionWillChangeAnimated:(BOOL) animated;
```

#### Discussion

The framework calls this method at the beginning of a change to the map’s visible region.

## Parameters

- `mapView`: The map view with the visible region that’s about to change.
- `animated`: If [`true`](../../Swift/true.md), the map view animates the change to the new region. If [`false`](../../Swift/false.md), the map view makes the change immediately.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Responding to map position changes
- [func mapViewDidChangeVisibleRegion(MKMapView)](./mapviewdidchangevisibleregion%28_%29.md)
  Tells the delegate when the map view’s visible region changes.
- [func mapView(MKMapView, regionDidChangeAnimated: Bool)](./mapview%28_,regiondidchangeanimated%29.md)
  Tells the delegate when the region the map view is displaying changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:regionwillchangeanimated:))*