# glyphImage

**Framework**: MapKit  
**Kind**: property

An image to display in the marker balloon.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
@MainActor var glyphImage: UIImage? { get set }
```

#### Discussion

Use this property or the [`glyphText`](mkmarkerannotationview/glyphtext.md) property to specify the marker balloon content. If you specify both an image and text, MapKit displays the text.

MapKit displays the glyph image when the marker is in the normal state. Create glyph images as template images so that MapKit can apply the glyph tint color to the image. Normally, you set the size of this image to 20 by 20 points on iOS and 40 by 40 points on tvOS. However, if you don’t provide a separate selected image in the [`selectedGlyphImage`](mkmarkerannotationview/selectedglyphimage.md) property, make the size of this image 40 by 40 points on iOS and 60 by 40 points on tvOS instead. MapKit scales images that are larger or smaller than those sizes.

## See Also

- [var glyphText: String?](mkmarkerannotationview/glyphtext.md)
  The text to display in the marker balloon.
- [var glyphTintColor: UIColor?](mkmarkerannotationview/glyphtintcolor.md)
  The color to apply to the glyph text or image.
- [var selectedGlyphImage: UIImage?](mkmarkerannotationview/selectedglyphimage.md)
  An image to display when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphimage)*