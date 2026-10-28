# showAnnotations(_:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

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
func showAnnotations(_ annotations: [any MKAnnotation], animated: Bool)
```

```objc
- (void) showAnnotations:(NSArray<id<MKAnnotation>> *) annotations animated:(BOOL) animated;
```

## Discussion

Calling this method updates the value in the [`region`](./region.md) property, and potentially other properties, to reflect the new map region.

## Parameters

- `annotations`: The annotations that you want to be visible on the map.
- `animated`: Specify [`true`](../../Swift/true.md) if you want the map view to animate the region change, or [`false`](../../Swift/false.md) if you want the map to display the new region immediately without animations.

## See Also

### Manipulating the visible portion of the map
- [var region: MKCoordinateRegion](./region.md)
  The area the map view displays.
- [func setRegion(MKCoordinateRegion, animated: Bool)](./setregion%28_,animated%29.md)
  Changes the currently visible region, and optionally animates the change.
- [var centerCoordinate: CLLocationCoordinate2D](./centercoordinate.md)
  The map coordinate at the center of the map view.
- [func setCenter(CLLocationCoordinate2D, animated: Bool)](./setcenter%28_,animated%29.md)
  Changes the center coordinate of the map, and optionally animates the change.
- [var visibleMapRect: MKMapRect](./visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](./setvisiblemaprect%28_,animated%29.md)
  Changes the currently visible portion of the map, and optionally animates the change.
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](./setvisiblemaprect%28_,edgepadding,animated%29.md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/showannotations(_:animated:))*