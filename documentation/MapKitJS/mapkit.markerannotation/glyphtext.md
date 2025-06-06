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

## Mentions

- [Clustering annotations](clustering-annotations.md)

#### Discussion

This property is the text to display in the balloon instead of displaying a glyph image. The default value is `""` (empty string). There’s a limited amount of space available for displaying glyph text. Specify no more than two or three characters.

If you specify both a [`glyphImage`](mapkit.markerannotation/glyphimage.md) and [`glyphText`](mapkit.markerannotation/glyphtext.md), MapKit JS ignores the glyph image, and displays the glyph text.

## See Also

- [glyphImage](mapkit.markerannotation/glyphimage.md)
  The image to display in the marker balloon.
- [selectedGlyphImage](mapkit.markerannotation/selectedglyphimage.md)
  The image to display in the marker balloon when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.markerannotation/glyphtext)*