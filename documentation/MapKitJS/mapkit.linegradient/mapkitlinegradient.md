# mapkit.LineGradient

**Framework**: MapKit JS  
**Kind**: init

Creates a style that renders a gradient along the length of a line.

**Availability**:
- MapKit JS 5.45+

## Declaration

```swift
new mapkit.LineGradient(
	optional Object options
);
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

The unit distance keys must be a number between `0` and `1`. A value of `0` represents the beginning of the polyline and a value of `1` represents the end. The associated values are CSS colors.

The following example creates a new gradient that progresses from `blue` at the start of the line to `red` at the end:

```javascript
overlay.style.lineGradient = new mapkit.LineGradient({
    0: "blue",
    1: "red"
});
```

If the start or end of the line don’t have a defined color, the gradient uses the style’s [`strokeColor`](mapkit.style/strokecolor.md) as a default.

You can extend gradients programatically with [`addColorStop`](mapkit.linegradient/addcolorstop.md) and [`addColorStopAtIndex`](mapkit.linegradient/addcolorstopatindex.md).

## Parameters

- `options`: A JavaScript object with unit distance values as keys with matched CSS colors.

## See Also

- [addColorStop](mapkit.linegradient/addcolorstop.md)
  Adds a color transition point to the gradient.
- [addColorStopAtIndex](mapkit.linegradient/addcolorstopatindex.md)
  Adds a color transition at the index point in the list of points within a polyline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.linegradient/mapkit.linegradient)*