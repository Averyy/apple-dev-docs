# widgetList(_:didRemoveRow:)

**Framework**: Notification Center  
**Kind**: method

Tells the delegate that the specified row was removed from the list.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func widgetList(_ list: NCWidgetListViewController, didRemoveRow row: Int)
```

#### Discussion

List item deletion is not enabled unless the delegate implements this method and [`widgetList(_:shouldRemoveRow:)`](ncwidgetlistviewdelegate/widgetlist(_:shouldremoverow:).md). The item represented by `row` is removed from the list view controller’s [`contents`](ncwidgetlistviewcontroller/contents.md) array before this method is called.

## Parameters

- `list`: The widget’s list view controller.
- `row`: The row that was removed.

## See Also

- [func widgetList(NCWidgetListViewController, shouldRemoveRow: Int) -> Bool](ncwidgetlistviewdelegate/widgetlist(_:shouldremoverow:).md)
  Asks the delegate to allow or prohibit the specified row to be removed from the list.
- [func widgetListPerformAddAction(NCWidgetListViewController)](ncwidgetlistviewdelegate/widgetlistperformaddaction(_:).md)
  Asks the delegate to perform an action when the Add (+) button is clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlist(_:didremoverow:))*