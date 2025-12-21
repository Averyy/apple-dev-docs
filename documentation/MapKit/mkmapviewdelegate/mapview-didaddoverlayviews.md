# mapView(_:didAddOverlayViews:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the map adds one or more overlay views to the map.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, didAddOverlayViews overlayViews: [Any])
```

#### Discussion

By the time the map view calls this method, MapKit has added the specified views to the map.

## Parameters

- `mapView`: The map view that adds the overlay views.
- `overlayViews`: An array of   objects representing the views that the map view adds.

## See Also

- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](mkmapviewdelegate/mapview(_:viewfor:)-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didaddoverlayviews:))*