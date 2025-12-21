# mapView(_:viewFor:)

**Framework**: MapKit  
**Kind**: method

Asks the delegate for the overlay view to use when displaying the specified overlay object.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, viewFor overlay: any MKOverlay) -> MKOverlayView
```

#### Return Value

The view to use when presenting the specified overlay on the map. If you return `nil`, no view  displays for the specified overlay object.

## Parameters

- `mapView`: The map view that requests the overlay view.
- `overlay`: The object representing the overlay that the map view is about to display.

## See Also

- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](mkmapviewdelegate/mapview(_:didaddoverlayviews:).md)
  Tells the delegate when the map adds one or more overlay views to the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:viewfor:)-6j267)*