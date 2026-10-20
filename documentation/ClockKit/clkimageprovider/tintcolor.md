# tintColor

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The tint color to apply to the image in a multicolor clock face.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var tintColor: UIColor? { get set }
```

```objc
@property (nonatomic, retain, nullable) UIColor * tintColor;
```

#### Discussion

For multicolor clock faces, the image provider applies the color in this property to the underlying image. For one-piece images, the color is applied directly to the image. For two-piece images, the color is applied only to the background image.

Specify `nil` to tint the image using the color of the complication template object. If the template doesn’t specify a color, the default color (white) is used.

## See Also

### Getting the Image Data
- [var onePieceImage: UIImage](./onepieceimage.md)
  The template image to use as a one-piece image.
- [var twoPieceImageBackground: UIImage?](./twopieceimagebackground.md)
  The background image in a two-piece image.
- [var twoPieceImageForeground: UIImage?](./twopieceimageforeground.md)
  The foreground image in a two-piece image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/tintcolor)*