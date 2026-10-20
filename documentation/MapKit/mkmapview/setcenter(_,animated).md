# setCenter(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func setCenter(_ coordinate: CLLocationCoordinate2D, animated: Bool)
```

```objc
- (void) setCenterCoordinate:(CLLocationCoordinate2D) coordinate animated:(BOOL) animated;
```

#### Discussion

Changing the center coordinate centers the map on the new coordinate without changing the current zoom level. It also updates the value in the [`region`](./region.md) property to reflect the new center coordinate and the new span values needed to maintain the current zoom level.

## Parameters

- `coordinate`: The new center coordinate for the map.
- `animated`: Specify [`true`](../../Swift/true.md) if you want the map view to scroll to the new location or [`false`](../../Swift/false.md) if you want the map to display the new location immediately.

## See Also

### Manipulating the visible portion of the map
- [var region: MKCoordinateRegion](./region.md)
  The area the map view displays.
- [func setRegion(MKCoordinateRegion, animated: Bool)](./setregion%28_,animated%29.md)
  Changes the currently visible region, and optionally animates the change.
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The map coordinate at the center of the map view.
- [func showAnnotations([any MKAnnotation], animated: Bool)](./showannotations%28_,animated%29.md)
  Sets the visible region so that the map displays the specified annotations.
- [var visibleMapRect: MKMapRect](./visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](./setvisiblemaprect%28_,animated%29.md)
  Changes the currently visible portion of the map, and optionally animates the change.
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](./setvisiblemaprect%28_,edgepadding,animated%29.md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setcenter(_:animated:))*