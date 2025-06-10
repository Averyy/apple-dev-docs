# maximumImageSize

**Framework**: CarPlay  
**Kind**: property

The maximum size of a list item’s image and accessory image.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
class var maximumImageSize: CGSize { get }
```

#### Discussion

At runtime, use this value to determine the maximum size for a list item’s image and accessory image.

## See Also

- [var text: String?](cplistitem/text.md)
  The list item’s primary text.
- [func setText(String)](cplistitem/settext(_:).md)
  Updates the list item’s primary text.
- [var detailText: String?](cplistitem/detailtext.md)
  The list item’s secondary text.
- [func setDetailText(String?)](cplistitem/setdetailtext(_:).md)
  Updates the list item’s secondary text.
- [var image: UIImage?](cplistitem/image.md)
  The image that the list item displays in its leading region.
- [func setImage(UIImage?)](cplistitem/setimage(_:).md)
  Updates the list item’s image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistitem/maximumimagesize)*