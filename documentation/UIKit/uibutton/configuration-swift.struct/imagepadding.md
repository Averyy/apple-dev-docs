# imagePadding

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The distance between the button’s image and text.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS

## Declaration

```swift
var imagePadding: CGFloat { get set }
```

#### Discussion

Use this property to adjust the distance from the title and subtitle. This doesn’t affect the distance to the button’s edge.

## See Also

### Configuring images
- [var image: UIImage?](./image.md)
  The foreground image the button displays.
- [var imagePlacement: NSDirectionalRectEdge](./imageplacement.md)
  The edge against which the button places the image.
- [var imageReservation: CGFloat](./imagereservation.md)
  A value that reserves space for the image in the same axis as the edge against which the button places the image.
- [var imageColorTransformer: UIConfigurationColorTransformer?](./imagecolortransformer.md)
  A block that transforms the image color when the button state changes.
- [var preferredSymbolConfigurationForImage: UIImage.SymbolConfiguration?](./preferredsymbolconfigurationforimage.md)
  A requested configuration object for the button symbol image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/configuration-swift.struct/imagepadding)*