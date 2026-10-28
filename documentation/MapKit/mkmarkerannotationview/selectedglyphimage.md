# selectedGlyphImage

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

An image to display when the user selects the marker.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
@NSCopying
var selectedGlyphImage: UIImage? { get set }
```

*macOS*

```swift
@NSCopying
var selectedGlyphImage: NSImage? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) UIImage * selectedGlyphImage;
```

*macOS*

```objc
@property (nonatomic, copy, nullable) NSImage * selectedGlyphImage;
```

## Discussion

MapKit displays the glyph image when the marker is in the selected state. If you specify an image for this property, you should also specify an image in the [`glyphImage`](./glyphimage.md) property.

Create glyph images as template images so that MapKit can apply the glyph tint color to the image. Set the size of this image to 40 by 40 points on iOS and 60 by 40 points on tvOS. MapKit scales images that are larger or smaller than those sizes.

## See Also

### Setting the Marker Content
- [var glyphText: String?](./glyphtext.md)
  The text to display in the marker balloon.
- [var glyphImage: UIImage?](./glyphimage.md)
  An image to display in the marker balloon.
- [var glyphTintColor: UIColor?](./glyphtintcolor.md)
  The color to apply to the glyph text or image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/selectedglyphimage)*