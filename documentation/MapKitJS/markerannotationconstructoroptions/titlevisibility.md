# titleVisibility

**Framework**: MapKit JS  
**Kind**: property

A value that determines the behavior of the title’s visibility.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
titleVisibility?: FeatureVisibility;
```

#### Discussion

The title visibility controls the title that renders below the balloon part of the marker. The default value is [`Adaptive`](featurevisibility/adaptive.md).

For adaptive visibility, the title is always visible in the normal state, by default. When the user selects the marker, the title is visible unless the marker’s selected state requires a callout.

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
- [subtitleVisibility](markerannotationconstructoroptions/subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/titlevisibility)*