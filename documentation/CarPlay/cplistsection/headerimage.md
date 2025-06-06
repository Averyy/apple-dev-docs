# headerImage

**Framework**: CarPlay  
**Kind**: property

An image that the section header displays.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@NSCopying
var headerImage: UIImage? { get set }
```

#### Discussion

The maximum size of the section header image is [`CPMaximumListSectionImageSize`](cpmaximumlistsectionimagesize.md).

Provide a [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) that is display-ready. To provide an image that includes light and dark styles, use an asset from your asset catalog that includes both styles, or use a [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) to combine two [`UIImage`](https://developer.apple.com/documentation/UIKit/UIImage) instances into a single image with both styles.

To size your header image properly, consider the display scale of the car screen. Use [`UIImageAsset`](https://developer.apple.com/documentation/UIKit/UIImageAsset) to combine multiple images with different trait collections into a single image. For more information about trait collections for CarPlay, see [`carTraitCollection`](cpinterfacecontroller/cartraitcollection.md).

## See Also

- [var headerButton: CPButton?](cplistsection/headerbutton.md)
  A button that the section header displays.
- [var headerSubtitle: String?](cplistsection/headersubtitle.md)
  A string that the header displays as a subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/headerimage)*