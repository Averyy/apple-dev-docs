# selectRowIndexes(_:byExtendingSelection:)

**Framework**: AppKit  
**Kind**: method

Sets in the receiver the indexes of rows that are selected.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func selectRowIndexes(_ indexes: IndexSet, byExtendingSelection extend: Bool)
```

## Parameters

- `indexes`: The indexes of rows in the receiver to select.
- `extend`: If  , the selected rows are specified by  . If  , the rows indicated by   are added to the collection of already selected rows, providing multiple selection.

## See Also

- [var selectedRowIndexes: IndexSet](nsruleeditor/selectedrowindexes.md)
  The indexes of the rule editor’s selected rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/selectrowindexes(_:byextendingselection:))*