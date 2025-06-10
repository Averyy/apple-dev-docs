# NSTableHeaderCell

**Framework**: AppKit  
**Kind**: class

An object that a table header view uses to draw the content of the column headers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTableHeaderCell
```

#### Overview

Subclasses of the `NSTableHeaderCell` class can override the [`drawInterior(withFrame:in:)`](nscell/drawinterior(withframe:in:).md), [`edit(withFrame:in:editor:delegate:event:)`](nscell/edit(withframe:in:editor:delegate:event:).md), and [`highlight(_:withFrame:in:)`](nscell/highlight(_:withframe:in:).md) methods to change the way headers appear. This specific subclass is responsible for drawing the sort indicators. See the [`NSCell`](nscell.md) class specification for information on overriding these methods.

See the [`NSTableView`](nstableview.md) and [`NSTableHeaderCell`](nstableheadercell.md) for more information.

## Topics

### Drawing Sorting Indicators
- [func drawSortIndicator(withFrame: NSRect, in: NSView, ascending: Bool, priority: Int)](nstableheadercell/drawsortindicator(withframe:in:ascending:priority:).md)
  Draws a sorting indicator given a cell frame contained inside a view.
- [func sortIndicatorRect(forBounds: NSRect) -> NSRect](nstableheadercell/sortindicatorrect(forbounds:).md)
  Returns the location to display the sorting indicator given `theRect`.

## Relationships

### Inherits From
- [NSTextFieldCell](nstextfieldcell.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTableHeaderView](nstableheaderview.md)
  An object that draws headers over a table view’s columns and handles mouse events in those headers.
- [class NSTableRowView](nstablerowview.md)
  The view shown for a row in a table view.
- [class NSTableColumn](nstablecolumn.md)
  The display characteristics and identifier for a column in a table view.
- [class NSTableViewRowAction](nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.
- [NSTableColumn.ResizingOptions](nstablecolumn/resizingoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheadercell)*