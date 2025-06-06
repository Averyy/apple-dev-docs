# tableView(_:userCanChangeVisibilityOf:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate to verify that the user can change the given column’s visibility.

**Availability**:
- macOS 14.0+

## Declaration

```swift
optional func tableView(_ tableView: NSTableView, userCanChangeVisibilityOf column: NSTableColumn) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the user can change the visibility of the column; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Implement this method to enable the table view to provide a menu that allows users to show or hide table columns.

To change a column’s visibility, ensure the column has a title. Further, setting the [`menu`](nsresponder/menu.md) property on the table view [`headerView`](nstableview/headerview.md) or, subclassing [`NSTableHeaderView`](nstableheaderview.md) and overriding the [`menu`](nsresponder/menu.md) property also prevents the column visibility from changing.

## Parameters

- `tableView`: The table view object requesting this information.
- `column`: The table column affected by the visibility change.

## See Also

- [func tableView(NSTableView, userDidChangeVisibilityOf: [NSTableColumn])](nstableviewdelegate/tableview(_:userdidchangevisibilityof:).md)
  Tells the delegate that the user changed the visibility of one or more table columns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewdelegate/tableview(_:usercanchangevisibilityof:))*