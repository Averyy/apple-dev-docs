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

- [func mapView(MKMapView, selectionAccessoryFor: any MKAnnotation) -> MKSelectionAccessory?](mkmapviewdelegate/mapview(_:selectionaccessoryfor:).md)
  Specifies the accessory to display for a selected annotation
- [func mapView(MKMapView, rendererFor: any MKOverlay) -> MKOverlayRenderer](mkmapviewdelegate/mapview(_:rendererfor:).md)
  Asks the delegate for a renderer object to use when drawing the specified overlay.
- [func mapView(MKMapView, didAdd: [MKOverlayRenderer])](mkmapviewdelegate/mapview(_:didadd:)-793gj.md)
  Tells the delegate when the map view adds one or more renderer objects to the map.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](mkmapviewdelegate/mapview(_:didaddoverlayviews:).md)
  Tells the delegate when the map adds one or more overlay views to the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:viewfor:)-6j267)*