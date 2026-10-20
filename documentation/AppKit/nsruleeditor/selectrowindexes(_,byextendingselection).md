# selectRowIndexes(_:byExtendingSelection:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets in the receiver the indexes of rows that are selected.

**Availability**:
- macOS

## Declaration

```swift
func selectRowIndexes(_ indexes: IndexSet, byExtendingSelection extend: Bool)
```

```objc
- (void) selectRowIndexes:(NSIndexSet *) indexes byExtendingSelection:(BOOL) extend;
```

## Parameters

- `indexes`: The indexes of rows in the receiver to select.

  > ❗ **Important**:  Raises an `NSRangeException` if any index in `rowIndexes` is less than `0` or greater than or equal to the number of rows.
- `extend`: If [`false`](../../Swift/false.md), the selected rows are specified by `indexes`. If [`true`](../../Swift/true.md), the rows indicated by `indexes` are added to the collection of already selected rows, providing multiple selection.

## See Also

### Working with the Selection
- [var selectedRowIndexes: IndexSet](./selectedrowindexes.md)
  The indexes of the rule editor’s selected rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/selectrowindexes(_:byextendingselection:))*