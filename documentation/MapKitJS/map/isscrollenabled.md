# isScrollEnabled

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get isScrollEnabled(): boolean;
set isScrollEnabled(value: boolean);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

You can programmatically cause the map to scroll when scrolling isn’t in an enabled state by changing the map’s [`center`](map/center.md) and [`region`](map/region.md) coordinates.

## See Also

- [isRotationAvailable](map/isrotationavailable.md)
  A Boolean value that indicates whether map rotation is available.
- [isRotationEnabled](map/isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [isZoomEnabled](map/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/isscrollenabled)*