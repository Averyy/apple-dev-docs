# selectedGlyphImage

**Framework**: MapKit JS  
**Kind**: property

The image to display in the marker balloon when the user selects the marker.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute Object|ImageDelegate selectedGlyphImage;
```

## Mentions

- [MapKit JS 5](mapkit-js-5.md)

#### Discussion

Glyph image values are object literals that contain absolute or relative URLs to standard, `@2x`, and `@3x` assets. Alternatively, you can set an [`ImageDelegate`](imagedelegate.md), which is an object you use to specify image URLs.

The framework requires at least one image and displays the selected glyph image in the balloon when the marker is in the selected state. If you specify an image for this property, also specify an image in the [`glyphImage`](mapkit.markerannotation/glyphimage.md) property.

Set the size of the selected glyph image to 40 x 40 pixels. Create glyph images as template images — a monochrome image with opacity, if needed — so that MapKit JS can apply the [`glyphColor`](mapkit.markerannotation/glyphcolor.md) to tint to the image. MapKit JS scales glyph images to fit in the balloon. If you don’t set [`selectedGlyphImage`](mapkit.markerannotation/selectedglyphimage.md), the framework uses [`glyphImage`](mapkit.markerannotation/glyphimage.md) when the user selects the marker. The default image is a pin.

## See Also

- [glyphText](mapkit.markerannotation/glyphtext.md)
  The text to display in the marker balloon.
- [glyphImage](mapkit.markerannotation/glyphimage.md)
  The image to display in the marker balloon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.markerannotation/selectedglyphimage)*