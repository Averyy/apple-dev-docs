# minimumThicknessForInlineSidebars

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum thickness for a sidebar before it automatically collapses.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var minimumThicknessForInlineSidebars: CGFloat { get set }
```

```objc
@property CGFloat minimumThicknessForInlineSidebars;
```

## Discussion

This value describes the minimum thickness in the primary axis of a split view—width if the split view’s [`isVertical`](../nssplitview/isvertical.md) value is [`true`](../../Swift/true.md), height if it’s [`false`](../../Swift/false.md). This value is the minimum thickness that sidebars can shrink to before they automatically collapse. When sidebars autocollapse in full-screen mode, they overlay the other split view items.

Autocollapsed sidebars automatically expand if their thickness increases to or above this minimum thickness threshold.

The default value of this property is [`automaticDimension`](./automaticdimension.md), which determines the minimum thickness for sidebars using the effective minimum size of the split view item views from the layout constraints in the window. If the system can’t apply the constraints that establish the minimum size for all noncollapsed split panes, all sidebars automatically collapse. In full-screen mode, if a sidebar attempts to expand in this state, it overlays instead.

## See Also

### Managing Sidebars
- [func toggleSidebar(Any?)](./togglesidebar%28_%29.md)
  Collapses or expands the first sidebar in the split view controller using an animation.
- [class let automaticDimension: CGFloat](./automaticdimension.md)
  The default value to apply to a dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/minimumthicknessforinlinesidebars)*