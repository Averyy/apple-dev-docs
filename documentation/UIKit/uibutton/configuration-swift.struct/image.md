# image

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The foreground image the button displays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
var image: UIImage? { get set }
```

#### Discussion

A configuration contains one image. To change the image based on button state, use [`configurationUpdateHandler`](../configurationupdatehandler-swift.property.md) or [`updateConfiguration()`](../updateconfiguration%28%29.md).

## See Also

### Configuring images
- [var imagePadding: CGFloat](./imagepadding.md)
  The distance between the button’s image and text.
- [var imagePlacement: NSDirectionalRectEdge](./imageplacement.md)
  The edge against which the button places the image.
- [var imageReservation: CGFloat](./imagereservation.md)
  A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [var imageColorTransformer: UIConfigurationColorTransformer?](./imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration?](./preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/image)*