# mapkit.PolylineOverlay

**Framework**: MapKit JS  
**Kind**: init

Creates a polyline overlay with coordinate points and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
new mapkit.PolylineOverlay(
	mapkit.Coordinate[] points,
	optional StylesOverlayOptions options
);
```

#### Discussion

The following is an example of the `options` parameter for a polyline overlay:

```javascript
{
    style: new mapkit.Style({
        lineWidth: 2,
        strokeColor: "#F0F"
    })
}
```

## Parameters

- `points`: The required points in the polyline as an array of  .
- `options`: An optional object literal of style options for initializing the polyline.

## See Also

- [StylesOverlayOptions](stylesoverlayoptions.md)
  An observable set of style attributes for an overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.polylineoverlay/mapkit.polylineoverlay)*