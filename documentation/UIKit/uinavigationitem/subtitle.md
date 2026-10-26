# subtitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string to display as the subtitle in the navigation bar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var subtitle: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * subtitle;
```

#### Discussion

If `attributedSubtitle` is `non-nil`, this property just returns the `String` representation of the `attributedString`. If `subtitleView` is non-nil, this property is ignored.

## See Also

### Configuring the subtitle
- [var attributedSubtitle: AttributedString?](./attributedsubtitle-wrjk.md)
- [var largeSubtitle: String?](./largesubtitle.md)
  String to be rendered below the large title.
- [var largeAttributedSubtitle: AttributedString?](./largeattributedsubtitle-4z2gx.md)
- [attributedSubtitle](./attributedsubtitle-4474c.md)
  An attributed string to display as the subtitle in the navigation bar.
- [largeAttributedSubtitle](./largeattributedsubtitle-2c0pk.md)
  An attributed string to be rendered below the large title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/subtitle)*