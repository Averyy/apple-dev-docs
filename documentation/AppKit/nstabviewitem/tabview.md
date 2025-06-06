# tabView

**Framework**: AppKit  
**Kind**: property

Returns the parent tab view for the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
var tabView: NSTabView? { get }
```

#### Discussion

Note that this is the tab view itself, not the view displayed when a user clicks the tab.

A tab view item normally learns about its parent tab view when it is inserted into the view’s array of items. The NSTabView methods [`addTabViewItem(_:)`](nstabview/addtabviewitem(_:).md) and [`insertTabViewItem(_:at:)`](nstabview/inserttabviewitem(_:at:).md) set the tab view for the added or inserted item.

## See Also

- [var view: NSView?](nstabviewitem/view.md)
  Sets the view associated with the receiver to `view`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/tabview)*