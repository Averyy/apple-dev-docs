# mapView(_:selectionAccessoryFor:)

**Framework**: MapKit  
**Kind**: method

Specifies the accessory to display for a selected annotation

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, selectionAccessoryFor annotation: any MKAnnotation) -> MKSelectionAccessory?
```

#### Discussion

Called for all selected annotations. Not all types of annotations support displaying selection accessories. For example, the map item detail selection accessory is only supported for [`MKMapItemAnnotation`](mkmapitemannotation.md) and [`MKMapFeatureAnnotation`](mkmapfeatureannotation.md). Please return `nil` for annotations where a selection accessory is not desired.

No accessory will be displayed if…

- nil is returned
- [`mapView(_:selectionAccessoryFor:)`](mkmapviewdelegate/mapview(_:selectionaccessoryfor:).md) is not implemented
- the accessory returned is not supported for `annotation`

## Parameters

- `mapView`: The map view that requests the selection accessory.
- `annotation`: The annotation.

## See Also

- [func mapView(MKMapView, rendererFor: any MKOverlay) -> MKOverlayRenderer](mkmapviewdelegate/mapview(_:rendererfor:).md)
  Asks the delegate for a renderer object to use when drawing the specified overlay.
- [func mapView(MKMapView, didAdd: [MKOverlayRenderer])](mkmapviewdelegate/mapview(_:didadd:)-793gj.md)
  Tells the delegate when the map view adds one or more renderer objects to the map.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](mkmapviewdelegate/mapview(_:viewfor:)-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](mkmapviewdelegate/mapview(_:didaddoverlayviews:).md)
  Tells the delegate when the map adds one or more overlay views to the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:selectionaccessoryfor:))*