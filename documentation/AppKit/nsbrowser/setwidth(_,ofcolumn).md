# setWidth(_:ofColumn:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the width of the specified column.

**Availability**:
- macOS

## Declaration

```swift
func setWidth(_ columnWidth: CGFloat, ofColumn columnIndex: Int)
```

```objc
- (void) setWidth:(CGFloat) columnWidth ofColumn:(NSInteger) columnIndex;
```

## Discussion

This method can be used to set the initial width of browser columns unless the column sizing is automatic; [`setWidth(_:ofColumn:)`](./setwidth%28_,ofcolumn%29.md) does nothing if [`columnResizingType`](./columnresizingtype-swift.property.md) is [`NSBrowser.ColumnResizingType.autoColumnResizing`](./columnresizingtype-swift.enum/autocolumnresizing.md). To set the default width for new columns (that don’t otherwise have initial widths from defaults or via the delegate), use a `columnIndex` of –1. A value set for `columnIndex` of –1 is persistent. An [`columnConfigurationDidChangeNotification`](./columnconfigurationdidchangenotification.md) notification is posted (not immediately), if necessary, so that the browser can autosave the new column configuration.

## Parameters

- `columnWidth`: The new width of the specified column.
- `columnIndex`: The index of the column for which to set the width.

## See Also

### Related Documentation
- [func browser(NSBrowser, shouldSizeColumn: Int, forUserResize: Bool, toWidth: CGFloat) -> CGFloat](../nsbrowserdelegate/browser%28_,shouldsizecolumn,foruserresize,towidth%29.md)
  Used to determine a column’s initial size.
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
- [func defaultColumnWidth() -> CGFloat](./defaultcolumnwidth%28%29.md)
  Returns the default column width of the browser’s columns.
- [func setDefaultColumnWidth(CGFloat)](./setdefaultcolumnwidth%28_%29.md)
  Sets the default column width for new browser columns that do not otherwise have an initial width from defaults or the browser’s delegate.
- [var rowHeight: CGFloat](./rowheight.md)
  The height of the browser’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/setwidth(_:ofcolumn:))*