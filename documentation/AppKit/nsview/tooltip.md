# toolTip

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The text for the view’s tooltip.

**Availability**:
- macOS

## Declaration

```swift
var toolTip: String? { get set }
```

```objc
@property (copy, nullable) NSString * toolTip;
```

## Discussion

The value of this property is `nil` if the view does not currently display tooltip text. Assigning a value to this property causes the tooltip to be displayed for the view. Setting the property to nil cancels the display of the tooltip for the view.

## See Also

### Providing a Tool Tip
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](./addtooltip%28_,owner,userdata%29.md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.
- [func removeAllToolTips()](./removealltooltips%28%29.md)
  Removes all tooltips assigned to the view.
- [func removeToolTip(NSView.ToolTipTag)](./removetooltip%28_%29.md)
  Removes the tooltip identified by specified tag.
- [typealias ToolTipTag](./tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/tooltip)*