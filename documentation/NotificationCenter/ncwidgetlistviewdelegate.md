# NCWidgetListViewDelegate

**Framework**: Notification Center  
**Kind**: protocol  
**Role**: Protocol

The interface for handling content display and editing in the list view of a macOS Today widget.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
protocol NCWidgetListViewDelegate : NSObjectProtocol
```

```objc
@protocol NCWidgetListViewDelegate <NSObject>
```

#### Overview

The `NCWidgetListViewDelegate` protocol defines methods that handle content display and editing in the list view of a Today widget. The [`delegate`](./ncwidgetlistviewcontroller/delegate.md) of an [`NCWidgetListViewController`](./ncwidgetlistviewcontroller.md) must adopt the `NCWidgetListViewDelegate` protocol.

The single required method in the protocol, [`widgetList(_:viewControllerForRow:)`](./ncwidgetlistviewdelegate/widgetlist%28_,viewcontrollerforrow%29.md), creates a view controller for the contents of one row in the widget’s list view. Optional methods in the `NCWidgetListViewDelegate` protocol support editing actions, such as adding a new list item and reordering or deleting list rows.

## Topics

### Creating a Content View Controller
- [func widgetList(NCWidgetListViewController, viewControllerForRow: Int) -> NSViewController](./ncwidgetlistviewdelegate/widgetlist%28_,viewcontrollerforrow%29.md)
  Asks the delegate for a content view controller for the specified row.
### Adding and Deleting Rows
- [func widgetList(NCWidgetListViewController, didRemoveRow: Int)](./ncwidgetlistviewdelegate/widgetlist%28_,didremoverow%29.md)
  Tells the delegate that the specified row was removed from the list.
- [func widgetList(NCWidgetListViewController, shouldRemoveRow: Int) -> Bool](./ncwidgetlistviewdelegate/widgetlist%28_,shouldremoverow%29.md)
  Asks the delegate to allow or prohibit the specified row to be removed from the list.
- [func widgetListPerformAddAction(NCWidgetListViewController)](./ncwidgetlistviewdelegate/widgetlistperformaddaction%28_%29.md)
  Asks the delegate to perform an action when the Add (+) button is clicked.
### Reordering List Rows
- [func widgetList(NCWidgetListViewController, didReorderRow: Int, toRow: Int)](./ncwidgetlistviewdelegate/widgetlist%28_,didreorderrow,torow%29.md)
  Tells the delegate that the specified row was moved to a new location.
- [func widgetList(NCWidgetListViewController, shouldReorderRow: Int) -> Bool](./ncwidgetlistviewdelegate/widgetlist%28_,shouldreorderrow%29.md)
  Asks the delegate to allow or prohibit the specified row to be moved to a new location in the list.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Displaying and Editing List Content
- [var delegate: (any NCWidgetListViewDelegate)?](./ncwidgetlistviewcontroller/delegate.md)
  The list view controller’s delegate or `nil` if the receiver doesn’t have a delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate)*