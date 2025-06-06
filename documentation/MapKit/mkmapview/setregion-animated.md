# setRegion(_:animated:)

**Framework**: MapKit  
**Kind**: method

Changes the currently visible region, and optionally animates the change.

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
func setRegion(_ region: MKCoordinateRegion, animated: Bool)
```

#### Discussion

Changing just the center coordinate of the region can still cause the span values to change implicitly. The span values might change because the distances that a span repesents change at different latitudes and longitudes, and the map view may need to adjust the span to account for the new location. If you want to change the center coordinate without changing the zoom level, use the [`setCenter(_:animated:)`](mkmapview/setcenter(_:animated:).md) instead.

When setting a new region, the map may adjust the value in the `region` parameter so that it fits the visible area of the map precisely. This adjustment ensures that the value in the [`region`](mkmapview/region.md) property reflects the visible portion of the map. However, it does mean that if you get the value of that property right after calling this method, the returned value may not match the value you set. You can use the [`regionThatFits(_:)`](mkmapview/regionthatfits(_:).md) method to determine the region that the map sets.

## Parameters

- `region`: The new region to display in the map view.
- `animated`: Specify   if you want the map view to animate the transition to the new region, or   if you want the map to center on the specified region immediately.

## See Also

- [var region: MKCoordinateRegion](mkmapview/region.md)
  The area the map view displays.
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
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](mkmapview/setvisiblemaprect(_:edgepadding:animated:).md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setregion(_:animated:))*