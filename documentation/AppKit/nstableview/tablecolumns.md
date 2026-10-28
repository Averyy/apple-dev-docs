# tableColumns

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array containing the current table column objects.

**Availability**:
- macOS

## Declaration

```swift
var tableColumns: [NSTableColumn] { get }
```

```objc
@property (copy, readonly) NSArray<NSTableColumn *> * tableColumns;
```

## Discussion

This property contains an array of [`NSTableColumn`](../nstablecolumn.md) objects corresponding to the columns in the table. This array contains all columns, including those that are currently hidden.

## See Also

### Column Management
- [func addTableColumn(NSTableColumn)](./addtablecolumn%28_%29.md)
  Adds the specified column as the last column of the table view.
- [func removeTableColumn(NSTableColumn)](./removetablecolumn%28_%29.md)
  Removes the specified column from the table view.
- [func moveColumn(Int, toColumn: Int)](./movecolumn%28_,tocolumn%29.md)
  Moves the column and heading at the specified index to the new specified index.
- [func column(withIdentifier: NSUserInterfaceItemIdentifier) -> Int](./column%28withidentifier%29.md)
  Returns the index of the first column in the table view whose identifier is equal to the specified identifier.
- [func tableColumn(withIdentifier: NSUserInterfaceItemIdentifier) -> NSTableColumn?](./tablecolumn%28withidentifier%29.md)
  Returns the `NSTableColumn` object for the first column whose identifier is equal to the specified object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableview/tablecolumns)*