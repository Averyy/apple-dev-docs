# NSViewToolTipOwner

**Framework**: AppKit  
**Kind**: protocol

A set of methods for dynamically associating a tool tip with a view.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSViewToolTipOwner : NSObjectProtocol
```

#### Overview

Tool tips are hints displayed to the user when the mouse hovers over a view. Adopt this protocol in views for which you want to provide tool tips. If the view does not implement this protocol, the system uses the [`description`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/description) method instead.

## Topics

### Obtaining Tool Tip Strings
- [func view(NSView, stringForToolTip: NSView.ToolTipTag, point: NSPoint, userData: UnsafeMutableRawPointer?) -> String](nsviewtooltipowner/view(_:stringfortooltip:point:userdata:).md)
  Returns the tool tip string to be displayed due to the cursor pausing at location `point` within the tool tip rectangle identified by `tag` in the view `view`.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSForm](nsform.md)
- [NSMatrix](nsmatrix.md)
- [NSTableHeaderView](nstableheaderview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsviewtooltipowner)*