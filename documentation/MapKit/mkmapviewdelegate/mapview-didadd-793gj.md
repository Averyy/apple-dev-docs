# mapView(_:didAdd:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the map view adds one or more renderer objects to the map.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, didAdd renderers: [MKOverlayRenderer])
```

#### Discussion

The map view adds renderer objects when it needs them to draw their contents, which might be prior to those contents appearing onscreen. It calls this method to let you know that the renderer is active and in use. By the time the map view calls this method, it has already added specified renderers to the map.

## Parameters

- `mapView`: The map view that adds the renderer objects.
- `renderers`: The renderer objects that the map view adds.

## See Also

- [func mapView(MKMapView, selectionAccessoryFor: any MKAnnotation) -> MKSelectionAccessory?](mkmapviewdelegate/mapview(_:selectionaccessoryfor:).md)
  Specifies the accessory to display for a selected annotation
- [func mapView(MKMapView, rendererFor: any MKOverlay) -> MKOverlayRenderer](mkmapviewdelegate/mapview(_:rendererfor:).md)
  Asks the delegate for a renderer object to use when drawing the specified overlay.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](mkmapviewdelegate/mapview(_:viewfor:)-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](mkmapviewdelegate/mapview(_:didaddoverlayviews:).md)
  Tells the delegate when the map adds one or more overlay views to the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didadd:)-793gj)*