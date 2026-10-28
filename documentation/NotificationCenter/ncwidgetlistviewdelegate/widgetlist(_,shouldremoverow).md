# widgetList(_:shouldRemoveRow:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to allow or prohibit the specified row to be removed from the list.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
optional func widgetList(_ list: NCWidgetListViewController, shouldRemoveRow row: Int) -> Bool
```

```objc
- (BOOL) widgetList:(NCWidgetListViewController *) list shouldRemoveRow:(NSUInteger) row;
```

## Return Value

[`true`](../../Swift/true.md) if the specified row can be removed, otherwise [`false`](../../Swift/false.md).

## Discussion

List item deletion is not enabled unless the delegate implements this method and [`widgetList(_:didRemoveRow:)`](./widgetlist%28_,didremoverow%29.md). Returning [`false`](../../Swift/false.md) prohibits `row` from being deleted. Returning YES allows `row` to be deleted, and the delegate will be called again when the item that `row` represents is deleted from the list view controller’s [`contents`](../ncwidgetlistviewcontroller/contents.md) array.

## Parameters

- `list`: The widget’s list view controller.
- `row`: The row that should be removed.

## See Also

### Adding and Deleting Rows
- [func widgetList(NCWidgetListViewController, didRemoveRow: Int)](./widgetlist%28_,didremoverow%29.md)
  Tells the delegate that the specified row was removed from the list.
- [func widgetListPerformAddAction(NCWidgetListViewController)](./widgetlistperformaddaction%28_%29.md)
  Asks the delegate to perform an action when the Add (+) button is clicked.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlist(_:shouldremoverow:))*