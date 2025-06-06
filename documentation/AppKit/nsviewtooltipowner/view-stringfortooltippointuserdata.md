# view(_:stringForToolTip:point:userData:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the tool tip string to be displayed due to the cursor pausing at location `point` within the tool tip rectangle identified by `tag` in the view `view`.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func view(_ view: NSView, stringForToolTip tag: NSView.ToolTipTag, point: NSPoint, userData data: UnsafeMutableRawPointer?) -> String
```

#### Discussion

`userData` is additional information provided by the creator of the tool tip rectangle.

## See Also

- [Online Help](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/OnlineHelp/OnlineHelp.html#//apple_ref/doc/uid/10000009i)
- [func addToolTip(NSRect, owner: Any, userData: UnsafeMutableRawPointer?) -> NSView.ToolTipTag](nsview/addtooltip(_:owner:userdata:).md)
  Creates a tooltip for a defined area in the view and returns a tag that identifies the tooltip rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewtooltipowner/view(_:stringfortooltip:point:userdata:))*