# accessibilityLabel()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns a short description of the table.

**Availability**:
- macOS ?+

## Declaration

```swift
func accessibilityLabel() -> String?
```

#### Return Value

The description of the table.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](nsaccessibilityprotocol.md) protocol’s [`accessibilityLabel`](nsaccessibility-c.protocol/accessibilitylabel.md) property.

Do not include the control’s type in the label (for example, use `Employees`, not `Employees Table`). If possible use a single word. To help ensure that accessibility clients such as VoiceOver read the label with the correct intonation, start this label with a capital letter. Do not put a period at the end. Always localize the label.

## See Also

- [func accessibilityColumnHeaderUIElements() -> [Any]?](nsaccessibilitytable/accessibilitycolumnheaderuielements.md)
  Returns the column header accessibility elements for the table.
- [func accessibilityColumns() -> [Any]?](nsaccessibilitytable/accessibilitycolumns.md)
  Returns the column accessibility elements for the table.
- [func accessibilityRowHeaderUIElements() -> [Any]?](nsaccessibilitytable/accessibilityrowheaderuielements.md)
  Returns the row header accessibility elements for the table.
- [func accessibilityRows() -> [any NSAccessibilityRow]?](nsaccessibilitytable/accessibilityrows.md)
  Returns the row accessibility elements for the table.
- [func accessibilitySelectedCells() -> [Any]?](nsaccessibilitytable/accessibilityselectedcells.md)
  The currently selected cells for the table.
- [func accessibilitySelectedColumns() -> [Any]?](nsaccessibilitytable/accessibilityselectedcolumns.md)
  Returns the currently selected columns for the table.
- [func accessibilitySelectedRows() -> [any NSAccessibilityRow]?](nsaccessibilitytable/accessibilityselectedrows.md)
  Returns the currently selected rows for the table.
- [func accessibilityVisibleCells() -> [Any]?](nsaccessibilitytable/accessibilityvisiblecells.md)
  Returns the visible cells for the table.
- [func accessibilityVisibleColumns() -> [Any]?](nsaccessibilitytable/accessibilityvisiblecolumns.md)
  Returns the visible columns for the table.
- [func accessibilityVisibleRows() -> [any NSAccessibilityRow]?](nsaccessibilitytable/accessibilityvisiblerows.md)
  Returns the visible rows for the table.
- [func setAccessibilitySelectedRows([any NSAccessibilityRow])](nsaccessibilitytable/setaccessibilityselectedrows(_:).md)
  Sets the table’s currently selected rows.
- [func accessibilityHeaderGroup() -> String?](nsaccessibilitytable/accessibilityheadergroup.md)
  Returns the header group for the table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/accessibilitylabel())*