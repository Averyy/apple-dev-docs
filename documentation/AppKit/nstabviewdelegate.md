# NSTabViewDelegate

**Framework**: AppKit  
**Kind**: protocol

The `NSTabViewDelegate` protocol defines the optional methods implemented by delegates of `NSTabView` objects.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTabViewDelegate : NSObjectProtocol
```

## Topics

### Adding and Removing Tabs
- [func tabViewDidChangeNumberOfTabViewItems(NSTabView)](nstabviewdelegate/tabviewdidchangenumberoftabviewitems(_:).md)
  Informs the delegate that the number of tab view items in `tabView` has changed.
### Selecting a Tab
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](nstabviewdelegate/tabview(_:shouldselect:).md)
  Invoked just before `tabViewItem` in `tabView` is selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](nstabviewdelegate/tabview(_:willselect:).md)
  Informs the delegate that `tabView` is about to select `tabViewItem`.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](nstabviewdelegate/tabview(_:didselect:).md)
  Informs the delegate that `tabView` has selected `tabViewItem`.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSTabViewController](nstabviewcontroller.md)

## See Also

- [var delegate: (any NSTabViewDelegate)?](nstabview/delegate.md)
  The tab view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate)*