# glyphText

**Framework**: MapKit JS  
**Kind**: property

The text to display in the marker balloon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string glyphText;
```

#### Discussion

The text to display in the balloon instead of a glyph image. The default value is `""` (empty string). There’s a limited amount of space available for displaying glyph text. Specify no more than two or three characters.

If you specify both a [`glyphImage`](markerannotationconstructoroptions/glyphimage.md) and [`glyphText`](markerannotationconstructoroptions/glyphtext.md), MapKit JS ignores the glyph image and displays the glyph text.

## See Also

- [color](markerannotationconstructoroptions/color.md)
  The background color of the balloon.
- [glyphColor](markerannotationconstructoroptions/glyphcolor.md)
  The fill color of the glyph.
- [glyphImage](markerannotationconstructoroptions/glyphimage.md)
  The image to display in the marker balloon.
- [selectedGlyphImage](markerannotationconstructoroptions/selectedglyphimage.md)
  The image to display in the balloon when the user selects the marker.
- [subtitleVisibility](markerannotationconstructoroptions/subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.
- [titleVisibility](markerannotationconstructoroptions/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/glyphtext)*