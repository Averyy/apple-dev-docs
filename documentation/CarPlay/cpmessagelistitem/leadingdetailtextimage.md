# leadingDetailTextImage

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

An image to display before the row’s detail text.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@NSCopying
var leadingDetailTextImage: UIImage? { get set }
```

```objc
@property (nonatomic, copy, nullable) UIImage * leadingDetailTextImage;
```

## Discussion

CarPlay places the image in front of the text in [`detailText`](./detailtext.md) and on the same line. If you specify an image larger or smaller than [`CPMaximumMessageItemLeadingDetailTextImageSize`](../cpmaximummessageitemleadingdetailtextimagesize.md), CarPlay scales your image to those dimensions. Use the image to add a visual element for your conversation or contact. For example, if you display the person’s phone number in the detail text, you might display an icon to indicate whether it’s their home or cellular phone.

## See Also

### Getting the row content
- [var text: String?](./text.md)
  The primary text to display in the message list item’s row.
- [var detailText: String?](./detailtext.md)
  Additional text to display less prominently below the row’s main text.
- [var trailingText: String?](./trailingtext.md)
  Additional text to display after the trailing configuration items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/leadingdetailtextimage)*