# NSTableHeaderCell

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that a table header view uses to draw the content of the column headers.

**Availability**:
- macOS

## Declaration

```swift
class NSTableHeaderCell
```

```objc
@interface NSTableHeaderCell : NSTextFieldCell
```

#### Overview

Subclasses of the `NSTableHeaderCell` class can override the [`drawInterior(withFrame:in:)`](./nscell/drawinterior%28withframe,in%29.md), [`edit(withFrame:in:editor:delegate:event:)`](./nscell/edit%28withframe,in,editor,delegate,event%29.md), and [`highlight(_:withFrame:in:)`](./nscell/highlight%28_,withframe,in%29.md) methods to change the way headers appear. This specific subclass is responsible for drawing the sort indicators. See the [`NSCell`](./nscell.md) class specification for information on overriding these methods.

See the [`NSTableView`](./nstableview.md) and [`NSTableHeaderCell`](./nstableheadercell.md) for more information.

## Topics

### Drawing Sorting Indicators
- [func drawSortIndicator(withFrame: NSRect, in: NSView, ascending: Bool, priority: Int)](./nstableheadercell/drawsortindicator%28withframe,in,ascending,priority%29.md)
  Draws a sorting indicator given a cell frame contained inside a view.
- [func sortIndicatorRect(forBounds: NSRect) -> NSRect](./nstableheadercell/sortindicatorrect%28forbounds%29.md)
  Returns the location to display the sorting indicator given `theRect`.

## Relationships

### Inherits From
- [NSTextFieldCell](./nstextfieldcell.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](./nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](./nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSUserInterfaceItemIdentification](./nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Rows and Columns
- [class NSTableHeaderView](./nstableheaderview.md)
  An object that draws headers over a table view’s columns and handles mouse events in those headers.
- [class NSTableRowView](./nstablerowview.md)
  The view shown for a row in a table view.
- [class NSTableColumn](./nstablecolumn.md)
  The display characteristics and identifier for a column in a table view.
- [class NSTableViewRowAction](./nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.
- [NSTableColumn.ResizingOptions](./nstablecolumn/resizingoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheadercell)*