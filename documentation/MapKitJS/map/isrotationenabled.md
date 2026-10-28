# isRotationEnabled

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the user may rotate the map using the compass control or a rotate gesture.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get isRotationEnabled(): boolean;
set isRotationEnabled(value: boolean);
```

## Discussion

When `isRotationEnabled` is `false`, you can still rotate the map programmatically by using [`rotation`](./rotation.md) or [`setRotationAnimated()`](./setrotationanimated.md).

## See Also

### Accessing interaction properties
- [isRotationAvailable](./isrotationavailable.md)
  A Boolean value that indicates whether map rotation is available.
- [isScrollEnabled](./isscrollenabled.md)
  A Boolean value that determines whether the user can cause the map to scroll with a pointing device or with gestures on a touchscreen.
- [isZoomEnabled](./iszoomenabled.md)
  A Boolean value that determines whether the user may zoom in and out on the map using pinch gestures or the zoom control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/map/isrotationenabled)*