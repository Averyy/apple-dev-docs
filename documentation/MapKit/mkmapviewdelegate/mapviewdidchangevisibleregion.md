# mapViewDidChangeVisibleRegion(_:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the map view’s visible region changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapViewDidChangeVisibleRegion(_ mapView: MKMapView)
```

#### Discussion

Use this method to update the map in response to intermediate changes to the region. The map view calls this method each time the value of its visible region changes.

> ❗ **Important**:  Because the map may call this method many times during the scrolling of the map, your implementation needs to be lightweight. Use this method to record the new region values or to make fast updates to your app’s interface. Don’t start any long-running synchronous tasks in this method.

## Parameters

- `mapView`: The map view with the visible region that changes.

## See Also

- [func mapView(MKMapView, regionWillChangeAnimated: Bool)](mkmapviewdelegate/mapview(_:regionwillchangeanimated:).md)
  Tells the delegate when the region the map view is displaying is about to change.
- [func mapView(MKMapView, regionDidChangeAnimated: Bool)](mkmapviewdelegate/mapview(_:regiondidchangeanimated:).md)
  Tells the delegate when the region the map view is displaying changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapviewdidchangevisibleregion(_:))*