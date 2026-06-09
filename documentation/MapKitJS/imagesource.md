# ImageSource

**Framework**: MapKit JS  
**Kind**: typealias

A union type that represents image sources that the framework can use for annotations and tile overlays.

**Availability**:
- MapKit JS 6.0+

## Declaration

```swift
type ImageSource =
    | HTMLImageElement
    | HTMLCanvasElement
    | ImageBitmap
    | OffscreenCanvas;
```

## Mentions

- [Migrating from Version 5 to Version 6](migrating-from-version-5-to-version-6.md)
- [MapKit JS 6](mapkit-js-6.md)

#### Discussion

An [`ImageSource`](imagesource.md) is an `HTMLImageElement`, `HTMLCanvasElement`, `ImageBitmap`, or `OffscreenCanvas`. You can set an [`ImageSource`](imagesource.md) directly on the [`ImageAnnotation`](imageannotation.md) [`image`](imageannotation/image.md) property or the [`MarkerAnnotation`](markerannotation.md) [`glyphImage`](markerannotation/glyphimage.md) property to display a preloaded or dynamically generated image. You can also wrap an [`ImageSource`](imagesource.md) in a `Promise` to load the image asynchronously.

#### Utilizing Cross Origin Images

To enable cross-origin image sources for MapKit JS, instruct the browser to load them in CORS mode. The `HTMLImageElement` provides a `crossOrigin` property that you need to set to either `"anonymous"` (without cookies) or `"use-credentials"` (with a cookie) to opt-in to CORS request mode.

When compositing a `HTMLCanvasElement` or `ImageBitmap`, composite these objects  from CORS-enabled cross-origin, or same-origin images.

## See Also

- [type ImageHashObject](imagehashobject.md)
  An object that defines a set of images URLs for different scales.
- [interface ImageDelegate](imagedelegate.md)
  An object you use to provide images for annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/imagesource)*