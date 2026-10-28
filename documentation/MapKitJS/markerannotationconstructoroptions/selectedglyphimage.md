# selectedGlyphImage

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The image to display in the balloon when the user selects the marker.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
selectedGlyphImage?:
    | ImageDelegate
    | ImageHashObject
    | ImageSource
    | Promise<ImageSource>
    | null;
```

## Discussion

Provide glyph images as object literals containing absolute or relative URLs to standard, 2x, and 3x Retina display assets, an [`ImageDelegate`](../imagedelegate.md), an [`ImageSource`](../imagesource.md) such as an `HTMLCanvasElement` or `ImageBitmap`, or a `Promise` that resolves to an [`ImageSource`](../imagesource.md). The framework requires at least one image. MapKit JS displays the selected glyph image in the balloon when the marker is in the selected state. If you specify an image for this property, also specify an image in the [`glyphImage`](../markerannotation/glyphimage.md) property.

Set the size of the selected glyph image to 40 x 40 pixels. MapKit JS scales glyph images to fit in the balloon. If you don’t set [`selectedGlyphImage`](./selectedglyphimage.md), the framework uses [`glyphImage`](./glyphimage.md) when the user selects the marker. The default image is a pin.

## See Also

### Setting marker annotation properties
- [color](./color.md)
  The background color of the balloon.
- [glyphColor](./glyphcolor.md)
  The fill color of the glyph.
- [glyphText](./glyphtext.md)
  The text to display in the marker balloon.
- [glyphImage](./glyphimage.md)
  The image to display in the marker balloon.
- [subtitleVisibility](./subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.
- [titleVisibility](./titlevisibility.md)
  A value that determines the behavior of the title’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/selectedglyphimage)*