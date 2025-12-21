# glyphTintColor

**Framework**: MapKit  
**Kind**: property

The color to apply to the glyph text or image.

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
@MainActor var glyphTintColor: NSColor? { get set }
```

#### Discussion

The default value of this property is `nil`, which applies the standard tint color for the current map style.

## See Also

- [var glyphText: String?](mkmarkerannotationview/glyphtext.md)
  The text to display in the marker balloon.
- [var glyphImage: UIImage?](mkmarkerannotationview/glyphimage.md)
  An image to display in the marker balloon.
- [var selectedGlyphImage: UIImage?](mkmarkerannotationview/selectedglyphimage.md)
  An image to display when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphtintcolor)*