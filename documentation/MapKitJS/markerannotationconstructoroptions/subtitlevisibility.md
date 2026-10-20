# subtitleVisibility

**Framework**: MapKit JS  
**Kind**: property  
**Role**: Interface Property

A value that determines the behavior of the subtitle’s visibility.

**Availability**:
- MapKit JS 5.0+

## Declaration

```
subtitleVisibility?: FeatureVisibility;
```

#### Discussion

The subtitle visibility controls the subtitle that renders below the balloon part of the marker. The default value is [`Adaptive`](../featurevisibility/adaptive.md).

For adaptive visibility, the subtitle is always hidden in the normal state, by default. In the selected state, the subtitle follows the same rules as the title.

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
- [selectedGlyphImage](./selectedglyphimage.md)
  The image to display in the balloon when the user selects the marker.
- [titleVisibility](./titlevisibility.md)
  A value that determines the behavior of the title’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions/subtitlevisibility)*