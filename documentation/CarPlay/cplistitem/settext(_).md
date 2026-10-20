# setText(_:)

**Framework**: CarPlay  
**Kind**: method  
**Role**: Instance Method

Updates the list item’s primary text.

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

- `text`: The list item’s primary text.

## See Also

### Managing Content
- [var text: String?](./text.md)
  The list item’s primary text.
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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/settext(_:))*