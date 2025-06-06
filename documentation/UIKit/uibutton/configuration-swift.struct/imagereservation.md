# imageReservation

**Framework**: UIKit  
**Kind**: property

A value that reserves space for the image in the same axis as the edge against which the button places the image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var imageReservation: CGFloat { get set }
```

#### Discussion

Defaults to `0`. The value reserves space in the axis that corresponds to [`imagePlacement`](uibuttonconfiguration/imageplacement.md). If the image is larger than the reservation value in that axis, the system ignores the reservation value. Otherwise, the system centers the image in the space that the reservation value provides.

If the image is a symbol image, the system scales the reservation value with dynamic type, based on the image configuration.

## See Also

- [var image: UIImage?](uibutton/configuration-swift.struct/image.md)
  The foreground image the button displays.
- [var imagePadding: CGFloat](uibutton/configuration-swift.struct/imagepadding.md)
  The distance between the button’s image and text.
- [var imagePlacement: NSDirectionalRectEdge](uibutton/configuration-swift.struct/imageplacement.md)
  The edge against which the button places the image.
- [var imageColorTransformer: UIConfigurationColorTransformer?](uibutton/configuration-swift.struct/imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration?](uibutton/configuration-swift.struct/preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/imagereservation)*