# image

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The image to display on the leading edge of the cell.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var image: UIImage? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIImage * image;
```

## Discussion

Use this property to access the image for your row. To change the value of this property after creating the list item, call the [`setImage(_:)`](./setimage%28_%29.md) method.

If your image originates from an asset catalog, CarPlay manages light and dark variants of your image and switches them when needed. If the image is smaller or larger than the dimensions in the [`maximumImageSize`](./maximumimagesize.md) property, CarPlay scales the image as needed to fit the space. Don’t specify an image object with an animated sequence of images.

To change the value of this property after creating the list item, call the [`setImage(_:)`](./setimage%28_%29.md) method.

## See Also

### Managing the row’s content
- [var text: String?](./text.md)
  The primary text for the list item.
- [var detailText: String?](./detailtext.md)
  The secondary text for the list item.
- [func setText(String)](./settext%28_%29.md)
  Updates the primary text of the list item.
- [func setDetailText(String?)](./setdetailtext%28_%29.md)
  Updates the secondary text of the list item.
- [func setImage(UIImage?)](./setimage%28_%29.md)
  Updates the leading image of the list item.
- [var userInfo: Any?](./userinfo.md)
  App-specific data you associate with the item.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum dimensions for the list item images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/image)*