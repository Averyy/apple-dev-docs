# allowsMultipleSelection

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.

**Availability**:
- macOS

## Declaration

```swift
var allowsMultipleSelection: Bool { get set }
```

```objc
@property BOOL allowsMultipleSelection;
```

#### Discussion

The default is [`false`](../../Swift/false.md), which allows the user to select only one column or row at a time. You can select multiple columns or rows programmatically regardless of this setting.

## See Also

### Related Documentation
- [func selectColumnIndexes(IndexSet, byExtendingSelection: Bool)](./selectcolumnindexes%28_,byextendingselection%29.md)
  Sets the column selection using `indexes` possibly extending the selection.
- [func selectRowIndexes(IndexSet, byExtendingSelection: Bool)](./selectrowindexes%28_,byextendingselection%29.md)
  Sets the row selection using `indexes` extending the selection if specified.
### Configuring Behavior
- [var allowsColumnReordering: Bool](./allowscolumnreordering.md)
  A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.
- [var allowsColumnResizing: Bool](./allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var allowsColumnSelection: Bool](./allowscolumnselection.md)
  A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.
- [var usesAutomaticRowHeights: Bool](./usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowsmultipleselection)*