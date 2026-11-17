# trailingText

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Additional text to display after the trailing configuration items.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var trailingText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * trailingText;
```

## Discussion

Specify the trailing text at initialization time. CarPlay places the text after any content from the [`trailingConfiguration`](./trailingconfiguration.md) property.

## See Also

### Getting the row content
- [var text: String?](./text.md)
  The primary text to display in the message list item’s row.
- [var detailText: String?](./detailtext.md)
  Additional text to display less prominently below the row’s main text.
- [var leadingDetailTextImage: UIImage?](./leadingdetailtextimage.md)
  An image to display before the row’s detail text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/trailingtext)*