# text

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The primary text for the list item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var text: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * text;
```

## Discussion

CarPlay displays this text prominently in the row, starting at the leading edge. To change the value of this property after creating the list item, call the [`setText(_:)`](./settext%28_%29.md) method.

## See Also

### Managing the row’s content
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
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum dimensions for the list item images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/text)*