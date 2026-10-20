# mapView(_:viewFor:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for the overlay view to use when displaying the specified overlay object.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Implement the [`mapView(_:rendererFor:)`](./mapview%28_,rendererfor%29.md) method instead.

## Declaration

```swift
optional func mapView(_ mapView: MKMapView, viewFor overlay: any MKOverlay) -> MKOverlayView
```

```objc
- (MKOverlayView *) mapView:(MKMapView *) mapView viewForOverlay:(id<MKOverlay>) overlay;
```

#### Return Value

The view to use when presenting the specified overlay on the map. If you return `nil`, no view  displays for the specified overlay object.

## Parameters

- `mapView`: The map view that requests the overlay view.
- `overlay`: The object representing the overlay that the map view is about to display.

## See Also

### Methods
- [func view(for: any MKOverlay) -> MKOverlayView](../mkmapview/view%28for%29-38z60.md)
  Returns the view associated with the overlay object, if any.
- [func mapView(MKMapView, didAddOverlayViews: [Any])](./mapview%28_,didaddoverlayviews%29.md)
  Tells the delegate when the map adds one or more overlay views to the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:viewfor:)-6j267)*