# userInfo

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

App-specific data you associate with the item.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var userInfo: Any? { get set }
```

```objc
@property (nonatomic, strong, nullable) id userInfo;
```

## Discussion

Use this property to attach app-specific data to the list item. For example, you might attach the model object from your app that corresponds to the list item’s content. This information is just for your app, and CarPlay doesn’t use it. The default value of this property is `nil`.

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
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum dimensions for the list item images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/userinfo)*