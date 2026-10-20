# NSTableColumn.ResizingOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- macOS

## Declaration

```swift
struct ResizingOptions
```

```c
enum NSTableColumnResizingOptions : NSUInteger;
```

## Topics

### Initializers
- [init(rawValue: UInt)](./resizingoptions/init%28rawvalue%29.md)
### Constants
- [static var autoresizingMask: NSTableColumn.ResizingOptions](./resizingoptions/autoresizingmask.md)
  Allows the table column to resize automatically in response to resizing the table view. The resizing behavior for the table view is set using the `NSTableView` method [`columnAutoresizingStyle`](../nstableview/columnautoresizingstyle-swift.property.md).
- [static var userResizingMask: NSTableColumn.ResizingOptions](./resizingoptions/userresizingmask.md)
  Allows the table column to be resized by the user.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Rows and Columns
- [class NSTableHeaderView](../nstableheaderview.md)
  An object that draws headers over a table view’s columns and handles mouse events in those headers.
- [class NSTableHeaderCell](../nstableheadercell.md)
  An object that a table header view uses to draw the content of the column headers.
- [class NSTableRowView](../nstablerowview.md)
  The view shown for a row in a table view.
- [class NSTableColumn](../nstablecolumn.md)
  The display characteristics and identifier for a column in a table view.
- [class NSTableViewRowAction](../nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/resizingoptions)*