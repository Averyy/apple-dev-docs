# new PolygonOverlay(points, options)

**Framework**: MapKit JS  
**Kind**: init

Creates a polygon overlay with an array of points and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(
        points: Coordinate[][] | Coordinate[],
        options?: OverlayOptions,
    );
```

#### Discussion

The following example shows the `options` parameter for a polygon overlay:

```javascript
{
    style: new mapkit.Style({
        lineWidth: 2,
        strokeColor: "#F00",
        fillColor: "#339"
    }),
    selected: true
}
```

## Parameters

- `points`: The points in the polygon as an array of arrays of  , or an array of  . For the latter, MapKit JS autowraps the array with an enclosing array.
- `options`: An optional object literal of options for initializing the polygon.

## See Also

- [interface OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/polygonoverlay/polygonoverlayconstructor)*