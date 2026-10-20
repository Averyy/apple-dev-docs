# view(for:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Returns the view associated with the overlay object, if any.

**Availability**:
- iOS 4.0+ - Deprecated in 13.0
- iPadOS 4.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use the [`renderer(for:)`](./renderer%28for%29.md) method instead.

## Declaration

```swift
func view(for overlay: any MKOverlay) -> MKOverlayView
```

```objc
- (MKOverlayView *) viewForOverlay:(id<MKOverlay>) overlay;
```

#### Return Value

The view associated with the overlay object or `nil` if the overlay is not onscreen.

## Parameters

- `overlay`: The overlay object whose view you want.

## See Also

### Methods
- [func mapView(MKMapView, didAddOverlayViews: [Any])](../mkmapviewdelegate/mapview%28_,didaddoverlayviews%29.md)
  Tells the delegate when the map adds one or more overlay views to the map.
- [func mapView(MKMapView, viewFor: any MKOverlay) -> MKOverlayView](../mkmapviewdelegate/mapview%28_,viewfor%29-6j267.md)
  Asks the delegate for the overlay view to use when displaying the specified overlay object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/view(for:)-38z60)*