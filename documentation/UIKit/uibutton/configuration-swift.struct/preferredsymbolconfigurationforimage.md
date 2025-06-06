# preferredSymbolConfigurationForImage

**Framework**: UIKit  
**Kind**: property

A requested configuration object for the button symbol image.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration? { get set }
```

#### Discussion

A symbol configuration defines details such as the point size, scale, text style, weight, and font of symbol image. The button uses these details to determine which variant of the image to use and how to scale or style the image.

## See Also

- [var image: UIImage?](uibutton/configuration-swift.struct/image.md)
  The foreground image the button displays.
- [var imagePadding: CGFloat](uibutton/configuration-swift.struct/imagepadding.md)
  The distance between the button’s image and text.
- [var imagePlacement: NSDirectionalRectEdge](uibutton/configuration-swift.struct/imageplacement.md)
  The edge against which the button places the image.
- [var imageReservation: CGFloat](uibutton/configuration-swift.struct/imagereservation.md)
  A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [var imageColorTransformer: UIConfigurationColorTransformer?](uibutton/configuration-swift.struct/imagecolortransformer.md)
  A block that transforms the image color when the button state changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/preferredsymbolconfigurationforimage)*