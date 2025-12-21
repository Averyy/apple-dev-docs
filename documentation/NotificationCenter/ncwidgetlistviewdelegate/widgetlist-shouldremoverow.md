# widgetList(_:shouldRemoveRow:)

**Framework**: Notification Center  
**Kind**: method

Asks the delegate to allow or prohibit the specified row to be removed from the list.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func widgetList(_ list: NCWidgetListViewController, shouldRemoveRow row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the specified row can be removed, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

List item deletion is not enabled unless the delegate implements this method and [`widgetList(_:didRemoveRow:)`](ncwidgetlistviewdelegate/widgetlist(_:didremoverow:).md). Returning [`false`](https://developer.apple.com/documentation/Swift/false) prohibits `row` from being deleted. Returning YES allows `row` to be deleted, and the delegate will be called again when the item that `row` represents is deleted from the list view controller’s [`contents`](ncwidgetlistviewcontroller/contents.md) array.

## Parameters

- `list`: The widget’s list view controller.
- `row`: The row that should be removed.

## See Also

- [func widgetList(NCWidgetListViewController, didRemoveRow: Int)](ncwidgetlistviewdelegate/widgetlist(_:didremoverow:).md)
  Tells the delegate that the specified row was removed from the list.
- [func widgetListPerformAddAction(NCWidgetListViewController)](ncwidgetlistviewdelegate/widgetlistperformaddaction(_:).md)
  Asks the delegate to perform an action when the Add (+) button is clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlist(_:shouldremoverow:))*