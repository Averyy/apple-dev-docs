# glyphImage

**Framework**: MapKit JS  
**Kind**: property

The glyph image for the place.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
get glyphImage(): MapFeatureAnnotationGlyphImage | null;
```

#### Discussion

Not all places have a glyph image. When a place does, this property returns a [`MapFeatureAnnotationGlyphImage`](mapfeatureannotationglyphimage.md) object that allows you to access the glyph image. You can’t set the glyph image property of the place annotation.

## See Also

- [title](mapfeatureannotation/title.md)
  The title of the feature.
- [featureType](mapfeatureannotation/featuretype.md)
  A value that describes the type of place the feature represents.
- [pointOfInterestCategory](mapfeatureannotation/pointofinterestcategory.md)
  The point-of-interest category of the feature.
- [color](placeannotation/color.md)
  The color of the place.
- [selectedGlyphImage](placeannotation/selectedglyphimage.md)
  The selected glyph image for the place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placeannotation/glyphimage)*