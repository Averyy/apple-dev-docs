# removeAllToolTips()

**Framework**: AppKit  
**Kind**: method

Removes all tooltips assigned to the view.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeAllToolTips()
```

#### Discussion

This method operates on tooltips created using either [`addToolTip(_:owner:userData:)`](nsview/addtooltip(_:owner:userdata:).md) or set using the [`toolTip`](nsview/tooltip.md) property.

## See Also

- [var toolTip: String?](nsview/tooltip.md)
  The text for the view’s tooltip.
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](nsview/addtooltip(_:owner:userdata:).md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeToolTip(NSView.ToolTipTag)](nsview/removetooltip(_:).md)
  Removes the tooltip identified by specified tag.
- [typealias ToolTipTag](nsview/tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removealltooltips())*