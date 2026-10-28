# NSView.ToolTipTag

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

This type describes the rectangle used to identify a tooltip rectangle.

**Availability**:
- macOS

## Declaration

```swift
typealias ToolTipTag = Int
```

```c
typedef NSInteger NSToolTipTag;
```

## Discussion

If the value of this type is 0, it is invalid. See the methods [`addToolTip(_:owner:userData:)`](./addtooltip%28_,owner,userdata%29.md) and[`removeToolTip(_:)`](./removetooltip%28_%29.md).

## See Also

### Providing a Tool Tip
- [var toolTip: String?](./tooltip.md)
  The text for the view’s tooltip.
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](./addtooltip%28_,owner,userdata%29.md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeAllToolTips()](./removealltooltips%28%29.md)
  Removes all tooltips assigned to the view.
- [func removeToolTip(NSView.ToolTipTag)](./removetooltip%28_%29.md)
  Removes the tooltip identified by specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/tooltiptag)*