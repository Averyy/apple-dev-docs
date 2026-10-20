# tableView(_:userDidChangeVisibilityOf:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the user changed the visibility of one or more table columns.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func tableView(_ tableView: NSTableView, userDidChangeVisibilityOf columns: [NSTableColumn])
```

```objc
- (void) tableView:(NSTableView *) tableView userDidChangeVisibilityOfTableColumns:(NSArray<NSTableColumn *> *) columns;
```

## Parameters

- `tableView`: The table view object requesting this information.
- `columns`: The table columns affected by the visibility change.

## See Also

### Showing and hiding columns
- [func tableView(NSTableView, userCanChangeVisibilityOf: NSTableColumn) -> Bool](./tableview%28_,usercanchangevisibilityof%29.md)
  Asks the delegate to verify that the user can change the given column’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:userdidchangevisibilityof:))*