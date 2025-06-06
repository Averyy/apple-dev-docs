# setVisibleMapRect(_:edgePadding:animated:)

**Framework**: MapKit  
**Kind**: method

Changes the currently visible portion of the map, allowing you to specify additional space around the edges.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets, animated animate: Bool)
```

## Parameters

- `mapRect`: The map rectangle to make visible in the map view.
- `insets`: The amount of additional space (measured in screen points) to make visible around the specified rectangle.
- `animate`: Specify   if you want the map view to animate the transition to the new map rectangle or   if you want the map to center on the specified rectangle immediately.

## See Also

- [var region: MKCoordinateRegion](mkmapview/region.md)
  The area the map view displays.
- [func setRegion(MKCoordinateRegion, animated: Bool)](mkmapview/setregion(_:animated:).md)
  Changes the currently visible region, and optionally animates the change.
- [var centerCoordinate: CLLocationCoordinate2D](mkmapview/centercoordinate.md)
  The map coordinate at the center of the map view.
- [func setCenter(CLLocationCoordinate2D, animated: Bool)](mkmapview/setcenter(_:animated:).md)
  Changes the center coordinate of the map, and optionally animates the change.
- [func showAnnotations([any MKAnnotation], animated: Bool)](mkmapview/showannotations(_:animated:).md)
  Sets the visible region so that the map displays the specified annotations.
- [var visibleMapRect: MKMapRect](mkmapview/visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](mkmapview/setvisiblemaprect(_:animated:).md)
  Changes the currently visible portion of the map, and optionally animates the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setvisiblemaprect(_:edgepadding:animated:))*