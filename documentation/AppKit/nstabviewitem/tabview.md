# tabView

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Returns the parent tab view for the receiver.

**Availability**:
- macOS

## Declaration

```swift
var tabView: NSTabView? { get }
```

```objc
@property (readonly, nullable) NSTabView * tabView;
```

## Discussion

Note that this is the tab view itself, not the view displayed when a user clicks the tab.

A tab view item normally learns about its parent tab view when it is inserted into the view’s array of items. The NSTabView methods [`addTabViewItem(_:)`](../nstabview/addtabviewitem%28_%29.md) and [`insertTabViewItem(_:at:)`](../nstabview/inserttabviewitem%28_,at%29.md) set the tab view for the added or inserted item.

## See Also

### Related Documentation
- [var view: NSView?](./view.md)
  Sets the view associated with the receiver to `view`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewitem/tabview)*