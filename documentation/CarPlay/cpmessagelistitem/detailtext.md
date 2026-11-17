# detailText

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

Additional text to display less prominently below the row’s main text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
var detailText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * detailText;
```

## Discussion

Specify the detail text at initialization time.

## See Also

### Getting the row content
- [var text: String?](./text.md)
  The primary text to display in the message list item’s row.
- [var trailingText: String?](./trailingtext.md)
  Additional text to display after the trailing configuration items.
- [var leadingDetailTextImage: UIImage?](./leadingdetailtextimage.md)
  An image to display before the row’s detail text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagelistitem/detailtext)*