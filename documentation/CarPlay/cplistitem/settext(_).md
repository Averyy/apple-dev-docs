# setText(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Updates the primary text of the list item.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func setText(_ text: String)
```

```objc
- (void) setText:(NSString *) text;
```

## Parameters

- `text`: The primary text to show in the list item’s row.

## See Also

### Managing the row’s content
- [var text: String?](./text.md)
  The primary text for the list item.
- [var detailText: String?](./detailtext.md)
  The secondary text for the list item.
- [var image: UIImage?](./image.md)
  The image to display on the leading edge of the cell.
- [func setDetailText(String?)](./setdetailtext%28_%29.md)
  Updates the secondary text of the list item.
- [func setImage(UIImage?)](./setimage%28_%29.md)
  Updates the leading image of the list item.
- [var userInfo: Any?](./userinfo.md)
  App-specific data you associate with the item.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum dimensions for the list item images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/settext(_:))*