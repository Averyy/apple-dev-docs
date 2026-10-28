# displayContext

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

The context for the content the system displays with this view.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var displayContext: SWAttributionView.DisplayContext { get set }
```

```objc
@property (nonatomic, assign, readwrite) SWAttributionViewDisplayContext displayContext;
```

## Discussion

Set the `displayContext` prior to adding this view to your view hierarchy.

## See Also

### Customizing highlights
- [var backgroundStyle: SWAttributionView.BackgroundStyle](./backgroundstyle-swift.property.md)
  The background style of the child view that contains names and avatars.
- [var highlight: SWHighlight?](./highlight.md)
  The highlight you use to display this attribution.
- [var highlightMenu: UIMenu](./highlightmenu.md)
  A menu with a list of system actions specific to this hightlight.
- [var horizontalAlignment: SWAttributionView.HorizontalAlignment](./horizontalalignment-swift.property.md)
  The horizontal alignment of the view.
- [var menuTitleForHideAction: String?](./menutitleforhideaction.md)
  A localized string the system uses as a custom title for the hide menu item.
- [var preferredMaxLayoutWidth: CGFloat](./preferredmaxlayoutwidth.md)
  A width the system uses to constrain the view contents.
- [var supplementalMenu: UIMenu?](./supplementalmenu.md)
  A supplemental menu to augment the attribution view’s existing menu.
- [enablesMarquee](./enablesmarquee.md)
  Automatically enables a marquee effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swattributionview/displaycontext-swift.property)*