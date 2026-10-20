# setDefaultColumnWidth(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the default column width for new browser columns that do not otherwise have an initial width from defaults or the browser’s delegate.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func setDefaultColumnWidth(_ columnWidth: CGFloat)
```

```objc
- (void) setDefaultColumnWidth:(CGFloat) columnWidth;
```

## Parameters

- `columnWidth`: The default column width to set.

## See Also

### Sizing
- [class func removeSavedColumns(withAutosaveName: NSBrowser.ColumnsAutosaveName)](./removesavedcolumns%28withautosavename%29.md)
  Removes the column configuration data stored under the given name from the application’s user defaults.
- [var columnsAutosaveName: NSBrowser.ColumnsAutosaveName](./columnsautosavename-swift.property.md)
  The name used to automatically save the browser’s column configuration.
- [NSBrowser.ColumnsAutosaveName](./columnsautosavename-swift.typealias.md)
- [func columnContentWidth(forColumnWidth: CGFloat) -> CGFloat](./columncontentwidth%28forcolumnwidth%29.md)
  Returns the content width for a given column width.
- [func columnWidth(forColumnContentWidth: CGFloat) -> CGFloat](./columnwidth%28forcolumncontentwidth%29.md)
  Returns the column width for the width of the given column’s content.
- [var columnResizingType: NSBrowser.ColumnResizingType](./columnresizingtype-swift.property.md)
  A constant indicating the browser’s column resizing type.
- [var prefersAllColumnUserResizing: Bool](./prefersallcolumnuserresizing.md)
  A Boolean that indicates whether the browser is set to resize all columns simultaneously rather than resizing a single column at a time.
- [func width(ofColumn: Int) -> CGFloat](./width%28ofcolumn%29.md)
  Returns the width of the specified column.
- [func setWidth(CGFloat, ofColumn: Int)](./setwidth%28_,ofcolumn%29.md)
  Sets the width of the specified column.
- [func defaultColumnWidth() -> CGFloat](./defaultcolumnwidth%28%29.md)
  Returns the default column width of the browser’s columns.
- [var rowHeight: CGFloat](./rowheight.md)
  The height of the browser’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setdefaultcolumnwidth(_:))*