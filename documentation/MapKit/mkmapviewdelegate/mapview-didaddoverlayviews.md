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

- [func mapView(MKMapView, selectionAccessoryFor: any MKAnnotation) -> MKSelectionAccessory?](mkmapviewdelegate/mapview(_:selectionaccessoryfor:).md)
  Specifies the accessory to display for a selected annotation
- [func mapView(MKMapView, rendererFor: any MKOverlay) -> MKOverlayRenderer](mkmapviewdelegate/mapview(_:rendererfor:).md)
  Asks the delegate for a renderer object to use when drawing the specified overlay.
- [func mapView(MKMapView, didAdd: [MKOverlayRenderer])](mkmapviewdelegate/mapview(_:didadd:)-793gj.md)
  Tells the delegate when the map view adds one or more renderer objects to the map.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](mkmapviewdelegate/mapview(_:viewfor:)-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didaddoverlayviews:))*