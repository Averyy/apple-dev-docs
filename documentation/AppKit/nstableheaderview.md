# NSTableHeaderView

**Framework**: AppKit  
**Kind**: class

An object that draws headers over a table view’s columns and handles mouse events in those headers.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSTableHeaderView
```

#### Overview

[`NSTableHeaderView`](nstableheaderview.md) uses [`NSTableHeaderCell`](nstableheadercell.md) to implement its user interface.

## Topics

### Setting the table view
- [var tableView: NSTableView?](nstableheaderview/tableview.md)
  The [`NSTableView`](nstableview.md) instance that this table header view belongs to.
### Checking altered columns
- [var draggedColumn: Int](nstableheaderview/draggedcolumn.md)
  The index of the column that the user is dragging.
- [var draggedDistance: CGFloat](nstableheaderview/draggeddistance.md)
  The horizontal distance that the user has dragged a column.
- [var resizedColumn: Int](nstableheaderview/resizedcolumn.md)
  The index of the column that the user is resizing.
### Utility methods
- [func column(at: NSPoint) -> Int](nstableheaderview/column(at:).md)
  Returns the index of the column whose header lies under `aPoint` in the receiver, or –1 if no such column is found.
- [func headerRect(ofColumn: Int) -> NSRect](nstableheaderview/headerrect(ofcolumn:).md)
  Returns the rectangle containing the header tile for the column at `columnIndex`.

## Relationships

### Inherits From
- [NSView](nsview.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSViewToolTipOwner](nsviewtooltipowner.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSTableHeaderCell](nstableheadercell.md)
  An object that a table header view uses to draw the content of the column headers.
- [class NSTableRowView](nstablerowview.md)
  The view shown for a row in a table view.
- [class NSTableColumn](nstablecolumn.md)
  The display characteristics and identifier for a column in a table view.
- [class NSTableViewRowAction](nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.
- [NSTableColumn.ResizingOptions](nstablecolumn/resizingoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableheaderview)*