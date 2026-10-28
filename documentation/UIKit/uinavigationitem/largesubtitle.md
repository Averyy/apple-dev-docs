# largeSubtitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

String to be rendered below the large title.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var largeSubtitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * largeSubtitle;
```

## Discussion

When `nil`, the navigation bar will fall back to the `subtitle`.

## See Also

### Configuring the subtitle
- [var subtitle: String?](./subtitle.md)
  A string to display as the subtitle in the navigation bar.
- [var attributedSubtitle: AttributedString?](./attributedsubtitle-wrjk.md)
- [var largeAttributedSubtitle: AttributedString?](./largeattributedsubtitle-4z2gx.md)
- [attributedSubtitle](./attributedsubtitle-4474c.md)
  An attributed string to display as the subtitle in the navigation bar.
- [largeAttributedSubtitle](./largeattributedsubtitle-2c0pk.md)
  An attributed string to be rendered below the large title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largesubtitle)*