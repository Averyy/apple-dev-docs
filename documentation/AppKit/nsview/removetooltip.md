# removeToolTip(_:)

**Framework**: AppKit  
**Kind**: method

Removes the tooltip identified by specified tag.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeToolTip(_ tag: NSView.ToolTipTag)
```

## Parameters

- `tag`: An integer tag that is the value returned by a previous   message.

## See Also

- [var toolTip: String?](nsview/tooltip.md)
  The text for the view’s tooltip.
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](nsview/addtooltip(_:owner:userdata:).md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeAllToolTips()](nsview/removealltooltips.md)
  Removes all tooltips assigned to the view.
- [typealias ToolTipTag](nsview/tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removetooltip(_:))*