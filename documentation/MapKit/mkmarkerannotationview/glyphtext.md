# glyphText

**Framework**: MapKit  
**Kind**: property

The text to display in the marker balloon.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var glyphText: String? { get set }
```

#### Discussion

Use this property or the [`glyphText`](mkmarkerannotationview/glyphtext.md) property to specify the marker balloon content. If you specify both an image and text, MapKit displays the text.

MapKit limits the amount of space available for displaying your glyph text. Specify no more than two or three characters for any strings you assign to this property.

## See Also

- [var glyphImage: UIImage?](mkmarkerannotationview/glyphimage.md)
  An image to display in the marker balloon.
- [var glyphTintColor: UIColor?](mkmarkerannotationview/glyphtintcolor.md)
  The color to apply to the glyph text or image.
- [var selectedGlyphImage: UIImage?](mkmarkerannotationview/selectedglyphimage.md)
  An image to display when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphtext)*