# subtitleVisibility

**Framework**: MapKit JS  
**Kind**: property

A value that determines the behavior of the subtitle’s visibility.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
subtitleVisibility?: FeatureVisibility;
```

#### Discussion

The subtitle visibility controls the subtitle that renders below the balloon part of the marker. The default value is [`Adaptive`](featurevisibility/adaptive.md).

For adaptive visibility, the subtitle is always hidden in the normal state, by default. In the selected state, the subtitle follows the same rules as the title.

## See Also

- [color](markerannotationconstructoroptions/color.md)
  The background color of the balloon.
- [glyphColor](markerannotationconstructoroptions/glyphcolor.md)
  The fill color of the glyph.
- [glyphText](markerannotationconstructoroptions/glyphtext.md)
  The text to display in the marker balloon.
- [glyphImage](markerannotationconstructoroptions/glyphimage.md)
  The image to display in the marker balloon.
- [selectedGlyphImage](markerannotationconstructoroptions/selectedglyphimage.md)
  The image to display in the balloon when the user selects the marker.
- [titleVisibility](markerannotationconstructoroptions/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/subtitlevisibility)*