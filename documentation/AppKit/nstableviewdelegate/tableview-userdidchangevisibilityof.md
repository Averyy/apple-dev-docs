# tableView(_:userDidChangeVisibilityOf:)

**Framework**: AppKit  
**Kind**: method

Tells the delegate that the user changed the visibility of one or more table columns.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func tableView(_ tableView: NSTableView, userDidChangeVisibilityOf columns: [NSTableColumn])
```

## Parameters

- `tableView`: The table view object requesting this information.
- `columns`: The table columns affected by the visibility change.

## See Also

- [func tableView(NSTableView, userCanChangeVisibilityOf: NSTableColumn) -> Bool](nstableviewdelegate/tableview(_:usercanchangevisibilityof:).md)
  Asks the delegate to verify that the user can change the given column’s visibility.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:userdidchangevisibilityof:))*