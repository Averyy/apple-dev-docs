# mapView(_:didAddOverlayViews:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the map adds one or more overlay views to the map.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Implement the [`mapView(_:didAdd:)`](./mapview%28_,didadd%29-793gj.md) method instead.

## Declaration

```swift
optional func mapView(_ mapView: MKMapView, didAddOverlayViews overlayViews: [Any])
```

```objc
- (void) mapView:(MKMapView *) mapView didAddOverlayViews:(NSArray *) overlayViews;
```

## Discussion

By the time the map view calls this method, MapKit has added the specified views to the map.

## Parameters

- `mapView`: The map view that adds the overlay views.
- `overlayViews`: An array of [`MKOverlayView`](../mkoverlayview.md) objects representing the views that the map view adds.

## See Also

### Methods
- [func view(for: any MKOverlay) -> MKOverlayView](../mkmapview/view%28for%29-38z60.md)
  Returns the view associated with the overlay object, if any.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](./mapview%28_,viewfor%29-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:didaddoverlayviews:))*