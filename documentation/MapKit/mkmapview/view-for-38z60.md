# view(for:)

**Framework**: MapKit  
**Kind**: method

Returns the view associated with the overlay object, if any.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
func view(for overlay: any MKOverlay) -> MKOverlayView
```

#### Return Value

The view associated with the overlay object or `nil` if the overlay is not onscreen.

## Parameters

- `overlay`: The overlay object whose view you want.

## See Also

- [func mapView(MKMapView, didAddOverlayViews: [Any])](mkmapviewdelegate/mapview(_:didaddoverlayviews:).md)
  Tells the delegate when the map adds one or more overlay views to the map.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](mkmapviewdelegate/mapview(_:viewfor:)-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/view(for:)-38z60)*