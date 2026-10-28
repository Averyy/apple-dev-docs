# maximumImageSize

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum size of a list item’s image and accessory image.

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

At runtime, use this value to determine the maximum size for a list item’s image and accessory image.

## See Also

### Managing Content
- [var text: String?](./text.md)
  The list item’s primary text.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/maximumimagesize)*