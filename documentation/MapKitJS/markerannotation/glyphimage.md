# glyphImage

**Framework**: MapKit JS  
**Kind**: property

The image to display in the marker balloon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get glyphImage():
    | ImageSource
    | ImageHashObject
    | ImageDelegate
    | Promise<ImageSource>
    | null;
set glyphImage(
    value:
        | ImageSource
        | ImageHashObject
        | ImageDelegate
        | Promise<ImageSource>
        | null,
);
```

#### Discussion

Glyph image values can be object literals that contain absolute or relative URLs to standard, `@2x`, and `@3x` assets, an [`ImageDelegate`](imagedelegate.md), an [`ImageSource`](imagesource.md) such as an `HTMLCanvasElement` or `ImageBitmap`, or a `Promise` that resolves to an [`ImageSource`](imagesource.md). See [`ImageSource`](imagesource.md) for cross-origin requirements.

The framework requires at least one image at 20 x 20 pixels. Create glyph images as template images — a monochrome image with opacity, if needed — so that MapKit JS can apply the [`glyphColor`](markerannotation/glyphcolor.md) to tint the image.

If you set [`glyphImage`](markerannotationconstructoroptions/glyphimage.md) to `null` or `undefined`, MapKit JS uses the default glyph image of a pin. If you specify both a [`glyphImage`](markerannotation/glyphimage.md) and [`glyphText`](markerannotation/glyphtext.md), MapKit JS ignores the glyph image, and the framework displays glyph text.

## See Also

- [glyphText](markerannotation/glyphtext.md)
  The text to display in the marker balloon.
- [selectedGlyphImage](markerannotation/selectedglyphimage.md)
  The image to display in the marker balloon when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotation/glyphimage)*