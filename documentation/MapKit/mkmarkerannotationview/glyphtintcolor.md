# glyphTintColor

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The color to apply to the glyph text or image.

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
var glyphTintColor: UIColor? { get set }
```

*macOS*

```swift
@NSCopying
var glyphTintColor: NSColor? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) UIColor * glyphTintColor;
```

*macOS*

```objc
@property (nonatomic, copy, nullable) NSColor * glyphTintColor;
```

#### Discussion

The default value of this property is `nil`, which applies the standard tint color for the current map style.

## See Also

### Setting the Marker Content
- [var glyphText: String?](./glyphtext.md)
  The text to display in the marker balloon.
- [var glyphImage: UIImage?](./glyphimage.md)
  An image to display in the marker balloon.
- [var selectedGlyphImage: UIImage?](./selectedglyphimage.md)
  An image to display when the user selects the marker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmarkerannotationview/glyphtintcolor)*