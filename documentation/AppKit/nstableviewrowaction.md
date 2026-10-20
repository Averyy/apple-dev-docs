# NSTableViewRowAction

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A single action to present when the user swipes horizontally on a table row.

**Availability**:
- macOS 10.11+

## Declaration

```swift
class NSTableViewRowAction
```

```objc
@interface NSTableViewRowAction : NSObject
```

#### Overview

In an editable table, performing a horizontal swipe on a row reveals a button to delete the row by default. This class lets you define one or more custom actions to display for a given row in your table. Each instance of this class represents a single action to perform and includes the text, formatting information, and behavior for the corresponding button.

To add custom actions to your table view’s rows, implement the [`tableView(_:rowActionsForRow:edge:)`](./nstableviewdelegate/tableview%28_,rowactionsforrow,edge%29.md) method in your table view’s delegate object. In that method, create and return an array of actions for the specified row. The table handles the remaining work of displaying the action buttons and executing the appropriate handler block when the user clicks the button.

## Topics

### Creating a Table Row Action
- [convenience init(style: NSTableViewRowAction.Style, title: String, handler: (NSTableViewRowAction, Int) -> Void)](./nstableviewrowaction/init%28style,title,handler%29.md)
  Creates and returns a new table view row action object.
### Configuring the Action’s Appearance
- [var style: NSTableViewRowAction.Style](./nstableviewrowaction/style-swift.property.md)
  The style applied to the action button.
- [var title: String](./nstableviewrowaction/title.md)
  The title of the action button.
- [var backgroundColor: NSColor!](./nstableviewrowaction/backgroundcolor.md)
  The background color of the action button.
### Constants
- [NSTableViewRowAction.Style](./nstableviewrowaction/style-swift.enum.md)
  Constants that help define the appearance and behavior of action buttons.
### Instance Properties
- [var image: NSImage?](./nstableviewrowaction/image.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Rows and Columns
- [class NSTableHeaderView](./nstableheaderview.md)
  An object that draws headers over a table view’s columns and handles mouse events in those headers.
- [class NSTableHeaderCell](./nstableheadercell.md)
  An object that a table header view uses to draw the content of the column headers.
- [class NSTableRowView](./nstablerowview.md)
  The view shown for a row in a table view.
- [class NSTableColumn](./nstablecolumn.md)
  The display characteristics and identifier for a column in a table view.
- [NSTableColumn.ResizingOptions](./nstablecolumn/resizingoptions.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstableviewrowaction)*