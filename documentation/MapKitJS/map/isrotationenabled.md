# isRotationEnabled

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get isRotationEnabled(): boolean;
set isRotationEnabled(value: boolean);
```

#### Discussion

When `isRotationEnabled` is `false`, you can still rotate the map programmatically by using [`rotation`](map/rotation.md) or [`setRotationAnimated(degrees, animated)`](map/setrotationanimated.md).

## See Also

- [isRotationAvailable](map/isrotationavailable.md)
  A Boolean value that indicates whether map rotation is available.
- [isScrollEnabled](map/isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.
- [isZoomEnabled](map/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/isrotationenabled)*