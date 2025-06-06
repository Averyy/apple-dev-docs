# mapkit.PolygonOverlay

**Framework**: MapKit JS  
**Kind**: init

Creates a polygon overlay with an array of points and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.PolygonOverlay(
	mapkit.Coordinate[] points,
	optional StylesOverlayOptions options
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

- [StylesOverlayOptions](stylesoverlayoptions.md)
  An observable set of style attributes for an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.polygonoverlay/mapkit.polygonoverlay)*