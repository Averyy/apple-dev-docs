# removeToolTip(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the tooltip identified by specified tag.

**Availability**:
- macOS

## Declaration

```swift
func removeToolTip(_ tag: NSView.ToolTipTag)
```

```objc
- (void) removeToolTip:(NSToolTipTag) tag;
```

## Parameters

- `tag`: An integer tag that is the value returned by a previous [`addToolTip(_:owner:userData:)`](./addtooltip%28_,owner,userdata%29.md) message.

## See Also

### Providing a Tool Tip
- [var toolTip: String?](./tooltip.md)
  The text for the view’s tooltip.
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](./addtooltip%28_,owner,userdata%29.md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeAllToolTips()](./removealltooltips%28%29.md)
  Removes all tooltips assigned to the view.
- [typealias ToolTipTag](./tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/removetooltip(_:))*