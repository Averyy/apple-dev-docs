# mapView(_:rendererFor:)

**Framework**: MapKit  
**Kind**: method

Asks the delegate for a renderer object to use when drawing the specified overlay.

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
optional func mapView(_ mapView: MKMapView, rendererFor overlay: any MKOverlay) -> MKOverlayRenderer
```

#### Return Value

The renderer to use when presenting the specified overlay on the map.

#### Discussion

Implement this method and use it to provide an appropriate renderer object for your overlays. The renderer object is responsible for drawing the contents of your overlay when the map view requests it to. MapKit supports many different types of standard renderer objects and you may also define your own custom renderers.

## Parameters

- `mapView`: The map view that requests the renderer object.
- `overlay`: The overlay object that the map view is about to display.

## See Also

- [func mapView(MKMapView, selectionAccessoryFor: any MKAnnotation) -> MKSelectionAccessory?](mkmapviewdelegate/mapview(_:selectionaccessoryfor:).md)
  Specifies the accessory to display for a selected annotation
- [func mapView(MKMapView, didAdd: [MKOverlayRenderer])](mkmapviewdelegate/mapview(_:didadd:)-793gj.md)
  Tells the delegate when the map view adds one or more renderer objects to the map.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](mkmapviewdelegate/mapview(_:viewfor:)-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](mkmapviewdelegate/mapview(_:didaddoverlayviews:).md)
  Tells the delegate when the map adds one or more overlay views to the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:rendererfor:))*