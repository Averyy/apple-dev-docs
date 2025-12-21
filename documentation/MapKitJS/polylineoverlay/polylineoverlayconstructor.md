# new PolylineOverlay(points, options)

**Framework**: MapKit JS  
**Kind**: init

Creates a polyline overlay with coordinate points and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(points: Coordinate[], options?: OverlayOptions);
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

- [interface OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/polylineoverlay/polylineoverlayconstructor)*