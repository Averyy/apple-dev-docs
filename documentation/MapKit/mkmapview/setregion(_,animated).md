# setRegion(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func setRegion(_ region: MKCoordinateRegion, animated: Bool)
```

```objc
- (void) setRegion:(MKCoordinateRegion) region animated:(BOOL) animated;
```

#### Discussion

Changing just the center coordinate of the region can still cause the span values to change implicitly. The span values might change because the distances that a span repesents change at different latitudes and longitudes, and the map view may need to adjust the span to account for the new location. If you want to change the center coordinate without changing the zoom level, use the [`setCenter(_:animated:)`](./setcenter%28_,animated%29.md) instead.

When setting a new region, the map may adjust the value in the `region` parameter so that it fits the visible area of the map precisely. This adjustment ensures that the value in the [`region`](./region.md) property reflects the visible portion of the map. However, it does mean that if you get the value of that property right after calling this method, the returned value may not match the value you set. You can use the [`regionThatFits(_:)`](./regionthatfits%28_%29.md) method to determine the region that the map sets.

## Parameters

- `region`: The new region to display in the map view.
- `animated`: Specify [`true`](../../Swift/true.md) if you want the map view to animate the transition to the new region, or [`false`](../../Swift/false.md) if you want the map to center on the specified region immediately.

## See Also

### Manipulating the visible portion of the map
- [var region: MKCoordinateRegion](./region.md)
  The area the map view displays.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setregion(_:animated:))*