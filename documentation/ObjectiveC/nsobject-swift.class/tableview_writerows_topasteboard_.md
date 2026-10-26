# tableView:writeRows:toPasteboard:

**Framework**: Objective-C Runtime  
**Kind**: method  
**Role**: Instance Method

Writes the specified rows to the specified pasteboard.

**Availability**:
- macOS 10.0+ - Deprecated in 10.4

> **Deprecated**: This method has been deprecated. You should implement [`tableView(_:writeRowsWith:to:)`](../../AppKit/nstableviewdatasource/tableview%28_,writerowswith,to%29.md) instead.

## Declaration

```objc
- (BOOL) tableView:(NSTableView *) tableView writeRows:(NSArray *) rows toPasteboard:(NSPasteboard *) pboard;
```

#### Return Value

Return [`YES`](../yes.md) to allow the drag: otherwise [`NO`](../no.md) to refuse the drag.

#### Discussion

Invoked by `aTableView` after it has been determined that a drag should begin, but before the drag has been started. To refuse the drag, return [`NO`](../no.md). To start a drag, return [`YES`](../yes.md) and place the drag data onto `pboard` (data, owner, and so on). The drag image and other drag-related information will be set up and provided by the table view once this call returns with [`YES`](../yes.md). `rows` is the list of row numbers that will be participating in the drag.

## Parameters

- `tableView`: The table view.
- `rows`: An array of row indexes.
- `pboard`: The pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/tableview:writerows:topasteboard:)*