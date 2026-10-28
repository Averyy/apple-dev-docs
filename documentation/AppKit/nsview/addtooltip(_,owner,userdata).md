# addToolTip(_:owner:userData:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.

**Availability**:
- macOS

## Declaration

```swift
func addToolTip(_ rect: NSRect, owner: Any, userData data: UnsafeMutableRawPointer?) -> NSView.ToolTipTag
```

```objc
- (NSToolTipTag) addToolTipRect:(NSRect) rect owner:(id) owner userData:(void *) data;
```

## Return Value

An integer tag identifying the tooltip; you can use this tag to remove the tooltip.

## Discussion

The tooltip string is obtained dynamically from `owner` by invoking either the `NSToolTipOwner` informal protocol method [`view:stringForToolTip:point:userData:`](../../ObjectiveC/nsobject-swift.class/view_stringfortooltip_point_userdata_.md), if implemented, or the [`NSObjectProtocol`](../../ObjectiveC/nsobjectprotocol.md) protocol method [`description`](../../ObjectiveC/nsobjectprotocol/description.md).

## Parameters

- `rect`: A rectangle defining the region of the view to associate the tooltip with.
- `owner`: An object from which to obtain the tooltip string. The object should either implement  [`view:stringForToolTip:point:userData:`](../../ObjectiveC/nsobject-swift.class/view_stringfortooltip_point_userdata_.md), or return a suitable string from its [`description`](../../ObjectiveC/nsobjectprotocol/description.md) method. It can therefore simply be an [`NSString`](../../Foundation/nsstring.md) object.

  > ❗ **Important**:  The view maintains a weak reference to `owner`. You’re responsible for ensuring that `owner` remains valid for as long as it may be needed.
- `data`: Any additional information you want to pass to [`view:stringForToolTip:point:userData:`](../../ObjectiveC/nsobject-swift.class/view_stringfortooltip_point_userdata_.md); it isn’t used if `owner` doesn’t implement this method.

## See Also

### Providing a Tool Tip
- [var toolTip: String?](./tooltip.md)
  The text for the view’s tooltip.
- [func removeAllToolTips()](./removealltooltips%28%29.md)
  Removes all tooltips assigned to the view.
- [func removeToolTip(NSView.ToolTipTag)](./removetooltip%28_%29.md)
  Removes the tooltip identified by specified tag.
- [typealias ToolTipTag](./tooltiptag.md)
  This type describes the rectangle used to identify a tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/addtooltip(_:owner:userdata:))*