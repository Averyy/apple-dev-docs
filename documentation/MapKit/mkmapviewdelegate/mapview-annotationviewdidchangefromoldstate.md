# mapView(_:annotationView:didChange:fromOldState:)

**Framework**: MapKit  
**Kind**: method

Tells the delegate when the drag state of one of its annotation views changes.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, didChange newState: MKAnnotationView.DragState, fromOldState oldState: MKAnnotationView.DragState)
```

#### Discussion

The drag state typically changes in response to user interactions with the annotation view. However, the annotation view itself is responsible for changing that state as well.

## Parameters

- `mapView`: The map view containing the annotation view.
- `view`: The annotation view whose drag state changed.
- `newState`: The new drag state of the annotation view.
- `oldState`: The previous drag state of the annotation view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapviewdelegate/mapview(_:annotationview:didchange:fromoldstate:))*