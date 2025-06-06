# MarkerAnnotationConstructorOptions

**Framework**: MapKit JS  
**Kind**: struct

An object containing the options that create a marker annotation.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
dictionary MarkerAnnotationConstructorOptions {
	string titleVisibility;
	string subtitleVisibility;
	string color;
	string glyphColor;
	string glyphText;
	Object glyphImage;
	Object selectedGlyphImage;
};
```

## Topics

### Setting marker annotation properties
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
- [titleVisibility](markerannotationconstructoroptions/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.

## See Also

- [mapkit.MarkerAnnotation](mapkit.markerannotation/mapkit.markerannotation.md)
  Creates a marker annotation at the coordinate location with provided options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/markerannotationconstructoroptions)*