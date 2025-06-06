# visibleMapRect

**Framework**: MapKit  
**Kind**: property

The area visible in the map view.

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
var visibleMapRect: MKMapRect { get set }
```

#### Discussion

This property represents the same basic information as the [`region`](mkmapview/region.md) property but specified as a map rectangle instead of a region.

Changing the value of this property updates the map view immediately. If you want to animate the change, use the [`setVisibleMapRect(_:animated:)`](mkmapview/setvisiblemaprect(_:animated:).md) method instead.

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
- [func setVisibleMapRect(MKMapRect, animated: Bool)](mkmapview/setvisiblemaprect(_:animated:).md)
  Changes the currently visible portion of the map, and optionally animates the change.
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](mkmapview/setvisiblemaprect(_:edgepadding:animated:).md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/visiblemaprect)*