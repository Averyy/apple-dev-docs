# allowsColumnReordering

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the table view allows the user to rearrange columns by dragging their headers.

**Availability**:
- macOS

## Declaration

```swift
var allowsColumnReordering: Bool { get set }
```

```objc
@property BOOL allowsColumnReordering;
```

#### Discussion

The default value of this property is [`true`](../../Swift/true.md), which allows the user to rearrange the table view’s columns. You can rearrange columns programmatically regardless of this setting.

## See Also

### Related Documentation
- [func moveColumn(Int, toColumn: Int)](./movecolumn%28_,tocolumn%29.md)
  Moves the column and heading at the specified index to the new specified index.
### Configuring Behavior
- [var allowsColumnResizing: Bool](./allowscolumnresizing.md)
  A Boolean value indicating whether the table view allows the user to resize columns by dragging between their headers.
- [var allowsMultipleSelection: Bool](./allowsmultipleselection.md)
  A Boolean value indicating whether the table view allows the user to select more than one column or row at a time.
- [var allowsEmptySelection: Bool](./allowsemptyselection.md)
  A Boolean value indicating whether the table view allows the user to select zero columns or rows.
- [var allowsColumnSelection: Bool](./allowscolumnselection.md)
  A Boolean value indicating whether the table view allows the user to select columns by clicking their headers.
- [var usesAutomaticRowHeights: Bool](./usesautomaticrowheights.md)
  A Boolean value that indicates whether the table view uses autolayout to calculate the height of rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/allowscolumnreordering)*