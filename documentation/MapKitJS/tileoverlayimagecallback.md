# TileOverlayImageCallback

**Framework**: MapKit JS  
**Kind**: typealias

A callback function that provides tile images for a tile overlay.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
type TileOverlayImageCallback = (
    x: number,
    y: number,
    z: number,
    scale: number,
    data: any,
) => ImageSource | Promise<ImageSource> | null;
```

#### Discussion

When MapKit JS needs to display a tile, it invokes the callback with the parameters `x`, `y`, `z`, `scale`, and `data`. Return one of the following:

- An [`ImageSource`](imagesource.md) such as an `HTMLCanvasElement` or `OffscreenCanvas` for synchronous tile rendering.
- A `Promise` that resolves to an [`ImageSource`](imagesource.md) for asynchronous tile loading.
- `null` to indicate there is no tile for the requested coordinates.

The following example creates a [`TileOverlay`](tileoverlay.md) with a callback that draws each tile on a canvas:

```javascript
const overlay = new mapkit.TileOverlay((x, y, z, scale) => {
    const size = 256 * scale;
    const canvas = new OffscreenCanvas(size, size);
    const ctx = canvas.getContext("2d");
    // Draw tile content based on x, y, z coordinates.
    return canvas;
});
```

To load tiles asynchronously, return a `Promise`:

```javascript
const overlay = new mapkit.TileOverlay((x, y, z, scale) => {
    return fetch(`https://myserver/tile/${z}/${x}/${y}`)
        .then((response) => response.blob())
        .then((blob) => createImageBitmap(blob));
});
```

See [`ImageSource`](imagesource.md) for cross-origin requirements.

## See Also

- [new TileOverlay(imageForTile, options)](tileoverlay/tileoverlayconstructor.md)
  Creates a tile overlay with a URL template or image callback and style options.
- [interface TileOverlayConstructorOptions](tileoverlayconstructoroptions.md)
  Attributes for initializing a tile overlay, including minimum and maximum zoom, opacity, and custom data.
- [type TileOverlayUrlTemplate](tileoverlayurltemplate.md)
  A type that specifies the URL template for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlayimagecallback)*