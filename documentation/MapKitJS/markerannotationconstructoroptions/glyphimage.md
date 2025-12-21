# glyphImage

**Framework**: MapKit JS  
**Kind**: property

The image to display in the marker balloon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
glyphImage?: ImageDelegate | ImageHashObject | null;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

The glyph image values need to be object literals containing absolute or relative URLs to standard, 2x, and 3x Retina display assets. The framework requires at least one image at 20 x 20 pixels.

MapKit JS uses the default glyph image of a pin if you set [`glyphImage`](markerannotationconstructoroptions/glyphimage.md) to `null`, `undefined`, or “” (an empty string). If you specify both a [`glyphImage`](markerannotationconstructoroptions/glyphimage.md) and [`glyphText`](markerannotationconstructoroptions/glyphtext.md), the framework ignores the glyph image and displays the glyph text.

## See Also

- [color](markerannotationconstructoroptions/color.md)
  The background color of the balloon.
- [glyphColor](markerannotationconstructoroptions/glyphcolor.md)
  The fill color of the glyph.
- [glyphText](markerannotationconstructoroptions/glyphtext.md)
  The text to display in the marker balloon.
- [selectedGlyphImage](markerannotationconstructoroptions/selectedglyphimage.md)
  The image to display in the balloon when the user selects the marker.
- [subtitleVisibility](markerannotationconstructoroptions/subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.
- [titleVisibility](markerannotationconstructoroptions/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/glyphimage)*