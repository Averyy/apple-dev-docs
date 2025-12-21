# selectedGlyphImage

**Framework**: MapKit JS  
**Kind**: property

The image to display in the balloon when the user selects the marker.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
selectedGlyphImage?: ImageDelegate | ImageHashObject | null;
```

#### Discussion

Provide glyph images as object literals containing absolute or relative URLs to standard, 2x, and 3x Retina display assets. The framework requires at least one image. MapKit JS displays the selected glyph image in the balloon when the marker is in the selected state. If you specify an image for this property, also specify an image in the [`glyphImage`](markerannotation/glyphimage.md) property.

Set the size of the selected glyph image to 40 x 40 pixels. MapKit JS scales glyph images to fit in the balloon. If you don’t set [`selectedGlyphImage`](markerannotationconstructoroptions/selectedglyphimage.md), the framework uses [`glyphImage`](markerannotationconstructoroptions/glyphimage.md) when the user selects the marker. The default image is a pin.

## See Also

- [color](markerannotationconstructoroptions/color.md)
  The background color of the balloon.
- [glyphColor](markerannotationconstructoroptions/glyphcolor.md)
  The fill color of the glyph.
- [glyphText](markerannotationconstructoroptions/glyphtext.md)
  The text to display in the marker balloon.
- [glyphImage](markerannotationconstructoroptions/glyphimage.md)
  The image to display in the marker balloon.
- [subtitleVisibility](markerannotationconstructoroptions/subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.
- [titleVisibility](markerannotationconstructoroptions/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/selectedglyphimage)*