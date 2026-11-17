# setImage(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Updates the leading image of the list item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setImage(_ image: UIImage?)
```

```objc
- (void) setImage:(UIImage *) image;
```

## Parameters

- `image`: An image to display on the leading edge of the list item’s row. If the image originates from an asset catalog, CarPlay manages light and dark variants of your image and switches them when needed. Specify images with the dimensions listed in the [`maximumImageSize`](./maximumimagesize.md) property. If your image is smaller or larger than the maximum dimensions, CarPlay scales the image as needed to fit the space. Don’t specify an image object with an animated sequence of images.

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
- [var userInfo: Any?](./userinfo.md)
  App-specific data you associate with the item.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum dimensions for the list item images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/setimage(_:))*