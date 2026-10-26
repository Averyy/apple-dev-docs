# attributedSubtitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An attributed string to display as the subtitle in the navigation bar.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedSubtitle;
```

#### Discussion

If non-nil, this property takes precedence over the `subtitle` property. If `subtitleView` is non-nil, this property is ignored. If `titleView` is non-nil, this property is ignored.

## See Also

### Configuring the subtitle
- [var subtitle: String?](./subtitle.md)
  A string to display as the subtitle in the navigation bar.
- [var largeSubtitle: String?](./largesubtitle.md)
  String to be rendered below the large title.
- [largeAttributedSubtitle](./largeattributedsubtitle-2c0pk.md)
  An attributed string to be rendered below the large title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/attributedsubtitle-4474c)*