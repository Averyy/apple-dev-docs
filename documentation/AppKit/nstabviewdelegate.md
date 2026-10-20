# NSTabViewDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

The `NSTabViewDelegate` protocol defines the optional methods implemented by delegates of `NSTabView` objects.

**Availability**:
- macOS

## Declaration

```swift
protocol NSTabViewDelegate : NSObjectProtocol
```

```objc
@protocol NSTabViewDelegate <NSObject>
```

## Topics

### Adding and Removing Tabs
- [func tabViewDidChangeNumberOfTabViewItems(NSTabView)](./nstabviewdelegate/tabviewdidchangenumberoftabviewitems%28_%29.md)
  Informs the delegate that the number of tab view items in `tabView` has changed.
### Selecting a Tab
- [func tabView(NSTabView, shouldSelect: NSTabViewItem?) -> Bool](./nstabviewdelegate/tabview%28_,shouldselect%29.md)
  Invoked just before `tabViewItem` in `tabView` is selected.
- [func tabView(NSTabView, willSelect: NSTabViewItem?)](./nstabviewdelegate/tabview%28_,willselect%29.md)
  Informs the delegate that `tabView` is about to select `tabViewItem`.
- [func tabView(NSTabView, didSelect: NSTabViewItem?)](./nstabviewdelegate/tabview%28_,didselect%29.md)
  Informs the delegate that `tabView` has selected `tabViewItem`.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [NSTabViewController](./nstabviewcontroller.md)

## See Also

### Handling the Selection of Tabs
- [var delegate: (any NSTabViewDelegate)?](./nstabview/delegate.md)
  The tab view’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstabviewdelegate)*