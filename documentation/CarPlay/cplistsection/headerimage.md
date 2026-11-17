# headerImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image to display in the header area of the section.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+

## Declaration

```swift
@NSCopying
var headerImage: UIImage? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIImage * headerImage;
```

## Discussion

This property contains the image you specified at initialization time. If you assign a new image to this property, create your [`UIImage`](../../UIKit/uiimage.md) type with an asset catalog resource whenever possible. From the asset catalog resources, CarPlay chooses the appropriate image resource automatically. For example, CarPlay chooses the light and dark variant of your image to match the vehicle settings.

The [`CPMaximumListSectionImageSize`](../cpmaximumlistsectionimagesize.md) constant contains the maximum supported size for images. To get the maximum image dimensions in pixels, multiple the maximum size values by the scale factor in the [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## See Also

### Getting the section’s header content
- [var header: String?](./header.md)
  The main text to display in the header area of the section.
- [var headerSubtitle: String?](./headersubtitle.md)
  The secondary text to display in the header area of the section.
- [var headerButton: CPButton?](./headerbutton.md)
  The button to display in the header area of the section.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistsection/headerimage)*