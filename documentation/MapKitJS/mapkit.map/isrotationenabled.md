# isRotationEnabled

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute boolean isRotationEnabled;
```

#### Discussion

When `isRotationEnabled` is `false`, you can still rotate the map programmatically by using [`rotation`](mapkit.map/rotation.md) or [`setRotationAnimated`](mapkit.map/setrotationanimated.md).

## See Also

- [isRotationAvailable](mapkit.map/isrotationavailable.md)
  A Boolean value that indicates whether map rotation is available.
- [isScrollEnabled](mapkit.map/isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.
- [isZoomEnabled](mapkit.map/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/isrotationenabled)*