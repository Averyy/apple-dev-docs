# widgetList(_:shouldReorderRow:)

**Framework**: Notification Center  
**Kind**: method

Asks the delegate to allow or prohibit the specified row to be moved to a new location in the list.

**Availability**:
- macOS 10.10+

## Declaration

```swift
optional func widgetList(_ list: NCWidgetListViewController, shouldReorderRow row: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if specified row can be moved, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

List item reordering is not enabled unless the delegate implements this method and [`widgetList(_:didReorderRow:toRow:)`](ncwidgetlistviewdelegate/widgetlist(_:didreorderrow:torow:).md). Returning [`false`](https://developer.apple.com/documentation/swift/false) prohibits `row` from being moved. Returning YES allows `row` to be moved, and the delegate will be called again when the item that `row` represents is relocated in the list view controller’s [`contents`](ncwidgetlistviewcontroller/contents.md) array.

## Parameters

- `list`: The widget’s list view controller.
- `row`: The row that should be moved.

## See Also

- [func widgetList(NCWidgetListViewController, didReorderRow: Int, toRow: Int)](ncwidgetlistviewdelegate/widgetlist(_:didreorderrow:torow:).md)
  Tells the delegate that the specified row was moved to a new location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlist(_:shouldreorderrow:))*