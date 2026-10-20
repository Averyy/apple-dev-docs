# setVisibleMapRect(_:edgePadding:animated:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Instance Method

Changes the currently visible portion of the map, allowing you to specify additional space around the edges.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: UIEdgeInsets, animated animate: Bool)
```

*macOS*

```swift
func setVisibleMapRect(_ mapRect: MKMapRect, edgePadding insets: NSEdgeInsets, animated animate: Bool)
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
- (void) setVisibleMapRect:(MKMapRect) mapRect edgePadding:(UIEdgeInsets) insets animated:(BOOL) animate;
```

*macOS*

```objc
- (void) setVisibleMapRect:(MKMapRect) mapRect edgePadding:(NSEdgeInsets) insets animated:(BOOL) animate;
```

## Parameters

- `mapRect`: The map rectangle to make visible in the map view.
- `insets`: The amount of additional space (measured in screen points) to make visible around the specified rectangle.
- `animate`: Specify [`true`](../../Swift/true.md) if you want the map view to animate the transition to the new map rectangle or [`false`](../../Swift/false.md) if you want the map to center on the specified rectangle immediately.

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
- [func showAnnotations([any MKAnnotation], animated: Bool)](./showannotations%28_,animated%29.md)
  Sets the visible region so that the map displays the specified annotations.
- [var visibleMapRect: MKMapRect](./visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](./setvisiblemaprect%28_,animated%29.md)
  Changes the currently visible portion of the map, and optionally animates the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/setvisiblemaprect(_:edgepadding:animated:))*