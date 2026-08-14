# NSTableColumn.ResizingOptions

**Framework**: AppKit  
**Kind**: struct

**Availability**:
- macOS ?+

## Declaration

```swift
struct ResizingOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](nstablecolumn/resizingoptions/init(rawvalue:).md)
### Constants
- [static var autoresizingMask: NSTableColumn.ResizingOptions](nstablecolumn/resizingoptions/autoresizingmask.md)
  Allows the table column to resize automatically in response to resizing the table view. The resizing behavior for the table view is set using the `NSTableView` method [`columnAutoresizingStyle`](nstableview/columnautoresizingstyle-swift.property.md).
- [static var userResizingMask: NSTableColumn.ResizingOptions](nstablecolumn/resizingoptions/userresizingmask.md)
  Allows the table column to be resized by the user.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [class NSTableHeaderView](nstableheaderview.md)
  An object that draws headers over a table view’s columns and handles mouse events in those headers.
- [class NSTableHeaderCell](nstableheadercell.md)
  An object that a table header view uses to draw the content of the column headers.
- [class NSTableRowView](nstablerowview.md)
  The view shown for a row in a table view.
- [class NSTableColumn](nstablecolumn.md)
  The display characteristics and identifier for a column in a table view.
- [class NSTableViewRowAction](nstableviewrowaction.md)
  A single action to present when the user swipes horizontally on a table row.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstablecolumn/resizingoptions)*