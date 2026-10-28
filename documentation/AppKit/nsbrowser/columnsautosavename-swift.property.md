# columnsAutosaveName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name used to automatically save the browser’s column configuration.

**Availability**:
- macOS

## Declaration

```swift
var columnsAutosaveName: NSBrowser.ColumnsAutosaveName { get set }
```

```objc
@property (copy) NSBrowserColumnsAutosaveName columnsAutosaveName;
```

## Discussion

Column configuration is defined as an array of column content widths. One width is saved for each level the user has reached. That is, the browser saves column width based on depth, not on unique paths. To do more complex column persistence, you should register for [`columnConfigurationDidChangeNotification`](./columnconfigurationdidchangenotification.md) and handle persistence yourself. This setting is persistent.

When this property is set to a value different than its current value, this property also reads in any column configuration data previously saved under the new value and applies the values to the browser.

## See Also

### Sizing
- [class func removeSavedColumns(withAutosaveName: NSBrowser.ColumnsAutosaveName)](./removesavedcolumns%28withautosavename%29.md)
  Removes the column configuration data stored under the given name from the application’s user defaults.
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
- [func setDefaultColumnWidth(CGFloat)](./setdefaultcolumnwidth%28_%29.md)
  Sets the default column width for new browser columns that do not otherwise have an initial width from defaults or the browser’s delegate.
- [var rowHeight: CGFloat](./rowheight.md)
  The height of the browser’s rows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbrowser/columnsautosavename-swift.property)*