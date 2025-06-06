# toolTip

**Framework**: AppKit  
**Kind**: property

The text for the view’s tooltip.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var toolTip: String? { get set }
```

#### Discussion

The value of this property is `nil` if the view does not currently display tooltip text. Assigning a value to this property causes the tooltip to be displayed for the view. Setting the property to nil cancels the display of the tooltip for the view.

## See Also

- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](nsview/addtooltip(_:owner:userdata:).md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeAllToolTips()](nsview/removealltooltips.md)
  Removes all tooltips assigned to the view.
- [func removeToolTip(NSView.ToolTipTag)](nsview/removetooltip(_:).md)
  Removes the tooltip identified by specified tag.
- [typealias ToolTipTag](nsview/tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/tooltip)*