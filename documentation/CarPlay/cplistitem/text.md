# text

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The list item’s primary text.

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

## See Also

### Managing Content
- [func setText(String)](./settext%28_%29.md)
  Updates the list item’s primary text.
- [var detailText: String?](./detailtext.md)
  The list item’s secondary text.
- [func setDetailText(String?)](./setdetailtext%28_%29.md)
  Updates the list item’s secondary text.
- [var image: UIImage?](./image.md)
  The image that the list item displays in its leading region.
- [func setImage(UIImage?)](./setimage%28_%29.md)
  Updates the list item’s image.
- [class var maximumImageSize: CGSize](./maximumimagesize.md)
  The maximum size of a list item’s image and accessory image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/text)*