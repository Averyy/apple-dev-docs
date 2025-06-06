# setCenter(_:animated:)

**Framework**: MapKit  
**Kind**: method

Changes the center coordinate of the map, and optionally animates the change.

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
func setCenter(_ coordinate: CLLocationCoordinate2D, animated: Bool)
```

#### Discussion

Changing the center coordinate centers the map on the new coordinate without changing the current zoom level. It also updates the value in the [`region`](mkmapview/region.md) property to reflect the new center coordinate and the new span values needed to maintain the current zoom level.

## Parameters

- `coordinate`: The new center coordinate for the map.
- `animated`: Specify   if you want the map view to scroll to the new location or   if you want the map to display the new location immediately.

## See Also

- [var region: MKCoordinateRegion](mkmapview/region.md)
  The area the map view displays.
- [func setRegion(MKCoordinateRegion, animated: Bool)](mkmapview/setregion(_:animated:).md)
  Changes the currently visible region, and optionally animates the change.
- [var centerCoordinate: CLLocationCoordinate2D](mkmapview/centercoordinate.md)
  The map coordinate at the center of the map view.
- [func showAnnotations([any MKAnnotation], animated: Bool)](mkmapview/showannotations(_:animated:).md)
  Sets the visible region so that the map displays the specified annotations.
- [var visibleMapRect: MKMapRect](mkmapview/visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](mkmapview/setvisiblemaprect(_:animated:).md)
  Changes the currently visible portion of the map, and optionally animates the change.
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](mkmapview/setvisiblemaprect(_:edgepadding:animated:).md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setcenter(_:animated:))*