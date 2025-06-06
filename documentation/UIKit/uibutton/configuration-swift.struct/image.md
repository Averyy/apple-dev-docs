# image

**Framework**: UIKit  
**Kind**: property

The foreground image the button displays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- tvOS 15.0+
- visionOS ?+

## Declaration

```swift
var image: UIImage? { get set }
```

#### Discussion

A configuration contains one image. To change the image based on button state, use [`configurationUpdateHandler`](uibutton/configurationupdatehandler-swift.property.md) or [`updateConfiguration()`](uibutton/updateconfiguration().md).

## See Also

- [var imagePadding: CGFloat](uibutton/configuration-swift.struct/imagepadding.md)
  The distance between the button’s image and text.
- [var imagePlacement: NSDirectionalRectEdge](uibutton/configuration-swift.struct/imageplacement.md)
  The edge against which the button places the image.
- [var imageReservation: CGFloat](uibutton/configuration-swift.struct/imagereservation.md)
  A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [var imageColorTransformer: UIConfigurationColorTransformer?](uibutton/configuration-swift.struct/imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration?](uibutton/configuration-swift.struct/preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/image)*