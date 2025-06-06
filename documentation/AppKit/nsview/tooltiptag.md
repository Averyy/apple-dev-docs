# NSView.ToolTipTag

**Framework**: AppKit  
**Kind**: typealias

This type describes the rectangle used to identify a tooltip rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias ToolTipTag = Int
```

#### Discussion

If the value of this type is 0, it is invalid. See the methods [`addToolTip(_:owner:userData:)`](nsview/addtooltip(_:owner:userdata:).md) and[`removeToolTip(_:)`](nsview/removetooltip(_:).md).

## See Also

- [var toolTip: String?](nsview/tooltip.md)
  The text for the view’s tooltip.
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](nsview/addtooltip(_:owner:userdata:).md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeAllToolTips()](nsview/removealltooltips.md)
  Removes all tooltips assigned to the view.
- [func removeToolTip(NSView.ToolTipTag)](nsview/removetooltip(_:).md)
  Removes the tooltip identified by specified tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/tooltiptag)*