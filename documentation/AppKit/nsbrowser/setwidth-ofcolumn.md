# setWidth(_:ofColumn:)

**Framework**: AppKit  
**Kind**: method

Sets the width of the specified column.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setWidth(_ columnWidth: CGFloat, ofColumn columnIndex: Int)
```

#### Discussion

This method can be used to set the initial width of browser columns unless the column sizing is automatic; [`setWidth(_:ofColumn:)`](nsbrowser/setwidth(_:ofcolumn:).md) does nothing if [`columnResizingType`](nsbrowser/columnresizingtype-swift.property.md) is [`NSBrowser.ColumnResizingType.autoColumnResizing`](nsbrowser/columnresizingtype-swift.enum/autocolumnresizing.md). To set the default width for new columns (that don’t otherwise have initial widths from defaults or via the delegate), use a `columnIndex` of –1. A value set for `columnIndex` of –1 is persistent. An [`columnConfigurationDidChangeNotification`](nsbrowser/columnconfigurationdidchangenotification.md) notification is posted (not immediately), if necessary, so that the browser can autosave the new column configuration.

## Parameters

- `columnWidth`: The new width of the specified column.
- `columnIndex`: The index of the column for which to set the width.

## See Also

- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](nsbrowserdelegate/browser(_:shouldsizecolumn:foruserresize:towidth:).md)
  Used to determine a column’s initial size.
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
- [func defaultColumnWidth() -> CGFloat](nsbrowser/defaultcolumnwidth.md)
  Returns the default column width of the browser’s columns.
- [func setDefaultColumnWidth(CGFloat)](nsbrowser/setdefaultcolumnwidth(_:).md)
  Sets the default column width for new browser columns that do not otherwise have an initial width from defaults or the browser’s delegate.
- [var rowHeight: CGFloat](nsbrowser/rowheight.md)
  The height of the browser’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setwidth(_:ofcolumn:))*