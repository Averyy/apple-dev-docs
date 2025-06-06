# onePieceImage

**Framework**: ClockKit  
**Kind**: property

The template image to use as a one-piece image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var onePieceImage: UIImage { get set }
```

#### Discussion

The one-piece image is used in multicolor environments when no two-piece image is available. The one-piece image is always used in monochrome environments. This property must not be `nil`.

The image you specify for this property must be a template image—that is, an image where you convey the desired shape using only the alpha channel of the image. The color channels of the image are ignored. Fully and partially opaque areas of the template image are tinted using the appropriate tint color, which is determined by the clock face.

The image provider scales your image as needed to fit the target template. For information about the image sizes to use in different templates, see [`Apple Watch Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/watch/human-interface-guidelines/).

## See Also

- [var tintColor: UIColor?](clkimageprovider/tintcolor.md)
  The tint color to apply to the image in a multicolor clock face.
- [var twoPieceImageBackground: UIImage?](clkimageprovider/twopieceimagebackground.md)
  The background image in a two-piece image.
- [var twoPieceImageForeground: UIImage?](clkimageprovider/twopieceimageforeground.md)
  The foreground image in a two-piece image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/onepieceimage)*