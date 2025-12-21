# isZoomEnabled

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get isZoomEnabled(): boolean;
set isZoomEnabled(value: boolean);
```

#### Discussion

Pinch-to-zoom with a trackpad requires browser touch event support. You can zoom the map programmatically when zoom isn’t in an enabled state by changing the [`region`](map/region.md) or [`visibleMapRect`](map/visiblemaprect.md).

## See Also

- [isRotationAvailable](map/isrotationavailable.md)
  A Boolean value that indicates whether map rotation is available.
- [isRotationEnabled](map/isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [isScrollEnabled](map/isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/iszoomenabled)*