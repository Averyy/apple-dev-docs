# widgetListPerformAddAction(_:)

**Framework**: Notification Center  
**Kind**: method

Asks the delegate to perform an action when the Add (+) button is clicked.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func widgetListPerformAddAction(_ list: NCWidgetListViewController)
```

#### Discussion

When a widget’s list is in editing mode, the list view controller can display an Add (+) button. The button’s action calls `widgetListPerformAddAction:` in the delegate.

If you want to display the default search view in the add action, you can use the `presentViewControllerInWidget:` method of `NSViewController`  to present an [`NCWidgetSearchViewController`](ncwidgetsearchviewcontroller.md) instance in the widget’s principal view controller.

## Parameters

- `list`: The widget’s list view controller.

## See Also

- [func widgetList(NCWidgetListViewController, didRemoveRow: Int)](ncwidgetlistviewdelegate/widgetlist(_:didremoverow:).md)
  Tells the delegate that the specified row was removed from the list.
- [func widgetList(NCWidgetListViewController, shouldRemoveRow: Int) -> Bool](ncwidgetlistviewdelegate/widgetlist(_:shouldremoverow:).md)
  Asks the delegate to allow or prohibit the specified row to be removed from the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlistperformaddaction(_:))*