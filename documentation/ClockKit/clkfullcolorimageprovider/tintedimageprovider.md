# tintedImageProvider

**Framework**: ClockKit  
**Kind**: property

An image provider that produces alternative images for tinted graphic complications.

**Availability**:
- watchOS 6.0+

## Declaration

```swift
var tintedImageProvider: CLKImageProvider? { get set }
```

#### Discussion

By default, when the system displays a graphic complication using the tinted mode, it desaturates the full-color image stored in the [`image`](clkfullcolorimageprovider/image.md) property. To provide an alternative template image instead, create an image provider and assign it to the [`tintedImageProvider`](clkfullcolorimageprovider/tintedimageprovider.md) property.

Tinted graphic complications interpret the tinted image provider as follows:

- The graphic complication ignores the [`tintColor`](clkimageprovider/tintcolor.md) property.
- The [`onePieceImage`](clkimageprovider/onepieceimage.md) property returns a single template image. The system sets the image’s color based on the watch-face color the user selected. This property is the only one required to provide tinted images.
- The [`twoPieceImageForeground`](clkimageprovider/twopieceimageforeground.md) and [`twoPieceImageBackground`](clkimageprovider/twopieceimagebackground.md) properties define a two-piece image. Both the foreground and background are template images. The complication layers the foreground image over the background image, and selects the color for both images based on the watch-face color. When applicable, the system displays two-piece images instead of the one-piece images.

## See Also

- [var image: UIImage](clkfullcolorimageprovider/image.md)
  The full-color image to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/clockkit/clkfullcolorimageprovider/tintedimageprovider)*