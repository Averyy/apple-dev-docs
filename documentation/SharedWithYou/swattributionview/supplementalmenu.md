# supplementalMenu

**Framework**: Shared with You  
**Kind**: property

A supplemental menu to augment the attribution view’s existing menu.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var supplementalMenu: NSMenuItem? { get set }
```

#### Discussion

Use `supplementalMenu` when there are additional actions a user can take on content represented by this view’s [`SWHighlight`](swhighlight.md). A `nil` value informs the system to not add a supplemental menu.

## See Also

- [var backgroundStyle: SWAttributionView.BackgroundStyle](swattributionview/backgroundstyle-swift.property.md)
  The background style of the child view that contains names and avatars.
- [var displayContext: SWAttributionView.DisplayContext](swattributionview/displaycontext-swift.property.md)
  The context for the content the system displays with this view.
- [var highlight: SWHighlight?](swattributionview/highlight.md)
  The highlight you use to display this attribution.
- [var highlightMenu: UIMenu](swattributionview/highlightmenu.md)
  A menu with a list of system actions specific to this hightlight.
- [var horizontalAlignment: SWAttributionView.HorizontalAlignment](swattributionview/horizontalalignment-swift.property.md)
  The horizontal alignment of the view.
- [var menuTitleForHideAction: String?](swattributionview/menutitleforhideaction.md)
  A localized string the system uses as a custom title for the hide menu item.
- [var preferredMaxLayoutWidth: CGFloat](swattributionview/preferredmaxlayoutwidth.md)
  A width the system uses to constrain the view contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swattributionview/supplementalmenu)*