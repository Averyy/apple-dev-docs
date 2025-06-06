# highlightedTableColumn

**Framework**: AppKit  
**Kind**: property

The column highlighted in the table.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
weak var highlightedTableColumn: NSTableColumn? { get set }
```

#### Discussion

Assigning a value to this property highlights the specified column. A highlightable column header can be used in conjunction with row selection to highlight a particular column of the table. An example of this is how the Mail application indicates the currently sorted column.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/highlightedtablecolumn)*