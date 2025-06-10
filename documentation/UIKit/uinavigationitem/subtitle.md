# subtitle

**Framework**: UIKit  
**Kind**: property

A string to display as the subtitle in the navigation bar.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
var subtitle: String? { get set }
```

#### Discussion

If `attributedSubtitle` is `non-nil`, this property just returns the `String` representation of the `attributedString`. If `subtitleView` is non-nil, this property is ignored.

## See Also

- [var attributedSubtitle: AttributedString?](uinavigationitem/attributedsubtitle-wrjk.md)
- [var largeSubtitle: String?](uinavigationitem/largesubtitle.md)
  String to be rendered below the large title.
- [var largeAttributedSubtitle: AttributedString?](uinavigationitem/largeattributedsubtitle-4z2gx.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uinavigationitem/subtitle)*