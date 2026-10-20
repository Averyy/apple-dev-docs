# onePieceImage

**Framework**: ClockKit  
**Kind**: property  
**Role**: Instance Property

The template image to use as a one-piece image.

**Availability**:
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: On watchOS 9.0 or later, use WidgetKit instead

## Declaration

```swift
var onePieceImage: UIImage { get set }
```

```objc
@property (nonatomic, retain) UIImage * onePieceImage;
```

#### Discussion

The one-piece image is used in multicolor environments when no two-piece image is available. The one-piece image is always used in monochrome environments. This property must not be `nil`.

The image you specify for this property must be a template image—that is, an image where you convey the desired shape using only the alpha channel of the image. The color channels of the image are ignored. Fully and partially opaque areas of the template image are tinted using the appropriate tint color, which is determined by the clock face.

The image provider scales your image as needed to fit the target template. For information about the image sizes to use in different templates, see [Apple Watch Human Interface Guidelines](https://developer.apple.com/watch/human-interface-guidelines/).

## See Also

### Getting the Image Data
- [var tintColor: UIColor?](./tintcolor.md)
  The tint color to apply to the image in a multicolor clock face.
- [var twoPieceImageBackground: UIImage?](./twopieceimagebackground.md)
  The background image in a two-piece image.
- [var twoPieceImageForeground: UIImage?](./twopieceimageforeground.md)
  The foreground image in a two-piece image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkimageprovider/onepieceimage)*