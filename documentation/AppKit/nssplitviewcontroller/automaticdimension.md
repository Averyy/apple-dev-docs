# automaticDimension

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The default value to apply to a dimension.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class let automaticDimension: CGFloat
```

```c
extern const CGFloat NSSplitViewControllerAutomaticDimension;
```

#### Discussion

Use this constant with any sizing-related [`NSSplitViewController`](../nssplitviewcontroller.md) property to get the default system behavior.

## See Also

### Managing Sidebars
- [func toggleSidebar(Any?)](./togglesidebar%28_%29.md)
  Collapses or expands the first sidebar in the split view controller using an animation.
- [var minimumThicknessForInlineSidebars: CGFloat](./minimumthicknessforinlinesidebars.md)
  The minimum thickness for a sidebar before it automatically collapses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssplitviewcontroller/automaticdimension)*