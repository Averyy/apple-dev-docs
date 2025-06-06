# isRotationAvailable

**Framework**: MapKit JS  
**Kind**: property

A Boolean value that indicates whether map rotation is available.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute boolean isRotationAvailable;
```

#### Discussion

MapKit JS determines whether it’s possible to rotate the map, and sets [`isRotationAvailable`](mapkit.map/isrotationavailable.md) to `true` or `false`. When the value is `true`, users can rotate the map and any labels on the map remain horizontal.

The value for [`isRotationAvailable`](mapkit.map/isrotationavailable.md) is:

When `isRotationAvailable` is `false`, [`isRotationEnabled`](mapkit.map/isrotationenabled.md) is always `false` and [`rotation`](mapkit.map/rotation.md) is always `0`.

## See Also

- [isRotationEnabled](mapkit.map/isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [isScrollEnabled](mapkit.map/isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.
- [isZoomEnabled](mapkit.map/iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/isrotationavailable)*