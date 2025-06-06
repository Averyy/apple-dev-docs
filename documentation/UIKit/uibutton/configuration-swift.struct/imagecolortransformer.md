# imageColorTransformer

**Framework**: UIKit  
**Kind**: property

A block that transforms the image color when the button state changes.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var imageColorTransformer: UIConfigurationColorTransformer? { get set }
```

#### Discussion

Use this property to transform an image to, for example, a monochrome or tinted image.

## See Also

- [var image: UIImage?](uibutton/configuration-swift.struct/image.md)
  The foreground image the button displays.
- [var imagePadding: CGFloat](uibutton/configuration-swift.struct/imagepadding.md)
  The distance between the button’s image and text.
- [var imagePlacement: NSDirectionalRectEdge](uibutton/configuration-swift.struct/imageplacement.md)
  The edge against which the button places the image.
- [var imageReservation: CGFloat](uibutton/configuration-swift.struct/imagereservation.md)
  A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration?](uibutton/configuration-swift.struct/preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/imagecolortransformer)*