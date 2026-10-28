# glyphText

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

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
var glyphText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * glyphText;
```

## Discussion

Use this property or the [`glyphText`](./glyphtext.md) property to specify the marker balloon content. If you specify both an image and text, MapKit displays the text.

MapKit limits the amount of space available for displaying your glyph text. Specify no more than two or three characters for any strings you assign to this property.

## See Also

### Setting the Marker Content
- [var glyphImage: UIImage?](./glyphimage.md)
  An image to display in the marker balloon.
- [var glyphTintColor: UIColor?](./glyphtintcolor.md)
  The color to apply to the glyph text or image.
- [var selectedGlyphImage: UIImage?](./selectedglyphimage.md)
  An image to display when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphtext)*