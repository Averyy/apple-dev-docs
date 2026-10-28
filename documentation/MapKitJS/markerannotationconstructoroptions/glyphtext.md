# glyphText

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

The text to display in the marker balloon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
glyphText?: string;
```

## Discussion

The text to display in the balloon instead of a glyph image. The default value is `null`. There’s a limited amount of space available for displaying glyph text. Specify no more than two or three characters.

If you specify both a [`glyphImage`](./glyphimage.md) and [`glyphText`](./glyphtext.md), MapKit JS ignores the glyph image and displays the glyph text.

## See Also

### Setting marker annotation properties
- [color](./color.md)
  The background color of the balloon.
- [glyphColor](./glyphcolor.md)
  The fill color of the glyph.
- [glyphImage](./glyphimage.md)
  The image to display in the marker balloon.
- [selectedGlyphImage](./selectedglyphimage.md)
  The image to display in the balloon when the user selects the marker.
- [subtitleVisibility](./subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.
- [titleVisibility](./titlevisibility.md)
  A value that determines the behavior of the title’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/glyphtext)*