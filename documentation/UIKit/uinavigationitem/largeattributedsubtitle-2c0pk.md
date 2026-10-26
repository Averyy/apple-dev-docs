# largeAttributedSubtitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An attributed string to be rendered below the large title.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) NSAttributedString * largeAttributedSubtitle;
```

#### Discussion

When `nil`, the navigation bar will fall back to the `largeSubtitle`. If a `largeSubtitleView` is set, this property is ignored.

## See Also

### Configuring the subtitle
- [var subtitle: String?](./subtitle.md)
  A string to display as the subtitle in the navigation bar.
- [attributedSubtitle](./attributedsubtitle-4474c.md)
  An attributed string to display as the subtitle in the navigation bar.
- [var largeSubtitle: String?](./largesubtitle.md)
  String to be rendered below the large title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/largeattributedsubtitle-2c0pk)*