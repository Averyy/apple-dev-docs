# removeAllToolTips()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes all tooltips assigned to the view.

**Availability**:
- macOS

## Declaration

```swift
func removeAllToolTips()
```

```objc
- (void) removeAllToolTips;
```

#### Discussion

This method operates on tooltips created using either [`addToolTip(_:owner:userData:)`](./addtooltip%28_,owner,userdata%29.md) or set using the [`toolTip`](./tooltip.md) property.

## See Also

### Providing a Tool Tip
- [var toolTip: String?](./tooltip.md)
  The text for the view’s tooltip.
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](./addtooltip%28_,owner,userdata%29.md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeToolTip(NSView.ToolTipTag)](./removetooltip%28_%29.md)
  Removes the tooltip identified by specified tag.
- [typealias ToolTipTag](./tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removealltooltips())*