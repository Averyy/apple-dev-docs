# selectRowIndexes(_:byExtendingSelection:)

**Framework**: AppKit  
**Kind**: method

Sets in the receiver the indexes of rows that are selected.

**Availability**:
- macOS ?+

## Declaration

```swift
func selectRowIndexes(_ indexes: IndexSet, byExtendingSelection extend: Bool)
```

## Parameters

- `indexes`: The indexes of rows in the receiver to select. > ❗ **Important**:  Raises an `NSRangeException` if any index in `rowIndexes` is less than `0` or greater than or equal to the number of rows.
- `extend`: If [`false`](https://developer.apple.com/documentation/Swift/false), the selected rows are specified by `indexes`. If [`true`](https://developer.apple.com/documentation/Swift/true), the rows indicated by `indexes` are added to the collection of already selected rows, providing multiple selection.

## See Also

- [var selectedRowIndexes: IndexSet](nsruleeditor/selectedrowindexes.md)
  The indexes of the rule editor’s selected rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/selectrowindexes(_:byextendingselection:))*