# TileOverlayUrlTemplate

**Framework**: MapKit JS  
**Kind**: typealias

A type that specifies the URL template for a tile overlay.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
type TileOverlayUrlTemplate =
    | string
    | ((x: number, y: number, z: number, scale: number, data: any) => string);
```

#### Discussion

You may set the URL template as either a template string or a function.

The template string must be in the format: `https://myserver/tile?x={x}&y={y}&z={z}&scale={scale}`. MapKit JS replaces the `x`, `y`, `z`, and `scale` values depending on the displayed map region and screen resolution, then loads an image from that URL. You can also add custom values to the template string. For example, a template string could look like: `https://{subdomain}.customtileserver.com/{z}/{x}/{y}?lang={lang}`. In this case, you must define `TileOverlay.data.subdomain` and `TileOverlay.data.lang` for the placeholders to populate. Also, note that not all parameters are necessary in a template string. The `scale` parameter is absent in this example.

You can provide a callback function instead of the template string. When MapKit JS needs to request new tiles, it invokes the [`urlTemplate`](tileoverlay/urltemplate.md) callback with the parameters `x`, `y`, `z`, `scale`, and `data`. The callback function must return a URL for the provided parameters. If the return value is anything but a nonempty string, MapKit JS doesn’t load any tiles for the requested region.

## See Also

- [Adding interactivity to overlays](adding-interactivity-to-overlays.md)
  Configure and respond to overlays to make them interactive.
- [class Overlay](overlay.md)
  An abstract base object that defines the methods and properties for map overlays.
- [class Style](style.md)
  A set of observable style properties for overlays, including the color and opacity of strokes and fills, and line styles.
- [class CircleOverlay](circleoverlay.md)
  A circular overlay with a configurable radius that centers on a specific geographic coordinate.
- [class PolylineOverlay](polylineoverlay.md)
  An overlay of connected line segments that don’t form a closed shape.
- [class PolygonOverlay](polygonoverlay.md)
  An overlay consisting of one or more points that forms a closed shape.
- [interface OverlayOptions](overlayoptions.md)
  A dictionary of options that determines an overlay’s data, and indicates whether it’s visible, in an enabled state, and in a selected state.
- [class TileOverlay](tileoverlay.md)
  An overlay that covers an area of the map with bitmapped tiles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlayurltemplate)*