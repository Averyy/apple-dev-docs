# new CircleOverlay(coordinate, radius, options)

**Framework**: MapKit JS  
**Kind**: init

Creates a circle overlay with a center coordinate, radius, and style options.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
constructor(
        coordinate: Coordinate,
        radius: number,
        options?: OverlayOptions,
    );
```

#### Discussion

An `options` parameter for a circle overlay resembles the following example:

```javascript
{
    style: new mapkit.Style({
        lineWidth: 2,
        strokeColor: "#999",
        fillColor: "#FFF"
    }),
    data: {
        population: 30500
    },
    enabled: false
}
```

## Parameters

- `coordinate`: The required coordinate of the circle’s center.
- `radius`: The circle’s required radius, in meters.
- `options`: An optional object literal of overlay properties for initializing the circle.

## See Also

- [interface OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/circleoverlay/circleoverlayconstructor)*