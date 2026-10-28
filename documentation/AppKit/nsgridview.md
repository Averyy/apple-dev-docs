# NSGridView

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A container that aligns views in a flexible grid of rows and columns.

**Availability**:
- macOS 10.12+

## Declaration

```swift
class NSGridView
```

```objc
@interface NSGridView : NSView
```

## Overview

A grid view helps you lay out content, such as photos or thumbnails, in a row-column arrangement similar to a spreadsheet. Within a grid view, an item that occupies a single row-column intersection is represented by an [`NSGridCell`](./nsgridcell.md) object.

## Topics

### Creating a Grid View
- [convenience init(numberOfColumns: Int, rows: Int)](./nsgridview/init%28numberofcolumns,rows%29.md)
  Creates a newly allocated grid view object with the specified number of columns and rows.
- [convenience init(views: [[NSView]])](./nsgridview/init%28views%29.md)
  Creates a newly allocated grid view object with the specified array of arrays of views.
- [init(frame: NSRect)](./nsgridview/init%28frame%29.md)
  Creates a newly allocated grid view object with the specified frame rectangle.
- [init?(coder: NSCoder)](./nsgridview/init%28coder%29.md)
  Creates a newly allocated grid view object from the coder.
### Getting Information About the Grid
- [var numberOfRows: Int](./nsgridview/numberofrows.md)
  The number of rows in the grid view.
- [var numberOfColumns: Int](./nsgridview/numberofcolumns.md)
  The number of columns in the grid view.
- [func index(of: NSGridColumn) -> Int](./nsgridview/index%28of%29-32sdd.md)
  Returns the index of the specified grid column.
- [func row(at: Int) -> NSGridRow](./nsgridview/row%28at%29.md)
  Returns the grid row object at the specified index.
- [func column(at: Int) -> NSGridColumn](./nsgridview/column%28at%29.md)
  Returns the grid column object at the specified index.
- [func index(of: NSGridRow) -> Int](./nsgridview/index%28of%29-6zs2o.md)
  Returns the index of the specified grid row.
### Adding, Removing, and Moving Rows
- [func addRow(with: [NSView]) -> NSGridRow](./nsgridview/addrow%28with%29.md)
  Adds an array of views to a new row.
- [func insertRow(at: Int, with: [NSView]) -> NSGridRow](./nsgridview/insertrow%28at,with%29.md)
  Inserts the array of view objects into the grid view at the index.
- [func removeRow(at: Int)](./nsgridview/removerow%28at%29.md)
  Removes the row from the grid view at the index.
- [func moveRow(at: Int, to: Int)](./nsgridview/moverow%28at,to%29.md)
  Moves the specified row to the new row location.
### Adding, Removing, and Moving Columns
- [func addColumn(with: [NSView]) -> NSGridColumn](./nsgridview/addcolumn%28with%29.md)
  Adds a new column containing the array of views.
- [func insertColumn(at: Int, with: [NSView]) -> NSGridColumn](./nsgridview/insertcolumn%28at,with%29.md)
  Inserts the array of view objects at the specified index.
- [func removeColumn(at: Int)](./nsgridview/removecolumn%28at%29.md)
  Removes the column from the grid view at the specified index.
- [func moveColumn(at: Int, to: Int)](./nsgridview/movecolumn%28at,to%29.md)
  Moves the specified column to a new column location.
### Managing Grid Spacing and Alignment
- [class let sizedForContent: CGFloat](./nsgridview/sizedforcontent.md)
  The default value for row and column sizes.
- [var columnSpacing: CGFloat](./nsgridview/columnspacing.md)
  The column spacing for the grid view.
- [var rowSpacing: CGFloat](./nsgridview/rowspacing.md)
  The row spacing for the grid view.
- [var rowAlignment: NSGridRow.Alignment](./nsgridview/rowalignment.md)
  The row alignment for the grid view.
- [var xPlacement: NSGridCell.Placement](./nsgridview/xplacement.md)
  The placement of the cell within the grid column.
- [var yPlacement: NSGridCell.Placement](./nsgridview/yplacement.md)
  The placement of the cell within the grid row.
### Creating and Merging Cells
- [func cell(atColumnIndex: Int, rowIndex: Int) -> NSGridCell](./nsgridview/cell%28atcolumnindex,rowindex%29.md)
  Returns the grid cell object at the specified column and row index.
- [func cell(for: NSView) -> NSGridCell?](./nsgridview/cell%28for%29.md)
  Returns the grid cell object that contains the given view or one of its ancestors.
- [func mergeCells(inHorizontalRange: NSRange, verticalRange: NSRange)](./nsgridview/mergecells%28inhorizontalrange,verticalrange%29.md)
  Expands the cell at the top-leading corner of the horizontal and vertical range to cover the entire area.

## Relationships

### Inherits From
- [NSView](./nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](./nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](./nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](./nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](./nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](./nstouchbarprovider.md)
- [NSUserActivityRestoring](./nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgridview)*