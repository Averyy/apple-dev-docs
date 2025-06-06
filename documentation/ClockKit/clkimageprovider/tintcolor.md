# tintColor

**Framework**: ClockKit  
**Kind**: property

The tint color to apply to the image in a multicolor clock face.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var tintColor: UIColor? { get set }
```

#### Discussion

For multicolor clock faces, the image provider applies the color in this property to the underlying image. For one-piece images, the color is applied directly to the image. For two-piece images, the color is applied only to the background image.

Specify `nil` to tint the image using the color of the complication template object. If the template doesn’t specify a color, the default color (white) is used.

## See Also

- [var onePieceImage: UIImage](clkimageprovider/onepieceimage.md)
  The template image to use as a one-piece image.
- [var twoPieceImageBackground: UIImage?](clkimageprovider/twopieceimagebackground.md)
  The background image in a two-piece image.
- [var twoPieceImageForeground: UIImage?](clkimageprovider/twopieceimageforeground.md)
  The foreground image in a two-piece image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/tintcolor)*