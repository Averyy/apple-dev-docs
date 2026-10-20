# widgetList(_:shouldReorderRow:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Asks the delegate to allow or prohibit the specified row to be moved to a new location in the list.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
optional func widgetList(_ list: NCWidgetListViewController, shouldReorderRow row: Int) -> Bool
```

```objc
- (BOOL) widgetList:(NCWidgetListViewController *) list shouldReorderRow:(NSUInteger) row;
```

#### Return Value

[`true`](../../Swift/true.md) if specified row can be moved, otherwise [`false`](../../Swift/false.md).

#### Discussion

List item reordering is not enabled unless the delegate implements this method and [`widgetList(_:didReorderRow:toRow:)`](./widgetlist%28_,didreorderrow,torow%29.md). Returning [`false`](../../Swift/false.md) prohibits `row` from being moved. Returning YES allows `row` to be moved, and the delegate will be called again when the item that `row` represents is relocated in the list view controller’s [`contents`](../ncwidgetlistviewcontroller/contents.md) array.

## Parameters

- `list`: The widget’s list view controller.
- `row`: The row that should be moved.

## See Also

### Reordering List Rows
- [func widgetList(NCWidgetListViewController, didReorderRow: Int, toRow: Int)](./widgetlist%28_,didreorderrow,torow%29.md)
  Tells the delegate that the specified row was moved to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlist(_:shouldreorderrow:))*