# rowHeight

**Framework**: AppKit  
**Kind**: property

The height of the browser’s rows.

**Availability**:
- macOS 10.6+

## Declaration

```swift
@MainActor
var rowHeight: CGFloat { get set }
```

#### Discussion

The value of this property must be greater than `0`. The default value of this property is `17.0`. Any fractional value will be forced to an integral value for drawing. For variable row height browsers (ones whose delegates implement [`browser(_:heightOfRow:inColumn:)`](nsbrowserdelegate/browser(_:heightofrow:incolumn:).md)), the row height will be used to draw alternating rows past the last row in each browser column.

This property is only available when using the item delegate methods. An exception is thrown if you are using the matrix delegate methods.

## See Also

- [class func removeSavedColumns(withAutosaveName: NSBrowser.ColumnsAutosaveName)](nsbrowser/removesavedcolumns(withautosavename:).md)
  Removes the column configuration data stored under the given name from the application’s user defaults.
- [var columnsAutosaveName: NSBrowser.ColumnsAutosaveName](nsbrowser/columnsautosavename-swift.property.md)
  The name used to automatically save the browser’s column configuration.
- [NSBrowser.ColumnsAutosaveName](nsbrowser/columnsautosavename-swift.typealias.md)
- [func columnContentWidth(forColumnWidth: CGFloat) -> CGFloat](nsbrowser/columncontentwidth(forcolumnwidth:).md)
  Returns the content width for a given column width.
- [func columnWidth(forColumnContentWidth: CGFloat) -> CGFloat](nsbrowser/columnwidth(forcolumncontentwidth:).md)
  Returns the column width for the width of the given column’s content.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/rowheight)*