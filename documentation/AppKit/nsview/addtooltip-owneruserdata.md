# addToolTip(_:owner:userData:)

**Framework**: AppKit  
**Kind**: method

Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.

**Availability**:
- macOS ?+

## Declaration

```swift
func addToolTip(_ rect: NSRect, owner: Any, userData data: UnsafeMutableRawPointer?) -> NSView.ToolTipTag
```

#### Return Value

An integer tag identifying the tooltip; you can use this tag to remove the tooltip.

#### Discussion

The tooltip string is obtained dynamically from `owner` by invoking either the `NSToolTipOwner` informal protocol method [`view:stringForToolTip:point:userData:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/view:stringForToolTip:point:userData:), if implemented, or the [`NSObjectProtocol`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol) protocol method [`description`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/description).

## Parameters

- `rect`: A rectangle defining the region of the view to associate the tooltip with.
- `owner`: An object from which to obtain the tooltip string. The object should either implement  [`view:stringForToolTip:point:userData:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/view:stringForToolTip:point:userData:), or return a suitable string from its [`description`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/description) method. It can therefore simply be an [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) object. > ❗ **Important**:  The view maintains a weak reference to `owner`. You’re responsible for ensuring that `owner` remains valid for as long as it may be needed.
- `data`: Any additional information you want to pass to [`view:stringForToolTip:point:userData:`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/view:stringForToolTip:point:userData:); it isn’t used if `owner` doesn’t implement this method.

## See Also

- [var toolTip: String?](nsview/tooltip.md)
  The text for the view’s tooltip.
- [func removeAllToolTips()](nsview/removealltooltips.md)
  Removes all tooltips assigned to the view.
- [func removeToolTip(NSView.ToolTipTag)](nsview/removetooltip(_:).md)
  Removes the tooltip identified by specified tag.
- [typealias ToolTipTag](nsview/tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addtooltip(_:owner:userdata:))*