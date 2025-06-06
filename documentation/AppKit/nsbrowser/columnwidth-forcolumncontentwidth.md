# columnWidth(forColumnContentWidth:)

**Framework**: AppKit  
**Kind**: method

Returns the column width for the width of the given column’s content.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func columnWidth(forColumnContentWidth columnContentWidth: CGFloat) -> CGFloat
```

#### Return Value

The width of the column (the width of the entire scrolling text view).

#### Discussion

For example, to guarantee that 16 pixels of your browser cell are always visible, call:

```objc
[browser setMinColumnWidth: [browser columnWidthForColumnContentWidth:16]]
```

## Parameters

- `columnContentWidth`: The width of the column’s content (the width of the matrix in the column).

## See Also

- [class func removeSavedColumns(withAutosaveName: NSBrowser.ColumnsAutosaveName)](nsbrowser/removesavedcolumns(withautosavename:).md)
  Removes the column configuration data stored under the given name from the application’s user defaults.
- [var columnsAutosaveName: NSBrowser.ColumnsAutosaveName](nsbrowser/columnsautosavename-swift.property.md)
  The name used to automatically save the browser’s column configuration.
- [NSBrowser.ColumnsAutosaveName](nsbrowser/columnsautosavename-swift.typealias.md)
- [func columnContentWidth(forColumnWidth: CGFloat) -> CGFloat](nsbrowser/columncontentwidth(forcolumnwidth:).md)
  Returns the content width for a given column width.
- [var columnResizingType: NSBrowser.ColumnResizingType](nsbrowser/columnresizingtype-swift.property.md)
  A constant indicating the browser’s column resizing type.
- [var prefersAllColumnUserResizing: Bool](nsbrowser/prefersallcolumnuserresizing.md)
  A Boolean that indicates whether the browser is set to resize all columns simultaneously rather than resizing a single column at a time.
- [func width(ofColumn: Int) -> CGFloat](nsbrowser/width(ofcolumn:).md)
  Returns the width of the specified column.
- [func setWidth(CGFloat, ofColumn: Int)](nsbrowser/setwidth(_:ofcolumn:).md)
  Sets the width of the specified column.
- [func defaultColumnWidth() -> CGFloat](nsbrowser/defaultcolumnwidth.md)
  Returns the default column width of the browser’s columns.
- [func setDefaultColumnWidth(CGFloat)](nsbrowser/setdefaultcolumnwidth(_:).md)
  Sets the default column width for new browser columns that do not otherwise have an initial width from defaults or the browser’s delegate.
- [var rowHeight: CGFloat](nsbrowser/rowheight.md)
  The height of the browser’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/columnwidth(forcolumncontentwidth:))*