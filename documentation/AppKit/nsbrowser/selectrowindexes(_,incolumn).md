# selectRowIndexes(_:inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Specifies the selected rows in a given column of the browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func selectRowIndexes(_ indexes: IndexSet, inColumn column: Int)
```

```objc
- (void) selectRowIndexes:(NSIndexSet *) indexes inColumn:(NSInteger) column;
```

## Parameters

- `indexes`: Rows to be selected in column `columnIndex`.
- `column`: Column in which to select rows `rowIndexes`.

## See Also

### Managing Selection Behavior
- [var allowsBranchSelection: Bool](./allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectedRowIndexes(inColumn: Int) -> IndexSet?](./selectedrowindexes%28incolumn%29.md)
  Provides the indexes of the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](./allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectrowindexes(_:incolumn:))*