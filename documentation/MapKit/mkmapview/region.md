# region

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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
var region: MKCoordinateRegion { get set }
```

```objc
@property (nonatomic) MKCoordinateRegion region;
```

## Discussion

The *region* encompasses both the latitude and longitude center point of the map, and the span of coordinates to display. The span values provide an implicit zoom value for the map. The larger the displayed area, the lower the amount of zoom. Similarly, the smaller the displayed area, the greater the amount of zoom.

Changing only the center coordinate of the region can still cause the span to change implicitly. The span might change because the distances that a span represents change at different latitudes and longitudes, and the map view may need to adjust the span to account for the new location. If you want to change the center coordinate without changing the zoom level, use the [`centerCoordinate`](./centercoordinate.md) instead.

Changing the value of this property updates the map view immediately. When setting this property, the map may adjust the new region value so that it fits the visible area of the map precisely. This ensures that the value in this property reflects the visible portion of the map. However, it does mean that if you get the value of this property right after setting it, the returned value may not match the value you set. You can use the [`regionThatFits(_:)`](./regionthatfits%28_%29.md) method to determine the region that the map sets.

If you want to animate the change in region, use the [`setRegion(_:animated:)`](./setregion%28_,animated%29.md) method instead.

## See Also

### Manipulating the visible portion of the map
- [func setRegion(MKCoordinateRegion, animated: Bool)](./setregion%28_,animated%29.md)
  Changes the currently visible region, and optionally animates the change.
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The map coordinate at the center of the map view.
- [func setCenter(CLLocationCoordinate2D, animated: Bool)](./setcenter%28_,animated%29.md)
  Changes the center coordinate of the map, and optionally animates the change.
- [func showAnnotations([any MKAnnotation], animated: Bool)](./showannotations%28_,animated%29.md)
  Sets the visible region so that the map displays the specified annotations.
- [var visibleMapRect: MKMapRect](./visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](./setvisiblemaprect%28_,animated%29.md)
  Changes the currently visible portion of the map, and optionally animates the change.
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](./setvisiblemaprect%28_,edgepadding,animated%29.md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/region)*