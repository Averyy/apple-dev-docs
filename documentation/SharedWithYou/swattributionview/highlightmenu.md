# highlightMenu

**Framework**: Shared with You  
**Kind**: property  
**Role**: Instance Property

A menu with a list of system actions specific to this hightlight.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var highlightMenu: UIMenu { get }
```

*macOS*

```swift
var highlightMenu: NSMenu { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, strong, readonly) UIMenu * highlightMenu;
```

*macOS*

```objc
@property (nonatomic, strong, readonly) NSMenu * highlightMenu;
```

## Discussion

Use this menu to augment an existing menu that the system attaches to the content represented by this [`SWAttributionView`](../swattributionview.md). This menu allows the user to reply to or hide the highlight. Your app needs to add this `hightlightMenu` inline with, and at the end of, the menu elements it augments.

## See Also

### Customizing highlights
- [var backgroundStyle: SWAttributionView.BackgroundStyle](./backgroundstyle-swift.property.md)
  The background style of the child view that contains names and avatars.
- [var displayContext: SWAttributionView.DisplayContext](./displaycontext-swift.property.md)
  The context for the content the system displays with this view.
- [var highlight: SWHighlight?](./highlight.md)
  The highlight you use to display this attribution.
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

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/swattributionview/highlightmenu)*