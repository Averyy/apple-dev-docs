# twoPieceImageForeground

**Framework**: ClockKit  
**Kind**: property

The foreground image in a two-piece image.

**Availability**:
- watchOS 2.0+

## Declaration

```swift
var twoPieceImageForeground: UIImage? { get set }
```

#### Discussion

The image you specified is tinted white and composited on top of the background image. This image is used only in multicolor environments. You may specify `nil` for this image if you want to display only the background image, but in that case it’s better to use a one-piece image instead.

The image you specify for this property must be a template image—that is, an image where you convey the desired shape using only the alpha channel of the image. The color channels of the image are ignored. Fully and partially opaque areas of the template image are tinted using the appropriate tint color, which is determined by the clock face.

The image provider scales your image as needed to fit the target template. For information about the image sizes to use in different templates, see [`Apple Watch Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/watch/human-interface-guidelines/).

## See Also

- [convenience init(onePieceImage: UIImage, twoPieceImageBackground: UIImage?, twoPieceImageForeground: UIImage?)](clkimageprovider/init(onepieceimage:twopieceimagebackground:twopieceimageforeground:).md)
  Creates and returns an image provider with both one-piece and two-piece images.
- [var onePieceImage: UIImage](clkimageprovider/onepieceimage.md)
  The template image to use as a one-piece image.
- [var tintColor: UIColor?](clkimageprovider/tintcolor.md)
  The tint color to apply to the image in a multicolor clock face.
- [var twoPieceImageBackground: UIImage?](clkimageprovider/twopieceimagebackground.md)
  The background image in a two-piece image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/twopieceimageforeground)*