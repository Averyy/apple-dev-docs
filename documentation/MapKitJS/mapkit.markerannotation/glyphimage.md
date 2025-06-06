# glyphImage

**Framework**: MapKit JS  
**Kind**: property

The image to display in the marker balloon.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute Object|ImageDelegate glyphImage;
```

#### Discussion

Glyph image values are object literals that contain absolute or relative URLs to standard, `@2x`, and `@3x` assets. Alternatively, you can set an [`ImageDelegate`](imagedelegate.md), which is an object you use to specify image URLs.

The framework requires at least one image at 20 x 20 pixels. Create glyph images as template images — a monochrome image with opacity, if needed — so that MapKit JS can apply the [`glyphColor`](mapkit.markerannotation/glyphcolor.md) to tint to the image.

If you set [`glyphImage`](markerannotationconstructoroptions/glyphimage.md) to `null`, `undefined`, or “” (an empty string), MapKit JS uses the default glyph image of a pin. If you specify both a [`glyphImage`](mapkit.markerannotation/glyphimage.md) and [`glyphText`](mapkit.markerannotation/glyphtext.md), MapKit JS ignores the glyph image, and the framework displays glyph text.

## See Also

- [glyphText](mapkit.markerannotation/glyphtext.md)
  The text to display in the marker balloon.
- [selectedGlyphImage](mapkit.markerannotation/selectedglyphimage.md)
  The image to display in the marker balloon when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.markerannotation/glyphimage)*