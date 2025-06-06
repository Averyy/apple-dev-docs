# contentInsets

**Framework**: UIKit  
**Kind**: property

The distances the edges of content are inset from the printing rectangle.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var contentInsets: UIEdgeInsets { get set }
```

#### Discussion

This property adjusts the margins for content printed by the formatter. The printing rectangle defines the area the printer is capable of printing in; each inset is an inward distance, in points, from a side of the printing area. The top inset is used only on the first page that the formatter draws. The bottom inset is not used. You can use the [`init(top:left:bottom:right:)`](uiedgeinsets/init(top:left:bottom:right:)-1s1t9.md) macro to create a [`UIEdgeInsets`](uiedgeinsets.md) structure.

The default value of this property is [`zero`](uiedgeinsets/zero.md).

## See Also

- [var perPageContentInsets: UIEdgeInsets](uiprintformatter/perpagecontentinsets.md)
  The margins for each printed page.
- [var maximumContentHeight: CGFloat](uiprintformatter/maximumcontentheight.md)
  The maximum height of the content area.
- [var maximumContentWidth: CGFloat](uiprintformatter/maximumcontentwidth.md)
  The maximum width of the content area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintformatter/contentinsets)*