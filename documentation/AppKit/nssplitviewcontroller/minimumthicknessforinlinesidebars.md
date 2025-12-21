# minimumThicknessForInlineSidebars

**Framework**: AppKit  
**Kind**: property

The minimum thickness for a sidebar before it automatically collapses.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var minimumThicknessForInlineSidebars: CGFloat { get set }
```

#### Discussion

This value describes the minimum thickness in the primary axis of a split view—width if the split view’s [`isVertical`](nssplitview/isvertical.md) value is [`true`](https://developer.apple.com/documentation/Swift/true), height if it’s [`false`](https://developer.apple.com/documentation/Swift/false). This value is the minimum thickness that sidebars can shrink to before they automatically collapse. When sidebars autocollapse in full-screen mode, they overlay the other split view items.

Autocollapsed sidebars automatically expand if their thickness increases to or above this minimum thickness threshold.

The default value of this property is [`automaticDimension`](nssplitviewcontroller/automaticdimension.md), which determines the minimum thickness for sidebars using the effective minimum size of the split view item views from the layout constraints in the window. If the system can’t apply the constraints that establish the minimum size for all noncollapsed split panes, all sidebars automatically collapse. In full-screen mode, if a sidebar attempts to expand in this state, it overlays instead.

## See Also

- [func toggleSidebar(Any?)](nssplitviewcontroller/togglesidebar(_:).md)
  Collapses or expands the first sidebar in the split view controller using an animation.
- [class let automaticDimension: CGFloat](nssplitviewcontroller/automaticdimension.md)
  The default value to apply to a dimension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/minimumthicknessforinlinesidebars)*