# text

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The primary text to display in the message list item’s row.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var text: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * text;
```

## Discussion

CarPlay displays this string prominently in the message list item’s row. If you initialize the message list item with a conversation identifier, this property contains the string from the `text` parameter of the initializer. If you initialize it with a contact, this property contains the contact name.

## See Also

### Getting the row content
- [var detailText: String?](./detailtext.md)
  Additional text to display less prominently below the row’s main text.
- [var trailingText: String?](./trailingtext.md)
  Additional text to display after the trailing configuration items.
- [var leadingDetailTextImage: UIImage?](./leadingdetailtextimage.md)
  An image to display before the row’s detail text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/text)*