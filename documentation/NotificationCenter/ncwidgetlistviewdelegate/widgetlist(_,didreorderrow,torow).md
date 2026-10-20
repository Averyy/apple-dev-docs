# widgetList(_:didReorderRow:toRow:)

**Framework**: Notification Center  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the specified row was moved to a new location.

**Availability**:
- macOS 10.10+ - Deprecated in 11.0

> **Deprecated**: Use [WidgetKit](../../WidgetKit/WidgetKit.md) instead.

## Declaration

```swift
optional func widgetList(_ list: NCWidgetListViewController, didReorderRow row: Int, toRow newIndex: Int)
```

```objc
- (void) widgetList:(NCWidgetListViewController *) list didReorderRow:(NSUInteger) row toRow:(NSUInteger) newIndex;
```

#### Discussion

List item reordering is not enabled unless the delegate implements this method and [`widgetList(_:shouldReorderRow:)`](./widgetlist%28_,shouldreorderrow%29.md). The item represented by `row` is moved to its new location in the list view controller’s [`contents`](../ncwidgetlistviewcontroller/contents.md) array before this method is called.

## Parameters

- `list`: The widget’s list view controller.
- `row`: The row that was moved.
- `newIndex`: The new location of `row`.

## See Also

### Reordering List Rows
- [func widgetList(NCWidgetListViewController, shouldReorderRow: Int) -> Bool](./widgetlist%28_,shouldreorderrow%29.md)
  Asks the delegate to allow or prohibit the specified row to be moved to a new location in the list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/notificationcenter/ncwidgetlistviewdelegate/widgetlist(_:didreorderrow:torow:))*