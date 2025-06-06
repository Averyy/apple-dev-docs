# showAnnotations(_:animated:)

**Framework**: MapKit  
**Kind**: method

Sets the visible region so that the map displays the specified annotations.

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
func showAnnotations(_ annotations: [any MKAnnotation], animated: Bool)
```

#### Discussion

Calling this method updates the value in the [`region`](mkmapview/region.md) property, and potentially other properties, to reflect the new map region.

## Parameters

- `annotations`: The annotations that you want to be visible on the map.
- `animated`: Specify   if you want the map view to animate the region change, or   if you want the map to display the new region immediately without animations.

## See Also

- [var region: MKCoordinateRegion](mkmapview/region.md)
  The area the map view displays.
- [func setRegion(MKCoordinateRegion, animated: Bool)](mkmapview/setregion(_:animated:).md)
  Changes the currently visible region, and optionally animates the change.
- [var centerCoordinate: CLLocationCoordinate2D](mkmapview/centercoordinate.md)
  The map coordinate at the center of the map view.
- [func setCenter(CLLocationCoordinate2D, animated: Bool)](mkmapview/setcenter(_:animated:).md)
  Changes the center coordinate of the map, and optionally animates the change.
- [var visibleMapRect: MKMapRect](mkmapview/visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](mkmapview/setvisiblemaprect(_:animated:).md)
  Changes the currently visible portion of the map, and optionally animates the change.
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](mkmapview/setvisiblemaprect(_:edgepadding:animated:).md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showannotations(_:animated:))*