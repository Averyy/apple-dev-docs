# NSTableRowView

**Framework**: AppKit  
**Kind**: class

The view shown for a row in a table view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
class NSTableRowView
```

#### Overview

[`NSTableRowView`](nstablerowview.md) is responsible for displaying attributes associated with the row, including the selection highlight, and group row look.

## Topics

### Display Style
- [var isEmphasized: Bool](nstablerowview/isemphasized.md)
  Determines whether the row will draw with the alternate or secondary color (unless overridden).
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nstablerowview/interiorbackgroundstyle.md)
  Specifies how the subviews should draw.
- [var isFloating: Bool](nstablerowview/isfloating.md)
  Specifies whether the row is drawn using the floating style.
### Row Selection
- [var isSelected: Bool](nstablerowview/isselected.md)
  Determines whether the row is selected.
- [var selectionHighlightStyle: NSTableView.SelectionHighlightStyle](nstablerowview/selectionhighlightstyle.md)
  Specifies the selection highlight style.
### Drag and Drop
- [var draggingDestinationFeedbackStyle: NSTableView.DraggingDestinationFeedbackStyle](nstablerowview/draggingdestinationfeedbackstyle.md)
  Specifies the dragging destination feedback style.
- [var indentationForDropOperation: CGFloat](nstablerowview/indentationfordropoperation.md)
  Defines the amount the drag target for a row should be indented.
- [var isTargetForDropOperation: Bool](nstablerowview/istargetfordropoperation.md)
  Specifies whether this row will draw a drop indicator based on the current dragging feedback style.
### Row Grouping
- [var isGroupRowStyle: Bool](nstablerowview/isgrouprowstyle.md)
  Specifies whether this row view is a group row.
- [var numberOfColumns: Int](nstablerowview/numberofcolumns.md)
  Returns the number of columns represented by views in the table row view.
### Overriding Row View Display Characteristics
- [var backgroundColor: NSColor](nstablerowview/backgroundcolor.md)
  The background color of the row.
- [func drawBackground(in: NSRect)](nstablerowview/drawbackground(in:).md)
  Draws the background of the row in the rectangle.
- [func drawDraggingDestinationFeedback(in: NSRect)](nstablerowview/drawdraggingdestinationfeedback(in:).md)
  Draws the row’s dragging destination feedback when the entire row is a drop target.
- [func drawSelection(in: NSRect)](nstablerowview/drawselection(in:).md)
  Draws the selected row.
- [func drawSeparator(in: NSRect)](nstablerowview/drawseparator(in:).md)
  Draws the horizontal separator between table rows.
### Accessing A Row Column View
- [func view(atColumn: Int) -> Any?](nstablerowview/view(atcolumn:).md)
  Provides access to the given view at a particular column.
### Instance Properties
- [var isNextRowSelected: Bool](nstablerowview/isnextrowselected.md)
- [var isPreviousRowSelected: Bool](nstablerowview/ispreviousrowselected.md)

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
- [NSAccessibilityGroup](nsaccessibilitygroup.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAccessibilityRow](nsaccessibilityrow.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class NSTableHeaderView](nstableheaderview.md)
  An object that draws headers over a table view’s columns and handles mouse events in those headers.
- [class NSTableHeaderCell](nstableheadercell.md)
  An object that a table header view uses to draw the content of the column headers.
- [class NSTableColumn](nstablecolumn.md)
  The display characteristics and identifier for a column in a table view.
- [class NSTableViewRowAction](nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.
- [NSTableColumn.ResizingOptions](nstablecolumn/resizingoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablerowview)*