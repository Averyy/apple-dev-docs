# selectedRowIndexes(inColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Provides the indexes of the selected rows in a given column of the browser.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func selectedRowIndexes(inColumn column: Int) -> IndexSet?
```

```objc
- (NSIndexSet *) selectedRowIndexesInColumn:(NSInteger) column;
```

#### Return Value

Rows selected in column `columnIndex`.

## Parameters

- `column`: The column whose selected rows are provided.

## See Also

### Managing Selection Behavior
- [var allowsBranchSelection: Bool](./allowsbranchselection.md)
  A Boolean that indicates whether the user can select branch items.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean that indicates whether there can be nothing selected.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean that indicates whether the user can select multiple items.
- [func selectRowIndexes(IndexSet, inColumn: Int)](./selectrowindexes%28_,incolumn%29.md)
  Specifies the selected rows in a given column of the browser.
- [var allowsTypeSelect: Bool](./allowstypeselect.md)
  A Boolean that indicates whether the browser allows keystroke-based selection (type select).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/selectedrowindexes(incolumn:))*