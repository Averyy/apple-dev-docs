# perPageContentInsets

**Framework**: UIKit  
**Kind**: property

The margins for each printed page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var perPageContentInsets: UIEdgeInsets { get set }
```

#### Discussion

This property specifies the margins to apply to each printed page. All margins are respected, so the top inset value represents the top margin of every page, the left inset value represents the left margin of every page, and so on. If the per-page insets are smaller than the printable area of the page, or smaller than the printable area after the values in the [`contentInsets`](uiprintformatter/contentinsets.md) property are applied, the value in this property is effectively ignored.

The default value of this property is [`zero`](uiedgeinsets/zero.md).

## See Also

- [var maximumContentHeight: CGFloat](uiprintformatter/maximumcontentheight.md)
  The maximum height of the content area.
- [var maximumContentWidth: CGFloat](uiprintformatter/maximumcontentwidth.md)
  The maximum width of the content area.
- [var contentInsets: UIEdgeInsets](uiprintformatter/contentinsets.md)
  The distances the edges of content are inset from the printing rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/perpagecontentinsets)*