# maximumImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum dimensions for the list item images.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class var maximumImageSize: CGSize { get }
```

```objc
@property (class, nonatomic, readonly) CGSize maximumImageSize;
```

## Discussion

This property contains the maximum permissible dimensions, in points, for the images in the [`image`](./image.md) and [`accessoryImage`](./accessoryimage.md) properties. When creating images for your items, use this information to determine the maximum size of your images.

To determine the maximum pixel dimensions for images, multiply the value in this property by the current scale factor for your CarPlay interface. Get the interface scale factor from the traits in the [`carTraitCollection`](../cpinterfacecontroller/cartraitcollection.md) property of your interface controller.

## See Also

### Managing the row’s content
- [var text: String?](./text.md)
  The primary text for the list item.
- [var detailText: String?](./detailtext.md)
  The secondary text for the list item.
- [var image: UIImage?](./image.md)
  The image to display on the leading edge of the cell.
- [func setText(String)](./settext%28_%29.md)
  Updates the primary text of the list item.
- [func setDetailText(String?)](./setdetailtext%28_%29.md)
  Updates the secondary text of the list item.
- [func setImage(UIImage?)](./setimage%28_%29.md)
  Updates the leading image of the list item.
- [var userInfo: Any?](./userinfo.md)
  App-specific data you associate with the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/maximumimagesize)*