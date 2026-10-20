# selectedGlyphImage

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Instance Property

The image to display in the marker balloon when the user selects the marker.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
get selectedGlyphImage():
    | ImageSource
    | ImageHashObject
    | ImageDelegate
    | Promise<ImageSource>
    | null;
set selectedGlyphImage(
    value:
        | ImageSource
        | ImageHashObject
        | ImageDelegate
        | Promise<ImageSource>
        | null,
);
```

## Mentions

- [MapKit JS 5](../mapkit-js-5.md)

#### Discussion

Glyph image values can be object literals that contain absolute or relative URLs to standard, `@2x`, and `@3x` assets, an [`ImageDelegate`](../imagedelegate.md), an [`ImageSource`](../imagesource.md) such as an `HTMLCanvasElement` or `ImageBitmap`, or a `Promise` that resolves to an [`ImageSource`](../imagesource.md). See [`ImageSource`](../imagesource.md) for cross-origin requirements.

The framework requires at least one image and displays the selected glyph image in the balloon when the marker is in the selected state. If you specify an image for this property, also specify an image in the [`glyphImage`](./glyphimage.md) property.

Set the size of the selected glyph image to 40 x 40 pixels. Create glyph images as template images — a monochrome image with opacity, if needed — so that MapKit JS can apply the [`glyphColor`](./glyphcolor.md) to tint the image. MapKit JS scales glyph images to fit in the balloon. If you don’t set [`selectedGlyphImage`](./selectedglyphimage.md), the framework uses [`glyphImage`](./glyphimage.md) when the user selects the marker. The default image is a pin.

## See Also

### Setting the glyph image and text
- [glyphText](./glyphtext.md)
  The text to display in the marker balloon.
- [glyphImage](./glyphimage.md)
  The image to display in the marker balloon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotation/selectedglyphimage)*