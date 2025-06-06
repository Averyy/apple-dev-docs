# region

**Framework**: MapKit  
**Kind**: property

The area the map view displays.

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
var region: MKCoordinateRegion { get set }
```

#### Discussion

The  encompasses both the latitude and longitude center point of the map, and the span of coordinates to display. The span values provide an implicit zoom value for the map. The larger the displayed area, the lower the amount of zoom. Similarly, the smaller the displayed area, the greater the amount of zoom.

Changing only the center coordinate of the region can still cause the span to change implicitly. The span might change because the distances that a span represents change at different latitudes and longitudes, and the map view may need to adjust the span to account for the new location. If you want to change the center coordinate without changing the zoom level, use the [`centerCoordinate`](mkmapview/centercoordinate.md) instead.

Changing the value of this property updates the map view immediately. When setting this property, the map may adjust the new region value so that it fits the visible area of the map precisely. This ensures that the value in this property reflects the visible portion of the map. However, it does mean that if you get the value of this property right after setting it, the returned value may not match the value you set. You can use the [`regionThatFits(_:)`](mkmapview/regionthatfits(_:).md) method to determine the region that the map sets.

If you want to animate the change in region, use the [`setRegion(_:animated:)`](mkmapview/setregion(_:animated:).md) method instead.

## See Also

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
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](mkmapview/setvisiblemaprect(_:edgepadding:animated:).md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/region)*