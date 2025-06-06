# StylesOverlayOptions

**Framework**: MapKit JS  
**Kind**: struct

An observable set of style attributes for an overlay.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary StylesOverlayOptions {
	mapkit.Style style;
};
```

#### Overview

The style object is an observable dictionary of [`style`](stylesoverlayoptions/style.md) properties. To render an overlay, you must assign a style object to it. The style object specifies attributes, including stroke and fill colors, opacity, and line styles.

Because [`style`](stylesoverlayoptions/style.md) properties are observable, MapKit JS automatically reflects changes to a style property on overlays that you associate with that style object.

## Topics

### Overlay style
- [style](stylesoverlayoptions/style.md)
  An object literal of style properties.

## See Also

- [mapkit.CircleOverlay](mapkit.circleoverlay/mapkit.circleoverlay.md)
  Creates a circle overlay with a center coordinate, radius, and style options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/stylesoverlayoptions)*