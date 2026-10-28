# centerCoordinate

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The map coordinate at the center of the map view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var centerCoordinate: CLLocationCoordinate2D { get set }
```

```objc
@property (nonatomic) CLLocationCoordinate2D centerCoordinate;
```

## Discussion

Changing the value in this property centers the map on the new coordinate without changing the current zoom level. It also updates the values in the [`region`](./region.md) property to reflect the new center coordinate and the new span values needed to maintain the current zoom level.

Changing the value of this property updates the map view immediately. If you want to animate the change, use the [`setCenter(_:animated:)`](./setcenter%28_,animated%29.md) method instead.

## See Also

### Manipulating the visible portion of the map
- [var region: MKCoordinateRegion](./region.md)
  The area the map view displays.
- [func setRegion(MKCoordinateRegion, animated: Bool)](./setregion%28_,animated%29.md)
  Changes the currently visible region, and optionally animates the change.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/centercoordinate)*