# isRotationAvailable

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether map rotation is available.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get isRotationAvailable(): boolean;
set isRotationAvailable(_: boolean);
```

## Discussion

MapKit JS determines whether it’s possible to rotate the map, and sets [`isRotationAvailable`](./isrotationavailable.md) to `true` or `false`. When the value is `true`, users can rotate the map, and any labels on the map remain horizontal.

The value for [`isRotationAvailable`](./isrotationavailable.md) is:

- **`true`**: When the client renders the map, such as by browsers that support WebGL.
- **`false`**: When the Apple Maps server renders the map with a grid of image tiles, or when you implement your own tile overlays ([`addTileOverlay()`](./addtileoverlay.md)).

When `isRotationAvailable` is `false`, [`isRotationEnabled`](./isrotationenabled.md) is always `false` and [`rotation`](./rotation.md) is always `0`.

## See Also

### Accessing interaction properties
- [isRotationEnabled](./isrotationenabled.md)
  A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.
- [isScrollEnabled](./isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.
- [isZoomEnabled](./iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/isrotationavailable)*