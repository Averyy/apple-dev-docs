# accessibilityLabel()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a short description of the table.

**Availability**:
- macOS

## Declaration

```swift
func accessibilityLabel() -> String?
```

```objc
- (NSString *) accessibilityLabel;
```

#### Return Value

The description of the table.

#### Discussion

This method is the getter for the [`NSAccessibilityProtocol`](../nsaccessibilityprotocol.md) protocol’s [`accessibilityLabel`](../nsaccessibility-c.protocol/accessibilitylabel.md) property.

Do not include the control’s type in the label (for example, use `Employees`, not `Employees Table`). If possible use a single word. To help ensure that accessibility clients such as VoiceOver read the label with the correct intonation, start this label with a capital letter. Do not put a period at the end. Always localize the label.

## See Also

### Supporting Accessibility
- [func accessibilityColumnHeaderUIElements() -> [Any]?](./accessibilitycolumnheaderuielements%28%29.md)
  Returns the column header accessibility elements for the table.
- [func accessibilityColumns() -> [Any]?](./accessibilitycolumns%28%29.md)
  Returns the column accessibility elements for the table.
- [func accessibilityRowHeaderUIElements() -> [Any]?](./accessibilityrowheaderuielements%28%29.md)
  Returns the row header accessibility elements for the table.
- [func accessibilityRows() -> [any NSAccessibilityRow]?](./accessibilityrows%28%29.md)
  Returns the row accessibility elements for the table.
- [func accessibilitySelectedCells() -> [Any]?](./accessibilityselectedcells%28%29.md)
  The currently selected cells for the table.
- [func accessibilitySelectedColumns() -> [Any]?](./accessibilityselectedcolumns%28%29.md)
  Returns the currently selected columns for the table.
- [func accessibilitySelectedRows() -> [any NSAccessibilityRow]?](./accessibilityselectedrows%28%29.md)
  Returns the currently selected rows for the table.
- [func accessibilityVisibleCells() -> [Any]?](./accessibilityvisiblecells%28%29.md)
  Returns the visible cells for the table.
- [func accessibilityVisibleColumns() -> [Any]?](./accessibilityvisiblecolumns%28%29.md)
  Returns the visible columns for the table.
- [func accessibilityVisibleRows() -> [any NSAccessibilityRow]?](./accessibilityvisiblerows%28%29.md)
  Returns the visible rows for the table.
- [func setAccessibilitySelectedRows([any NSAccessibilityRow])](./setaccessibilityselectedrows%28_%29.md)
  Sets the table’s currently selected rows.
- [func accessibilityHeaderGroup() -> String?](./accessibilityheadergroup%28%29.md)
  Returns the header group for the table.
### Related Documentation
- [accessibilityLabel](../nsaccessibility-c.protocol/accessibilitylabel.md)
  A short description of the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibilitytable/accessibilitylabel())*